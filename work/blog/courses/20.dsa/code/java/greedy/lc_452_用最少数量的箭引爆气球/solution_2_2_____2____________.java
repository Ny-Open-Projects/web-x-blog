// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244333
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc452_solution222 { // 定义类型
  static int findMinArrowShots(int[][] points) { // 定义函数/方法 findMinArrowShots
    if (points == null || points.length == 0) return 0; // 若 points 等于 null 或 points.长度 等于 0，直接返回 0
    Arrays.sort(points, (a, b) -> a[1] - b[1]); // 排序
    int arrows = 1; // 把 1 存入 arrows
    int end = points[0][1]; // 把 points[0][1] 存入 终点
    for (int i = 1; i < points.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 points.长度 就继续
      if (points[i][0] > end) { // 若 points[下标 i][0] 超过 终点
        arrows++; // arrows 加一
        end = points[i][1]; // 把 points[下标 i][1]; 写入 终点
      }
    }
    return arrows; // 返回 arrows
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int gotNull = findMinArrowShots(null); // 把 findMinArrowShots(null) 存入 gotNull
    if (gotNull != 0) throw new RuntimeException("FAILED null: got " + gotNull);
    int[][] points = {
      {1, 2}, {2, 3}, {3, 4}, {4, 5}
    }; // 把 {{1, 2}, {2, 3}, {3, 4}, {4, 5}}; 写入 int[][] points
    int got = findMinArrowShots(points); // 把 findMinArrowShots(points) 存入 got
    if (got != 2) throw new RuntimeException("FAILED: got " + got + " want 2");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
