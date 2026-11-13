// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc518_solution222 { // 定义类型
  public int change(int amount, int[] coins) { // 定义函数/方法 change
    int[] dp = new int[amount + 1]; // 把 new int[目标金额 加 1]; 写入 int[] dp
    int[] valid = new int[amount + 1]; // 把 new int[目标金额 加 1]; 写入 int[] valid
    dp[0] = 1; // 把 1; 写入 dp[0]
    valid[0] = 1; // 把 1; 写入 valid[0]
    for (int coin : coins) { // for (int coin : 硬币面额) {
      for (int i = coin; i <= amount; i++) { // 让 下标 i 从 coin 开始计数，下标 i 不超过 目标金额 就继续
        valid[i] |= valid[i - coin]; // 把 valid[下标 i 减 coin]; 写入 valid[i] |
      }
    }
    if (valid[amount] == 0) { // 若 valid[目标金额] 等于 0
      return 0; // 返回 0
    }
    for (int coin : coins) { // for (int coin : 硬币面额) {
      for (int i = coin; i <= amount; i++) { // 让 下标 i 从 coin 开始计数，下标 i 不超过 目标金额 就继续
        dp[i] += dp[i - coin]; // dp[i]累加 DP 表[下标 i 减 coin]
      }
    }
    return dp[amount]; // 返回 DP 表[目标金额]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc518_solution222 s =
        new lc518_solution222(); // 把 new lc518_solution222(); 写入 lc518_solution222 s
    int got = s.change(5, new int[] {1, 2, 5}); // 把 字符串.change(5, new int[]{1, 2, 5}) 存入 got
    if (got != 4) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
