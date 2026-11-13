// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355902
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc877_solution111 { // 定义类型
  public boolean stoneGame(int[] piles) { // 定义函数/方法 stoneGame
    int n = piles.length; // 把 piles.长度 存入 元素个数
    int[][] dp = new int[n][n]; // 把 new int[元素个数][元素个数]; 写入 int[][] dp
    for (int i = 0; i < n; i++) dp[i][i] = piles[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int length = 2; length <= n; length++) { // 让 长度 从 2 开始计数，长度 不超过 元素个数 就继续
      for (int i = 0; i + length - 1 < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 加 长度 减 1 小于 元素个数 就继续
        int j = i + length - 1; // 把 下标 i 加 长度 减 1 存入 下标 j
        dp[i][j] = Math.max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
      }
    }
    return dp[0][n - 1] > 0; // 返回 DP 表[0][元素个数 减 1] 超过 0
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc877_solution111 s =
        new lc877_solution111(); // 把 new lc877_solution111(); 写入 lc877_solution111 s
    boolean got =
        s.stoneGame(
            new int[] {5, 3, 4, 5}); // 把 字符串.stoneGame(new int[]{5, 3, 4, 5}); 写入 boolean got
    if (got != true) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
