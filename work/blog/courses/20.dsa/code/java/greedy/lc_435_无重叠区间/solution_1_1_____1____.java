// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244140
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc435_solution111 { // 定义类型
  static int eraseOverlapIntervals(int[][] intervals) { // 定义函数/方法 eraseOverlapIntervals
    if (intervals == null || intervals.length == 0)
      return 0; // 若 intervals 等于 null 或 intervals.长度 等于 0，直接返回 0
    Arrays.sort(intervals, (a, b) -> a[1] - b[1]); // 排序
    int n = intervals.length; // 把 intervals.长度 存入 元素个数
    int right = intervals[0][1]; // 把 intervals[0][1] 存入 右边界
    int ans = 1; // 把 1 存入 答案
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
      if (intervals[i][0] >= right) { // 若 intervals[下标 i][0] 不低于 右边界
        ++ans; // 加一 答案;
        right = intervals[i][1]; // 把 intervals[下标 i][1]; 写入 右边界
      }
    }
    return n - ans; // 返回 元素个数 减 答案
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
