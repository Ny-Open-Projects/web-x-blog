// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
package com.webfault.dsa; // 引入依赖

class lc518_solution111 { // 定义类型
  static int change(int amount, int[] coins) { // 定义函数/方法 change
    int[] dp = new int[amount + 1]; // 把 new int[目标金额 加 1]; 写入 int[] dp
    dp[0] = 1; // 把 1; 写入 dp[0]
    for (int coin : coins) // for (int coin : 硬币面额)
    for (int a = coin; a <= amount; a++) dp[a] += dp[a - coin]; // 让 数组 从 coin 开始计数，数组 不超过 目标金额 就继续
    return dp[amount]; // 返回 DP 表[目标金额]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int got = change(5, new int[] {1, 2, 5}); // 把 change(5, new int[]{1, 2, 5}) 存入 got
    if (got != 4) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
