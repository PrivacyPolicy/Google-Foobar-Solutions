package com.google.challenges;

import java.util.Arrays;
import java.util.ArrayList;
import java.awt.Color;

public class Answer {

    public double[] dimensions, captain_position, badguy_position;
    public int distance;

    public /*static*/ int answer(int[] dimensions, int[] captain_position, int[] badguy_position, int distance) {
        this.dimensions = new double[] {
            (double) dimensions[0],
            (double) dimensions[1]
        };
        this.captain_position = new double[] {
            (double) captain_position[0],
            (double) captain_position[1]
        };
        this.badguy_position = new double[] {
            (double) badguy_position[0],
            (double) badguy_position[1]
        };
        this.distance = distance;

        return 0;
    }

    // determine if the given laser will bounce onto the badguy
    public double willItHit(int[] vectDir, ArrayList<double[]> collisions) {
        double[] start = new double[] {
            captain_position[0],
            captain_position[1]
        };
        double dist = 0;
        double latestDist = 0;
        double[] lastStart = start;
        double[] col = new double[] {-1d, -1d};
        while (dist < distance && !hitCaptain(col) && !hitBadguy(col)) {
            col = edgeCollision(start, vectDir);
            latestDist = calcDistance(start, col);
            dist += latestDist;
            collisions.add(col);
            int wall = -1;
            if (eq(col[0], 0)) wall = WALL_LEFT;
            if (eq(col[0], dimensions[0])) wall = WALL_RIGHT;
            if (eq(col[1], 0)) wall = WALL_TOP;
            if (eq(col[1], dimensions[1])) wall = WALL_BOTTOM;
            if (eq(col[0], 0) && eq(col[1], 0)
                || eq(col[0], dimensions[0]) && eq(col[1], 0)
                || eq(col[0], 0) && eq(col[1], dimensions[1])
                || eq(col[0], dimensions[0]) && eq(col[1], dimensions[1])) {
                wall = WALL_CORNER;
            }
            vectDir = reflect(vectDir, wall);
            lastStart = start;
            start = col;
        }
        // reduce length of last lazer to accurately represent distance
        double overshoot = dist - distance;
        double dY = col[1] - lastStart[1];
        double dX = col[0] - lastStart[0];
        double distMult = (latestDist - overshoot) / latestDist;
        double newX = distMult * dX + lastStart[0];
        double newY = distMult * dY + lastStart[1];
        collisions.set(collisions.size() - 1, new double[] {newX, newY});
        return dist - overshoot;
    }

    // if two doubles are close enough to be considered equal
    public static final double EPSILON = 0.0000001;
    public static boolean eq(double a, double b) {
        return Math.abs(a - b) < EPSILON;
    }
    public static boolean eq(int a, int b) {
        return eq((double) a, (double) b);
    }
    public static boolean eq(int a, double b) {
        return eq((double) a, b);
    }
    public static boolean eq(double a, int b) {
        return eq(a, (double) b);
    }

    // true if the signs of the numbers are the same, false otherwise
    public static boolean sameSign(double a, double b) {
        if (eq(a, 0)) a = 0d;
        if (eq(b, 0)) b = 0d;
        return (a < 0) == (b < 0);
    }

    // true of point == captain_position, false otherwise
    public boolean hitCaptain(double[] point) {
        return eq(point[0], captain_position[0]) && eq(point[1], captain_position[1]);
    }

    // true of point == badguy_position, false otherwise
    public boolean hitBadguy(double[] point) {
        return eq(point[0], badguy_position[0]) && eq(point[1], badguy_position[1]);
    }

    // return a reflected vector based off of what wall was hit
    public static final int WALL_TOP    = 0b0000;
    public static final int WALL_BOTTOM = 0b0001;
    public static final int WALL_LEFT   = 0b0010;
    public static final int WALL_RIGHT  = 0b0100;
    public static final int WALL_CORNER = 0b1000;
    public int[] reflect(int[] vectDir, int wall) {
        switch (wall) {
            case WALL_TOP:
            case WALL_BOTTOM:
                vectDir[1] = -vectDir[1];
                break;
            case WALL_LEFT:
            case WALL_RIGHT:
                vectDir[0] = -vectDir[0];
                break;
            case WALL_CORNER:
                vectDir[0] = -vectDir[0];
                vectDir[1] = -vectDir[1];
                break;
            default:
                // Throw error
                break;
        }
        return vectDir;
    }

