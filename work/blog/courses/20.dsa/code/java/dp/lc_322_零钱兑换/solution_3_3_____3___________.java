// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144851123
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型
  static int coinChange(int[] coins, int amount) { // 定义函数/方法 coinChange
    if (amount < 0) return -1; // 若 目标金额 小于 0，直接返回 减 1
    int[] dp = new int[amount + 1]; // 把 new int[目标金额 加 1]; 写入 int[] dp
    for (int i = 0; i <= amount; i++) dp[i] = amount + 1; // 让 下标 i 从 0 开始计数，下标 i 不超过 目标金额 就继续
    dp[0] = 0; // 把 0; 写入 dp[0]
    for (int a = 1; a <= amount; a++) { // 让 数组 从 1 开始计数，数组 不超过 目标金额 就继续
      for (int c : coins) { // for (int 字符 : 硬币面额) {
        if (c <= a && dp[a - c] + 1 < dp[a]) dp[a] = dp[a - c] + 1;
      }
    }
    return dp[amount] > amount ? -1 : dp[amount]; // 返回 DP 表[目标金额] 超过 目标金额 ? 减 1 : DP 表[目标金额]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] coins = {{1, 2, 5}, {2}, {1}}; // 把 {{1,2,5}, {2}, {1}}; 写入 int[][] coins
    int[] amounts = {11, 3, 0}; // 把 {11, 3, 0}; 写入 int[] amounts
    int[] wants = {3, -1, 0}; // 把 {3, 减 1, 0}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < coins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 硬币面额.长度 就继续
      int got = coinChange(coins[i], amounts[i]); // 把 coinChange(硬币面额[下标 i], amounts[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        System.out.println(
            "FAIL coins="
                + Arrays.toString(coins[i])
                + " amount="
                + amounts[i]
                + " want="
                + wants[i]
                + " got="
                + got); // 打印输出
        ok = false; // 把 false; 写入 ok
      }
    }
    if (!ok) {
      System.out.println("RESULT: FAIL");
      System.exit(1);
    } // 若 取反 ok) { System.out.输出(「RESULT: FAIL」); System.exit(1); }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
