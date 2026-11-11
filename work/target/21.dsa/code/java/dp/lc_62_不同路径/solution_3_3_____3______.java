// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc62_solution333 { // 定义类型
  // 不同路径：二维动态规划
  // 忠实于 Python 参考实现 ref_uniquePaths 的 DP 思想
  public int uniquePaths(int m, int n) { // 定义函数/方法 uniquePaths
    int[][] f = new int[m][n]; // 把 new int[映射表][元素个数]; 写入 int[][] f
    for (int i = 0; i < m; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      f[i][0] = 1; // 把 1; 写入 f[i][0]
    }
    for (int j = 0; j < n; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
      f[0][j] = 1; // 把 1; 写入 f[0][j]
    }
    for (int i = 1; i < m; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
      for (int j = 1; j < n; j++) { // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
        f[i][j] = f[i - 1][j] + f[i][j - 1]; // 把 f[下标 i 减 1][下标 j] 加 f[下标 i][下标 j 减 1]; 写入 f[i][j]
      }
    }
    return f[m - 1][n - 1]; // 返回 f[映射表 减 1][元素个数 减 1]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc62_solution333 s = new lc62_solution333(); // 把 new lc62_solution333(); 写入 lc62_solution333 s
    int[][] cases = {
      {3, 7, 28}, {3, 2, 3}, {1, 1, 1}
    }; // 把 {{3, 7, 28}, {3, 2, 3}, {1, 1, 1}}; 写入 int[][] cases
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      int got = s.uniquePaths(c[0], c[1]); // 把 字符串.uniquePaths(字符[0], 字符[1]) 存入 got
      if (got != c[2]) { // 若 got 不等于 字符[2]
        System.out.println(
            "FAIL: uniquePaths(" + c[0] + "," + c[1] + ")=" + got + " want " + c[2]); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
