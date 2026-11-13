// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849793
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc123_solution111 { // 定义类型
  public int maxProfit(int[] prices) { // 定义函数/方法 maxProfit
    int len = prices.length; // 把 价格序列.长度 存入 长度
    int[] dp = new int[5]; // 把 new int[5]; 写入 int[] dp
    dp[1] = -prices[0]; // 把 减 价格序列[0]; 写入 dp[1]
    dp[3] = -prices[0]; // 把 减 价格序列[0]; 写入 dp[3]
    for (int i = 1; i < len; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 长度 就继续
      dp[1] =
          Math.max(
              dp[1], dp[0] - prices[i]); // 把 Math.取较大值 DP 表[1], DP 表[0] 减 价格序列[下标 i]); 写入 dp[1]
      dp[2] =
          Math.max(
              dp[2], dp[1] + prices[i]); // 把 Math.取较大值 DP 表[2], DP 表[1] 加 价格序列[下标 i]); 写入 dp[2]
      dp[3] =
          Math.max(
              dp[3], dp[2] - prices[i]); // 把 Math.取较大值 DP 表[3], DP 表[2] 减 价格序列[下标 i]); 写入 dp[3]
      dp[4] =
          Math.max(
              dp[4], dp[3] + prices[i]); // 把 Math.取较大值 DP 表[4], DP 表[3] 加 价格序列[下标 i]); 写入 dp[4]
    }
    return dp[4]; // 返回 DP 表[4]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc123_solution111 s =
        new lc123_solution111(); // 把 new lc123_solution111(); 写入 lc123_solution111 s
    int got = s.maxProfit(new int[] {1, 2, 3}); // 把 字符串.maxProfit(new int[]{1, 2, 3}) 存入 got
    if (got != 2) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
