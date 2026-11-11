// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package com.webfault.dsa; // 引入依赖

class lc62_solution444 { // 定义类型
  // 不同路径：一维动态规划（忠实翻译 Python ref_uniquePaths）
  // dp = [1]*n; for _ in range(1, m): for j in range(1, n): dp[j] += dp[j-1]
  static int uniquePaths(int m, int n) { // 定义函数/方法 uniquePaths
    int[] f = new int[n]; // 把 new int[元素个数]; 写入 int[] f
    for (int i = 0; i < n; i++) f[i] = 1; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 1; i < m; i++) // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
    for (int j = 1; j < n; j++) f[j] += f[j - 1]; // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
    return f[n - 1]; // 返回 f[元素个数 减 1]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = {
      {3, 7, 28}, {3, 2, 3}, {1, 1, 1}
    }; // 把 {{3, 7, 28}, {3, 2, 3}, {1, 1, 1}}; 写入 int[][] cases
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      int got = uniquePaths(c[0], c[1]); // 把 uniquePaths(字符[0], 字符[1]) 存入 got
      if (got != c[2]) { // 若 got 不等于 字符[2]
        System.out.println(
            "FAIL: uniquePaths(" + c[0] + "," + c[1] + ")=" + got + " want " + c[2]); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
