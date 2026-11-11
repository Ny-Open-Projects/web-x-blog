// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244140
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc435_solution222 { // 定义类型
  static int eraseOverlapIntervals(int[][] intervals) { // 定义函数/方法 eraseOverlapIntervals
    if (intervals == null || intervals.length == 0)
      return 0; // 若 intervals 等于 null 或 intervals.长度 等于 0，直接返回 0
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]); // 排序
    int n = intervals.length; // 把 intervals.长度 存入 元素个数
    int[] f = new int[n]; // 把 new int[元素个数]; 写入 int[] f
    Arrays.fill(f, 1); // Arrays.fill(f, 1);
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
      for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        if (intervals[j][1] <= intervals[i][0]) { // 若 intervals[下标 j][1] 不超过 intervals[下标 i][0]
          f[i] = Math.max(f[i], f[j] + 1); // 把 Math.取较大值 f[下标 i], f[下标 j] 加 1); 写入 f[i]
        }
      }
    }
    int maxF = 0; // 把 0 存入 maxF
    for (int v : f) maxF = Math.max(maxF, v); // 把 Math.取较大值 maxF, 值); 写入 for (int v : f) maxF
    return n - maxF; // 返回 元素个数 减 maxF
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int gotNull = eraseOverlapIntervals(null); // 把 eraseOverlapIntervals(null) 存入 gotNull
    if (gotNull != 0) throw new RuntimeException("FAILED null: got " + gotNull);
    int[][] intervals = {
      {1, 2}, {2, 3}, {3, 4}, {1, 3}
    }; // 把 {{1, 2}, {2, 3}, {3, 4}, {1, 3}}; 写入 int[][] intervals
    int got = eraseOverlapIntervals(intervals); // 把 eraseOverlapIntervals(intervals) 存入 got
    if (got != 1) throw new RuntimeException("FAILED: got " + got + " want 1");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