    // find the location of the nearest edge collision
    public double[] edgeCollision(double[] start, int[] vectDir) {
        double x = 0f, y = 0f;
        if (vectDir[0] == 0 && vectDir[1] == 0) {
            return new double[] {-1f, -1f};
        }

        // first, check if it collides with either of the people
        if (vectDir[0] != 0) {
            double dY = captain_position[1] - start[1];
            double dX = captain_position[0] - start[0];
            double m = vectDir[1] / (double) vectDir[0];
            if (eq(m, dY / dX) && !eq(captain_position[0], start[0])
                && sameSign(vectDir[1], dY) && sameSign(vectDir[0], dX)) {
                return captain_position;
            }

            dY = badguy_position[1] - start[1];
            dX = badguy_position[0] - start[0];
            if (eq(m, dY / dX) && !eq(badguy_position[0], start[0])
                && sameSign(vectDir[1], dY) && sameSign(vectDir[0], dX)) {
                return badguy_position;
            }
        } else {
            if (eq(captain_position[0], start[0])
                && !eq(start[1], captain_position[1])
                && sameSign(vectDir[1], captain_position[1] - start[1])) {
                return captain_position;
            }
            if (eq(badguy_position[0], start[0])
                && !eq(start[1], badguy_position[1])
                && sameSign(vectDir[1], badguy_position[1] - start[1])) {
                return badguy_position;
            }
        }

        // going to hit the top or bottom (or left or right)?
        double xGoal = (vectDir[0] < 0) ? 0 : dimensions[0];
        double yGoal = (vectDir[1] > 0) ? dimensions[1] : 0;

        // check for top/bottom collision
        if (vectDir[1] != 0) {
            x = start[0] + (yGoal - start[1]) * vectDir[0] / (double)vectDir[1];
            if (x >= 0 && x <= dimensions[0]) {
                return new double[] {x, yGoal};
            }
        }

        // check for left/right collision
        if (vectDir[0] != 0) {
            y = -vectDir[1] / (double)vectDir[0] * (start[0] - xGoal) + start[1];
            if (y >= 0 && y <= dimensions[1]) {
                return new double[] {xGoal, y};
            }
        }

        return new double[] {-1f, -1f};
    }

    public double[] edgeCollision(int[] start, int[] vectDir) {
        double[] a = new double[] { (double) start[0], (double) start[1] };
        return edgeCollision(a, vectDir);
    }

    public double calcDistance(double[] p1, double[] p2) {
        double a = p1[0] - p2[0], b = p1[1] - p2[1];
        return Math.sqrt(a * a + b * b);
    }

    public double calcDistance(int[] p1, int[] p2) {
        double[] a = new double[] { (double) p1[0], (double) p1[1] };
        double[] b = new double[] { (double) p2[0], (double) p2[1] };
        return calcDistance(a, b);
    }
    public double calcDistance(int[] p1, double[] p2) {
        double[] a = new double[] { (double) p1[0], (double) p1[1] };
        return calcDistance(a, p2);
    }
    public double calcDistance(double[] p1, int[] p2) {
        double[] b = new double[] { (double) p2[0], (double) p2[1] };
        return calcDistance(p1, b);
    }

    public double calcD(int wall) {
        double[] A = captain_position;
        double[] B = badguy_position;
        double d = 0;
        if (wall == WALL_TOP || wall == WALL_BOTTOM) {
            double wallY = (wall == WALL_BOTTOM) ? 0 : dimensions[1];
            double yHeight = Math.abs(B[1] - wallY);
            double d0 = (A[0] - B[0]) * yHeight / (B[1] - A[1] + 2 * yHeight);
            double d1 = (A[0] - B[0]) * yHeight / (B[1] - A[1] - 2 * yHeight);
            d = Math.max(d0, d1);
        } else if (wall == WALL_LEFT || wall == WALL_RIGHT) {
            double wallX = (wall == WALL_LEFT) ? 0 : dimensions[0];
            double xHeight = Math.abs(B[0] - wallX);
            double d0 = (B[1] - A[1]) * xHeight / (A[0] - B[0] - 2 * xHeight);
            double d1 = (B[1] - A[1]) * xHeight / (A[0] - B[0] + 2 * xHeight);
            d = Math.max(d0, d1);
        }
        return d;
    }

