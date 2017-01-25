package com.google.challenges;

import java.util.ArrayList;
import java.util.Arrays;

import javax.swing.border.EmptyBorder;
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;

public class LaserDisplay extends JFrame implements ChangeListener {
	private final JButton b = new JButton();
    public TestPane pane;

    private static final int SLIDER_MULT = 100;

	public LaserDisplay(int cols, int rows) {
		super();
		this.setTitle("Laser Display");
		this.getContentPane().setLayout(new BorderLayout());
		this.setBounds(100 * 3, 100 * 3, 180 * 3, 140 * 3);

        pane = new TestPane(180 * 3, 140 * 3, cols, rows);
        this.add(pane);

        JSlider angle = new JSlider(JSlider.HORIZONTAL, 0,
                                    (int) Math.round(Math.PI * 2 * SLIDER_MULT),
                                    (int) Math.round(Math.PI / 4 * SLIDER_MULT));
        angle.setMajorTickSpacing((int) Math.round(Math.PI / 2 * SLIDER_MULT));
        angle.setMinorTickSpacing((int) Math.round(Math.PI / 4 * SLIDER_MULT));
        angle.setPaintTicks(true);
        angle.setPaintLabels(false);
        angle.addChangeListener(this);
        this.add(angle, BorderLayout.SOUTH);

        this.pack();
		this.setVisible(true);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	private JButton makeButton() {
		b.setText("Click me!");
		b.setBounds(40, 40, 100, 30);
		b.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(b, "Hello World!");
			}
		});
		return b;
	}

    public void stateChanged(ChangeEvent e) {
        JSlider source = (JSlider) e.getSource();
        double angleValue = (double) source.getValue() / SLIDER_MULT;

        int x = (int) Math.floor(Math.cos(angleValue) * 10000000);
        int y = (int) Math.floor(Math.sin(angleValue) * 10000000);

        int[] shot = new int[] { x, y };

        Answer a = new Answer();
        // int[] dim = new int[] {300, 275};
        // int[] gPos = new int[] {150, 150};
        // int[] bPos = new int[] {185, 100};
        // int dist = 500;
        int[] dim = new int[] {4, 2};
        int[] gPos = new int[] {1, 0};
        int[] bPos = new int[] {3, 2};
        int dist = 9;
        a.answer(dim, gPos, bPos, dist);
        ArrayList<double[]> collisions = new ArrayList<>();

        double travelDist = a.willItHit(shot, collisions);
        double[] start = new double[] { (double) gPos[0], (double) gPos[1] };
        pane.removeLines();
        for (int i = 0; i < collisions.size(); i++) {
            double[] c = collisions.get(i);
            pane.addLine(start[0], start[1], c[0], c[1], Color.BLUE);
            start = c;
        }
        // invalidate();
        pane.repaint();
    }

	// public static void main(String[] args) {
	// 	LaserDisplay ld = new LaserDisplay();
    //     // ld.pane.addLine(1, 1, 1.5, 2, Color.BLUE);
    //     // ld.pane.addLine(1.5, 2, 2, 1, Color.BLUE);
    // }

    public class TestPane extends JPanel {

        int width, height, rows, columns;
        ArrayList<Line> lines = new ArrayList<>();
        ArrayList<Dot> dots = new ArrayList<>();

        public TestPane(int width, int height, int columns, int rows) {
            super();
            this.width = width;
            this.height = height;
            this.rows = rows;
            this.columns = columns;
            setBorder(new EmptyBorder(20, 20, 20, 20));
        }

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(width, height);
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2 = (Graphics2D) g.create();

            int dl = getInsets().left;
            int dt = getInsets().top;
            int dw = getWidth() - dl - getInsets().right;
            int dh = getHeight() - dt - getInsets().bottom;

            float htOfRow = dh / (float) rows;
            for (int k = 0; k <= rows; k++) {
                g.drawLine(dl, (int) (k * htOfRow + dt),
                           dw + dl, (int) (k * htOfRow + dt));
            }

            float wdOfRow = dw / (float) columns;
            for (int k = 0; k <= columns; k++) {
                g.drawLine((int) (k * wdOfRow + dl), dt,
                           (int) (k * wdOfRow + dl), dh + dt);
            }

            // draw lines
            for (int i = 0; i < lines.size(); i++) {
                Line line = lines.get(i);
                g2.setPaint(line.color);
                g2.drawLine((int) (dl + line.x1 * wdOfRow),
                            (int) (dt + (rows - line.y1) * htOfRow),
                            (int) (dl + line.x2 * wdOfRow),
                            (int) (dt + (rows - line.y2) * htOfRow));
            }

            // draw dots
            for (int i = 0; i < dots.size(); i++) {
                Dot dot = dots.get(i);
                g2.setPaint(dot.color);
                double RADIUS = 10d;
                Ellipse2D.Double circle = new Ellipse2D.Double(dl + dot.x * wdOfRow - RADIUS / 2, dt + (rows - dot.y) * htOfRow - RADIUS / 2, RADIUS, RADIUS);
                g2.fill(circle);
            }
        }

        public void addLine(double x1, double y1, double x2, double y2, Color color) {
            lines.add(new Line(x1, y1, x2, y2, color));
        }

        public void removeLines() {
            lines = new ArrayList<>();
        }

        public void addDot(double x, double y, Color color) {
            dots.add(new Dot(x, y, color));
        }
    }

    public class Line {
        public double x1 = 0, y1 = 0, x2 = 0, y2 = 0;
        public Color color = Color.BLACK;
        public Line(double x1, double y1, double x2, double y2, Color color) {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
            this.color = color;
        }
    }

    public class Dot {
        public double x = 0, y = 0;
        public Color color = Color.BLACK;
        public Dot(double x, double y, Color color) {
            this.x = x;
            this.y = y;
            this.color = color;
        }
    }

    // class Grids extends Canvas {
    //     int width, height, rows, columns;
    //
    //     Grids(int w, int h, int r, int c) {
    //         setSize(width = w, height = h);
    //         rows = r;
    //         columns = c;
    //     }
    //     public void paint(Graphics g) {
    //         int k;
    //         width = getSize().width;
    //         height = getSize().height;
    //
    //         int htOfRow = height / (rows);
    //         for (k = 0; k < rows; k++) {
    //             g.drawLine(0, k * htOfRow , width, k * htOfRow);
    //         }
    //
    //         int wdOfRow = width / (columns);
    //         for (k = 0; k < columns; k++) {
    //             g.drawLine(k*wdOfRow , 0, k*wdOfRow , height);
    //         }
    //     }
    // }
}
