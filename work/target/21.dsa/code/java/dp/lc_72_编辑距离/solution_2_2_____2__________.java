// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848060
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static int minDistance(String w1, String w2) { // 定义函数/方法 minDistance
    int m = w1.length(), n = w2.length(); // 把 w1.长度(), 元素个数 赋值为 w2.长度() 存入 映射表
    int[][] dp = new int[m + 1][n + 1]; // 把 new int[映射表 加 1][元素个数 加 1]; 写入 int[][] dp
    for (int i = 0; i <= m; i++) dp[i][0] = i; // 让 下标 i 从 0 开始计数，下标 i 不超过 映射表 就继续
    for (int j = 0; j <= n; j++) dp[0][j] = j; // 让 下标 j 从 0 开始计数，下标 j 不超过 元素个数 就继续
    for (int i = 1; i <= m; i++) // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
        int cost =
            w1.charAt(i - 1) == w2.charAt(j - 1)
                ? 0
                : 1; // 把 w1 取字符 下标 i 减 1) 等于 w2 取字符 下标 j 减 1) ? 0 : 1 存入 cost
        dp[i][j] = Math.min(dp[i - 1][j] + 1, Math.min(dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost));
      }
    return dp[m][n]; // 返回 DP 表[映射表][元素个数]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[] a = {"horse", "intention", ""};
    String[] b = {"ros", "execution", ""};
    int[] ws = {3, 5, 0};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      int got = minDistance(a[i], b[i]); // 把 minDistance(数组[下标 i], b[下标 i]) 存入 got
      if (got != ws[i]) {
        ok = false;
        System.out.println("FAIL " + got + " want " + ws[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