    public static double determinant(double[][] matrix) { // method sig. takes a matrix (two dimensional array), returns determinant.
        double sum = 0;
        short s;
        if (matrix.length == 1) {  // bottom case of recursion. size 1 matrix determinant is itself.
            return(matrix[0][0]);
        }
        for (int i = 0; i < matrix.length; i++) { // finds determinant using row-by-row expansion
            double[][] smaller = new double[matrix.length - 1][matrix.length - 1]; // creates smaller matrix- values not in same row, column
            for (int a = 1; a < matrix.length; a++) {
                for (int b = 0; b < matrix.length; b++) {
                    if (b < i) {
                        smaller[a - 1][b] = matrix[a][b];
                    } else if (b > i) {
                        smaller[a - 1][b - 1] = matrix[a][b];
                    }
                }
            }
            if (i % 2 == 0) { // sign changes based on i
                s = 1;
            } else {
                s = -1;
            }
            sum += s * matrix[0][i] * determinant(smaller); // recursive step: determinant of larger determined by smaller.
        }
        return(sum); // returns determinant value. once stack is finished, returns final determinant.
    }

    public double[] calcReflectPoint(int wall, double[] a, double[] b) {
        if (wall == WALL_TOP || wall == WALL_BOTTOM) {
            double y = (wall == WALL_TOP) ? dimensions[1] : 0;
            double x = -a[1] * b[0] + y * b[0] - b[1] * a[0] + y * a[0];
            return new double[] {x / (-a[1] - b[1] + 2 * y), y};
        } else if (wall == WALL_LEFT || wall == WALL_RIGHT) {
            double x = (wall == WALL_LEFT) ? 0 : dimensions[0];
            double y = -a[1] * b[0] + x * b[1] - b[1] * a[0] + x * a[1];
            return new double[] {x, y / (-a[0] - b[0] + 2 * x)};
        }
        return new double[] {-1, -1};
    }

