package com.google.challenges;

public class Answer {

    public static final int MAX_WIDTH = 20, MAX_HEIGHT = 20;

    public static int answer(int[][] maze) {
        int minLength = MAX_WIDTH * MAX_HEIGHT;
        for (int row = 0; row < maze.length; row++) {
            for (int col = 0; col < maze[row].length; col++) {
                if (maze[row][col] == 1) {
                    maze[row][col] = 0;
                    int smallestValue = smallest(maze);
                    if (smallestValue != -1) {
                        minLength = Math.min(minLength, smallestValue);
                    }
                    maze[row][col] = 1;
                }
            }
        }
        if (minLength < MAX_WIDTH * MAX_HEIGHT) {
            return minLength;
        } else {
            return smallest(maze);
        }
    }

    public static int smallest(int[][] maze) {
        int[][] cache = new int[maze.length][];
        for (int i = 0; i < cache.length; i++) {
            cache[i] = new int[maze[i].length];
            for (int j = 0; j < cache[i].length; j++) {
                cache[i][j] = -1;
            }
        }
        recSmallest(maze, cache, 0, 0, 0);
        int l = cache.length - 1;
        int[] lastRow = cache[l];
        int lastElement = cache[l][lastRow.length - 1];
        if (lastElement > 0) {
            return lastElement;
        } else {
            return -1;
        }
    }

    public static void recSmallest(int[][] maze, int[][] cache, int x, int y,
                                   int dist) {
        dist += 1;
        int h = maze.length - 1;
        if (y < 0 || y > h) return;
        int w = maze[y].length - 1;
        if (x < 0 || x > w) return;
        if (cache[y][x] <= dist && cache[y][x] != -1) return;
        if (maze[y][x] == 1) return;

        cache[y][x] = dist;

        int[][] nextSteps = new int[][] {
            new int[] { x, y + 1 },
            new int[] { x + 1, y },
            new int[] { x, y - 1 },
            new int[] { x - 1, y }
        };
        for (int i = 0; i < nextSteps.length; i++) {
            int nextX = nextSteps[i][0];
            int nextY = nextSteps[i][1];
            recSmallest(maze, cache, nextX, nextY, dist);
        }
    }
}
