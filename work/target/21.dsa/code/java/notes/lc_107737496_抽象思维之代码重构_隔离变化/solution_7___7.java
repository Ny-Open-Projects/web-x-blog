// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_7：用 dict 模拟 switch 分派确定下一位置后螺旋填充
class Main { // 定义类型

  static int[] place(int row, int col, char direction, int n, int[][] m) { // 定义函数/方法 place
    if (direction == 'D') { // 若 direction 等于 'D'
      if (row + 1 < n && m[row + 1][col] == 0) { // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0
        return new int[] {row + 1, col}; // 返回 new int[] {row 加 1, col}
      }
      return new int[] {row, col + 1, (int) 'R'}; // 返回 new int[] {row, col 加 1, (int) 'R'}
    } else if (direction == 'R') { // 否则，若 direction 等于 'R'
      if (col + 1 < n && m[row][col + 1] == 0) { // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0
        return new int[] {row, col + 1}; // 返回 new int[] {row, col 加 1}
      }
      return new int[] {row - 1, col, (int) 'U'}; // 返回 new int[] {row 减 1, col, (int) 'U'}
    } else if (direction == 'U') { // 否则，若 direction 等于 'U'
      if (row - 1 >= 0 && m[row - 1][col] == 0) { // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0
        return new int[] {row - 1, col}; // 返回 new int[] {row 减 1, col}
      }
      return new int[] {row, col - 1, (int) 'L'}; // 返回 new int[] {row, col 减 1, (int) 'L'}
    } else { // 否则
      if (col - 1 >= 0 && m[row][col - 1] == 0) { // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0
        return new int[] {row, col - 1}; // 返回 new int[] {row, col 减 1}
      }
      return new int[] {row + 1, col, (int) 'D'}; // 返回 new int[] {row 加 1, col, (int) 'D'}
    }
  }

  static int[][] fillSpiral(int n) { // 定义函数/方法 fillSpiral
    int[][] m = new int[n][n]; // 把 new int[元素个数][元素个数]; 写入 int[][] m
    int row = 0; // 把 0 存入 row
    int col = 0; // 把 0 存入 col
    char direction = 'D'; // 把 'D'; 写入 char direction
    int num = 1; // 把 1 存入 num
    while (num <= n * n) { // 循环，直到不满足「num 不超过 元素个数 乘 元素个数」
      m[row][col] = num; // 把 num; 写入 m[row][col]
      num++; // num 加一
      int[] res =
          place(row, col, direction, n, m); // 把 place(row, col, direction, 元素个数, 映射表); 写入 int[] res
      row = res[0]; // 把 结果[0]; 写入 row
      col = res[1]; // 把 结果[1]; 写入 col
      if (res.length == 3) { // 若 结果.长度 等于 3
        direction = (char) res[2]; // 把 (char) 结果[2]; 写入 direction
      }
    }
    return m; // 返回 映射表
  }

  static boolean eq2(int[][] a, int[][] b) { // 定义函数/方法 eq2
    if (a.length != b.length) { // 若 数组.长度 不等于 b.长度
      return false; // 返回 false
    }
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i].length != b[i].length) { // 若 数组[下标 i].长度 不等于 b[下标 i].长度
        return false; // 返回 false
      }
      for (int j = 0; j < a[i].length; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
        if (a[i][j] != b[i][j]) { // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]
          return false; // 返回 false
        }
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] sizes = {3, 4, 5}; // 把 {3, 4, 5}; 写入 int[] sizes
    int[][][] want = new int[sizes.length][][]; // 把 new int[sizes.长度][][]; 写入 int[][][] want
    want[0] =
        new int[][] {
          {1, 8, 7}, {2, 9, 6}, {3, 4, 5}
        }; // 把 new int[][] {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; 写入 want[0]
    want[1] = new int[][] {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    want[2] =
        new int[][] {
          {1, 16, 15, 14, 13},
          {2, 17, 24, 23, 12},
          {3, 18, 25, 22, 11},
          {4, 19, 20, 21, 10},
          {5, 6, 7, 8, 9}
        }; // {4, 19, 20, 21, 10}, {5, 6, 7, 8, 9}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < sizes.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 sizes.长度 就继续
      int[][] got = fillSpiral(sizes[k]); // 把 fillSpiral(sizes[下标 k]); 写入 int[][] got
      if (!eq2(got, want[k])) { // 若 取反 eq2(got, want[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL fill_spiral(" + sizes[k] + ")=" + Arrays.deepToString(got)); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
