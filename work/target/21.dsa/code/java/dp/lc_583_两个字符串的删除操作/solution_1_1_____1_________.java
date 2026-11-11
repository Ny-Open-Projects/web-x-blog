// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853278
package com.webfault.dsa; // 引入依赖

class Lc583 { // 定义类型
  int minDistance(String word1, String word2) { // 定义函数/方法 minDistance
    int m = word1.length(), n = word2.length(); // 把 word1.长度(), 元素个数 赋值为 word2.长度() 存入 映射表
    int[][] dp = new int[m + 1][n + 1]; // 把 new int[映射表 加 1][元素个数 加 1]; 写入 int[][] dp
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      char c1 = word1.charAt(i - 1); // 逐字符处理
      for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
        char c2 = word2.charAt(j - 1); // 逐字符处理
        if (c1 == c2) dp[i][j] = dp[i - 1][j - 1] + 1;
        else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); // 否则
      }
    }
    int lcs = dp[m][n]; // 把 DP 表[映射表][元素个数] 存入 lcs
    return m - lcs + n - lcs; // 返回 映射表 减 lcs 加 元素个数 减 lcs
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc583 s = new Lc583(); // 把 new Lc583(); 写入 Lc583 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.minDistance("sea", "eat") != 2) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.minDistance("", "") != 0) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