    // solve a n x n + 1 matrix that represents a system of n equations
    public double[] matrixSolve(double[][] matrix) {
        double[] returnArray = new double[matrix.length];
        double[][] tempMatrix = new double[matrix.length][matrix.length + 1];
        int lastInd = matrix.length;
        double[][] firstHalfMatrix = new double[matrix.length][matrix.length];
        double firstHalfDeterm;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {
                firstHalfMatrix[i][j] = matrix[i][j];
            }
        }
        firstHalfDeterm = determinant(firstHalfMatrix);
        // for each variable
        for (int i = 0; i < matrix.length; i++) {
            // copy matrix
            for (int j = 0; j < matrix.length; j++) {
                for (int k = 0; k < matrix.length; k++) {
                    if (k == i) {
                        tempMatrix[j][k] = matrix[j][lastInd];
                    } else {
                        tempMatrix[j][k] = matrix[j][k];
                    }
                }
            }
            returnArray[i] = determinant(tempMatrix) / firstHalfDeterm;
        }
        return returnArray;
    }

    // return the matrix values for the given variables
    // x coord of each reflection/end point
    public double[] matrixSetupRow(double xY, double yY, double zY) {
        return new double[] {
            yY - zY,
            xY + zY - 2 * yY,
            yY - xY
        };
    }

    // a and b are the x, y coords of the start and end points, respectively
    // walls is a list of which wall is reflected each time
    // walls for now is > 1
    public double[][] matrixSetup(double[] a, double[] b, int[] walls) {
        int l = walls.length;
        // n = 1 if wall is reflect y else 0 for reflect x
        // note: n ^ 1 == oposite of n
        int n = (walls[0] == WALL_TOP || walls[0] == WALL_BOTTOM) ? 1 : 0;

        // handle edge case where there is only one reflection
        if (l == 1) {
            double[] row1 = matrixSetupRow(a[n], yForWall(walls[0]), b[n]);
            return new double[][] {
                {
                    row1[1], -a[n ^ 1] * row1[0] - b[n ^ 1] * row1[2]
                }
            };
        }
        // initialze matrix
        double[][] matrix = new double[l][l + 1];
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l + 1; j++) {
                matrix[i][j] = 0;
            }
        }
        // handle the general case
        double[] row1;
        if (walls[0] == WALL_TOP || walls[0] == WALL_BOTTOM) {
            row1 = matrixSetupRow(a[1],
                                  getYForWall(walls[0]),
                                  getYForWall(walls[1]));
            System.out.println("ay| " + a[1]);
            System.out.println("ay| " + getYForWall(walls[0]));
            System.out.println("ay| " + getYForWall(walls[1]));
            System.out.println();
        } else {
            row1 = matrixSetupRow(a[0],
                                  getXForWall(walls[0]),
                                  getXForWall(walls[1]));
            System.out.println("ax| " + a[0]);
            System.out.println("ax| " + getXForWall(walls[0]));
            System.out.println("ax| " + getXForWall(walls[1]));
            System.out.println();
        }
        matrix[0][0] = row1[1];
        matrix[0][1] = row1[2];
        matrix[0][l] = -a[n] * row1[0];
        double[] row;
        for (int i = 0; i < l - 2; i++) {
            if (walls[i + 1] == WALL_TOP || walls[i + 1] == WALL_BOTTOM) {
                row = matrixSetupRow(getYForWall(walls[i]),
                                     getYForWall(walls[i + 1]),
                                     getYForWall(walls[i + 2]));
                System.out.println("by| " + getYForWall(walls[i]));
                System.out.println("by| " + getYForWall(walls[i + 1]));
                System.out.println("by| " + getYForWall(walls[i + 2]));
                System.out.println();
            } else {
                row = matrixSetupRow(getXForWall(walls[i]),
                                     getXForWall(walls[i + 1]),
                                     getXForWall(walls[i + 2]));
               System.out.println("bx| " + getXForWall(walls[i]));
               System.out.println("bx| " + getXForWall(walls[i + 1]));
               System.out.println("bx| " + getXForWall(walls[i + 2]));
               System.out.println();
            }
            matrix[i + 1][i] = row[0];
            matrix[i + 1][i + 1] = row[1];
            matrix[i + 1][i + 2] = row[2];
        }
        n = (walls[l - 1] == WALL_TOP || walls[l - 1] == WALL_BOTTOM) ? 1 : 0;
        double[] lastRow;
        if (walls[l - 1] == WALL_TOP || walls[l - 1] == WALL_BOTTOM) {
            lastRow = matrixSetupRow(getYForWall(walls[l - 2]), getYForWall(walls[l - 1]), b[1]);
            System.out.println("cy| " + getYForWall(walls[l - 2]));
            System.out.println("cy| " + getYForWall(walls[l - 1]));
            System.out.println("cy| " + b[1]);
            System.out.println();
        } else {
            lastRow = matrixSetupRow(getXForWall(walls[l - 2]), getXForWall(walls[l - 1]), b[0]);
            System.out.println("cx| " + getXForWall(walls[l - 2]));
            System.out.println("cx| " + getXForWall(walls[l - 1]));
            System.out.println("cx| " + b[0]);
            System.out.println();
        }
        matrix[l - 1][l - 2] = lastRow[0];
        matrix[l - 1][l - 1] = lastRow[1];
        matrix[l - 1][l] = -b[n ^ 1] * lastRow[2];

        return matrix;
    }

    // return the y-coordinate of a given wall
    public double yForWall(int wall) {
        switch (wall) {
            case WALL_RIGHT:
                return dimensions[0];
            case WALL_TOP:
                return dimensions[1];
            case WALL_BOTTOM:
            case WALL_LEFT:
                return 0;
            default:
                return -1;
        }
    }

    public double getXForWall(int wall) {
        return (wall == WALL_RIGHT) ? dimensions[0] : 0;
    }
    public double getYForWall(int wall) {
        return (wall == WALL_TOP) ? dimensions[1] : 0;
    }

    // do some fancy maths to calculate all reflection points
    public double[][] calcReflectPoints(double[] a, double[] b, int[] walls) {
        double[][] matrix = matrixSetup(a, b, walls);
        double[] xSpots = matrixSolve(matrix);
        double[][] spots = new double[2 + walls.length][2];
        spots[0][0] = a[0];
        spots[0][1] = a[1];
        spots[walls.length + 1][0] = b[0];
        spots[walls.length + 1][1] = b[1];
        for (int i = 1; i < spots.length - 1; i++) {
            int wall = walls[i - 1];
            if (wall == WALL_TOP || wall == WALL_BOTTOM) {
                spots[i][0] = xSpots[i - 1];
                spots[i][1] = yForWall(wall);
            } else {
                spots[i][0] = yForWall(wall);
                spots[i][1] = xSpots[i - 1];
            }
        }
        return spots;
    }

    private static final int[][] shots = new int[][] {
        new int[] {1, 0},
        new int[] {1, 2},
        new int[] {1, -2},
        new int[] {3, 2},
        new int[] {3, -2}, // 4
        new int[] {-3, -2},
        new int[] {-3, 2},
        new int[] {-10, 3},
    };

    public static void main(String[] args) {
        Answer a = new Answer();
        // int[] dim = new int[] {300, 275};
        // int[] gPos = new int[] {150, 150};
        // int[] bPos = new int[] {185, 100};
        // int dist = 500;
        // int[] dim = new int[] {3, 2};
        // int[] gPos = new int[] {1, 1};
        // int[] bPos = new int[] {2, 1};
        // int dist = 4;
        // int[] dim = new int[] {2, 4};
        // int[] gPos = new int[] {2, 4};
        // int[] bPos = new int[] {2, 0};
        // int dist = 4;
        int[] dim = new int[] {4, 2};
        int[] gPos = new int[] {1, 0};
        int[] bPos = new int[] {3, 2};
        int dist = 9;
        a.answer(dim, gPos, bPos, dist);
        //
        //
        int[] walls = new int[] {a.WALL_LEFT, a.WALL_TOP, a.WALL_BOTTOM, a.WALL_RIGHT};
        // double[][] matrix = a.matrixSetup(a.captain_position, a.badguy_position, walls);
        // for (int i = 0; i < matrix.length; i++) {
        //     System.out.println(Arrays.toString(matrix[i]));
        // }
        System.out.println("The lasers bounce all around! Specifically, at:");
        double[][] reflectPoints = a.calcReflectPoints(a.captain_position, a.badguy_position, walls);
        for (int i = 0; i < reflectPoints.length; i++) {
            System.out.println(Arrays.toString(reflectPoints[i]));
        }
        //
        //
        // int[][] aM = new int[][] {
        //     new int[] {6, -3},
        //     new int[] {3, 3}
        // };
        // int[][] bM = new int[][] {
        //     new int[] {1, 6},
        //     new int[] {2, 3}
        // };
        // double[][] cM = new double[][] {
        //     new double[] {1+0-2*2, -1*(1-2), -1*0*(2-0)},
        //     new double[] {(0-1), 2+1-2*0, 4*(2-0)}
        // };
        // cM = new double[][] {
        //     new double[] {-3, 1, 0, 0},
        //     new double[] {-2, 4, -2, 0},
        //     new double[] {0, 1, -3, -12}
        // };
        // double[] xy = a.matrixSolve(cM);
        // x = determinant(new int[][] {
        //     new int[] {1, -3},
        //     new int[] {2, 3}
        // });
        // System.out.println(Arrays.toString(xy));
        //
        //
        // a.answer(dim, gPos, bPos, dist);
        // int wall = WALL_RIGHT;
        // double[] rPos = a.calcReflectPoint(wall, a.captain_position, a.badguy_position);
        // System.out.println(Arrays.toString(rPos));
        //
        //
        // double d = a.calcD(wall);
        // double c = Math.abs(bPos[1] - gPos[1]) - d;
        // double wallX = (wall == WALL_RIGHT) ? 0 : dim[0];
        // double alpha = Math.atan2(d, Math.abs(wallX - bPos[0]));
        // double laserDist = -1;
        // if (!eq(alpha, Math.PI / 2)) { // straight angle
        //     laserDist = (c + d) / Math.sin(alpha);
        // }
        // System.out.println("d = " + d + ", c = " + c + ", alpha = " + alpha);
        // System.out.println(laserDist);
        // System.out.println(5);
        //
        //
        // ArrayList<double[]> collisions = new ArrayList<>();
        // int[] shot = shots[7];
        // System.out.println("Laser shot from " + Arrays.toString(gPos) + " at " + Arrays.toString(shot) + " bounces at:");
        // double travelDist = a.willItHit(shot, collisions);
        // for (int i = 0; i < collisions.size(); i++) {
        //     double[] col = collisions.get(i);
        //     System.out.println(Arrays.toString(col));
        // }
        // if (a.hitBadguy(collisions.get(collisions.size() - 1))) {
        //     System.out.println("Where it hit the bad guy! Yay!");
        // } else if (a.hitCaptain(collisions.get(collisions.size() - 1))) {
        //     System.out.println("Where it hit the captain! Oh no!");
        // } else {
        //     System.out.println("Before fading out.");
        // }
        // System.out.println("Travelling a total of " + travelDist);
        //
        // LaserDisplay ld = new LaserDisplay(dim[0], dim[1]);
        // ld.pane.addDot(gPos[0], gPos[1], Color.GREEN);
        // ld.pane.addDot(bPos[0], bPos[1], Color.RED);
        // double[] start = new double[] { (double) gPos[0], (double) gPos[1] };
        // for (int i = 0; i < collisions.size(); i++) {
        //     double[] c = collisions.get(i);
        //     ld.pane.addLine(start[0], start[1], c[0], c[1], Color.BLUE);
        //     start = c;
        // }
    }

}
