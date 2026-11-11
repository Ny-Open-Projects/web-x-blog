package com.webfault.dsa;

import java.util.*;

class lc502_solution1 {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) indices[i] = i;
        Arrays.sort(indices, (a, b) -> capital[a] - capital[b]);
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        int i = 0;
        for (int t = 0; t < k; t++) {
            while (i < n && capital[indices[i]] <= w) {
                maxHeap.offer(profits[indices[i]]);
                i++;
            }
            if (maxHeap.isEmpty()) break;
            w += maxHeap.poll();
        }
        return w;
    }

    public static void main(String[] args) {
        lc502_solution1 s = new lc502_solution1();
        int[][] cases = {
            {2, 0, 4},   // k, w, want  (profits/capital follow)
        };
        // cases: (k, w, profits[], capital[], want)
        Object[] t1 = new Object[]{2, 0, new int[]{1, 2, 3}, new int[]{0, 1, 1}, 4};
        Object[] t2 = new Object[]{1, 0, new int[]{1, 2, 3}, new int[]{1, 2, 3}, 0};
        Object[] t3 = new Object[]{3, 0, new int[]{1, 2, 3}, new int[]{0, 1, 1}, 6};
        Object[][] tests = {t1, t2, t3};
        boolean ok = true;
        for (Object[] t : tests) {
            int k = (int) t[0];
            int w = (int) t[1];
            int[] profits = (int[]) t[2];
            int[] capital = (int[]) t[3];
            int want = (int) t[4];
            int got = s.findMaximizedCapital(k, w, profits, capital);
            if (got != want) {
                ok = false;
                System.out.println("FAIL findMaximizedCapital(" + k + "," + w + ")=" + got + " want " + want);
            }
        }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
