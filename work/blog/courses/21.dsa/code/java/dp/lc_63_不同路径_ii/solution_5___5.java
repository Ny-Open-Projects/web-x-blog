// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130713079
package com.webfault.dsa; // 引入依赖

/** 忠实翻译 python/dp/lc_63_不同路径_ii/solution_5___5.py 方案5：二维 dp。 */
class Lc63S5 { // 定义类型
  static int uniquePathsWithObstacles(int[][] obstacleGrid) { // 定义函数/方法 uniquePathsWithObstacles
    int m = obstacleGrid.length; // 把 obstacleGrid.长度 存入 映射表
    int n = obstacleGrid[0].length; // 把 obstacleGrid[0].长度 存入 元素个数
    int[][] dp = new int[m][n]; // 把 new int[映射表][元素个数]; 写入 int[][] dp
    for (int i = 0; i < m; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      if (obstacleGrid[i][0] == 0) { // 若 obstacleGrid[下标 i][0] 等于 0
        dp[i][0] = 1; // 把 1; 写入 dp[i][0]
      } else { // 否则
        break; // 跳出循环
      }
    }
    for (int j = 0; j < n; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
      if (obstacleGrid[0][j] == 0) { // 若 obstacleGrid[0][下标 j] 等于 0
        dp[0][j] = 1; // 把 1; 写入 dp[0][j]
      } else { // 否则
        break; // 跳出循环
      }
    }
    for (int i = 1; i < m; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
      for (int j = 1; j < n; j++) { // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
        if (obstacleGrid[i][j] == 1) { // 若 obstacleGrid[下标 i][下标 j] 等于 1
          continue; // 跳过本轮，进入下一次
        }
        dp[i][j] =
            dp[i - 1][j]
                + dp[i][j - 1]; // 把 DP 表[下标 i 减 1][下标 j] 加 DP 表[下标 i][下标 j 减 1]; 写入 dp[i][j]
      }
    }
    return dp[m - 1][n - 1]; // 返回 DP 表[映射表 减 1][元素个数 减 1]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] g1 = {
      {0, 0, 0}, {0, 1, 0}, {0, 0, 0}
    }; // 把 { {0, 0, 0}, {0, 1, 0}, {0, 0, 0} }; 写入 int[][] g1
    int[][] g2 = {{0, 0}, {1, 0}}; // 把 { {0, 0}, {1, 0} }; 写入 int[][] g2
    int[][] g3 = {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}};
    int r1 = uniquePathsWithObstacles(g1); // 把 uniquePathsWithObstacles(g1) 存入 r1
    int r2 = uniquePathsWithObstacles(g2); // 把 uniquePathsWithObstacles(g2) 存入 r2
    int r3 = uniquePathsWithObstacles(g3); // 把 uniquePathsWithObstacles(g3) 存入 r3
    if (!(r1 == 2 && r2 == 1 && r3 == 2)) { // 若 取反 (r1 等于 2 且 r2 等于 1 且 r3 等于 2
      System.out.println("FAIL got " + r1 + " " + r2 + " " + r3 + " want 2 1 2"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
