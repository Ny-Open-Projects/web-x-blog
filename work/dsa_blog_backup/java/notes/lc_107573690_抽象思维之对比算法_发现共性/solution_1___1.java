// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static int climbStairsRefactored(int h) { // 定义函数/方法 climbStairsRefactored
    int[] count = {0}; // 把 {0}; 写入 int[] count
    dfs(0, h, count); // dfs(0, h, 计数);
    return count[0]; // 返回 计数[0]
  }

  static void dfs(int pos, int goal, int[] count) { // 定义函数/方法 dfs
    if (pos == goal) {
      count[0]++;
      return;
    } // 若 pos 等于 goal) { 计数[0] 加一 ; return; }
    for (int k = 0; k < 3; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 3 就继续
      int nxt = pos + (k + 1); // 把 pos 加 (下标 k 加 1) 存入 nxt
      if (!(0 <= nxt && nxt <= goal)) continue; // 若 取反 (0 不超过 nxt 且 nxt 不超过 goal)) continue;
      dfs(nxt, goal, count); // dfs(nxt, goal, 计数);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int got = climbStairsRefactored(10); // 把 climbStairsRefactored(10) 存入 got
    if (got != 274) {
      System.out.println("FAIL got " + got + " want 274");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
