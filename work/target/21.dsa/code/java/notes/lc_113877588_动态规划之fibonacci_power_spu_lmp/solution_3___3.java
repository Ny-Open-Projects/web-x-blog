// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
package com.webfault.dsa; // 引入依赖

class lc113877588_solution33 { // 定义类型
  // 最长曼哈顿路径（只能向右/向下，求权重和最大）
  static int longestManhattanPath(int[][] grid) { // 定义函数/方法 longestManhattanPath
    if (grid == null || grid.length == 0 || grid[0].length == 0)
      return 0; // 若 网格 等于 null 或 网格.长度 等于 0 或 网格[0].长度 等于 0，直接返回 0
    int m = grid.length, n = grid[0].length; // 把 网格.长度, 元素个数 赋值为 网格[0].长度 存入 映射表
    int[][] dp = new int[m][n]; // 把 new int[映射表][元素个数]; 写入 int[][] dp
    dp[0][0] = grid[0][0]; // 把 网格[0][0]; 写入 dp[0][0]
    for (int i = 0; i < m; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      for (int j = 0; j < n; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
        if (i == 0 && j == 0) continue; // 若 下标 i 等于 0 且 下标 j 等于 0) continue;
        int up = (i > 0) ? dp[i - 1][j] : Integer.MIN_VALUE;
        int left = (j > 0) ? dp[i][j - 1] : Integer.MIN_VALUE;
        dp[i][j] =
            grid[i][j] + Math.max(up, left); // 把 网格[下标 i][下标 j] 加 Math.取较大值 up, 左边界); 写入 dp[i][j]
      }
    }
    return dp[m - 1][n - 1]; // 返回 DP 表[映射表 减 1][元素个数 减 1]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] grid = {
      {5, 1, 3}, {2, 4, 2}, {3, 2, 1}
    }; // 把 {{5, 1, 3}, {2, 4, 2}, {3, 2, 1}}; 写入 int[][] grid
    if (longestManhattanPath(grid) != 14) { // 若 longestManhattanPath(网格) 不等于 14
      System.out.println("FAIL"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
