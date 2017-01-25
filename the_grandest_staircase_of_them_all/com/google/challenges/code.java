package com.google.challenges;

public class Answer {

    public static final float EPSILON = 0.0000001;

    public static int answer(int n) {

        // Your code goes here.

    }

    public static int pentagonalNumber(n) {
        return Math.round(n * (3 * n - 1) / 2f);
    }

    public static int calcM(k) {
        float m = (1 + Math.sqrt(1 + 12 * k)) / 6;
        if (!Float.isNaN(m) && Math.abs(Math.round(m) - m) < EPSILON) {
            return m;
        }
        m = (1 - Math.sqrt(1 + 12 * k)) / 6;
        if (!Float.isNaN(m) && Math.abs(Math.round(m) - m) < EPSILON) {
            return m;
        }
        return NaN;
    }

    public static
}
