// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829625
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1143_solution111 { // 定义类型
  public int longestCommonSubsequence(
      String text1, String text2) { // 定义函数/方法 longestCommonSubsequence
    int m = text1.length(), n = text2.length(); // 把 text1.长度(), 元素个数 赋值为 text2.长度() 存入 映射表
    int[][] dp = new int[m + 1][n + 1]; // 把 new int[映射表 加 1][元素个数 加 1]; 写入 int[][] dp
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      char c1 = text1.charAt(i - 1); // 逐字符处理
      for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
        char c2 = text2.charAt(j - 1); // 逐字符处理
        if (c1 == c2) { // 若 c1 等于 c2
          dp[i][j] = dp[i - 1][j - 1] + 1; // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1; 写入 dp[i][j]
        } else { // 否则
          dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
      }
    }
    return dp[m][n]; // 返回 DP 表[映射表][元素个数]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc1143_solution111 s =
        new lc1143_solution111(); // 把 new lc1143_solution111(); 写入 lc1143_solution111 s
    int got =
        s.longestCommonSubsequence(
            "abcde", "ace"); // 把 字符串.longestCommonSubsequence(「abcde」, 「abcde」) 存入 got
    if (got != 3) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
