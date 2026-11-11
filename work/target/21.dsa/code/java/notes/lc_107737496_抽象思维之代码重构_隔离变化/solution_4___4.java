// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_4：依据前一位置、方向（DRUL 逆时针）与边界规则确定下一个位置
class Main { // 定义类型

  static int[][] placeFill(int n) { // 定义函数/方法 placeFill
    int[][] m = new int[n][n]; // 把 new int[元素个数][元素个数]; 写入 int[][] m
    int row = 0; // 把 0 存入 row
    int col = 0; // 把 0 存入 col
    char direction = 'D'; // 把 'D'; 写入 char direction
    int num = 1; // 把 1 存入 num
    int total = n * n; // 把 元素个数 乘 元素个数 存入 总和
    while (num <= total) { // 循环，直到不满足「num 不超过 总和」
      m[row][col] = num; // 把 num; 写入 m[row][col]
      num++; // num 加一
      if (direction == 'D') { // 若 direction 等于 'D'
        if (row + 1 < n && m[row + 1][col] == 0) { // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0
          row++; // row 加一
        } else { // 否则
          direction = 'R'; // 把 'R'; 写入 direction
          col++; // col 加一
        }
      } else if (direction == 'R') { // 否则，若 direction 等于 'R'
        if (col + 1 < n && m[row][col + 1] == 0) { // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0
          col++; // col 加一
        } else { // 否则
          direction = 'U'; // 把 'U'; 写入 direction
          row--; // row 减一
        }
      } else if (direction == 'U') { // 否则，若 direction 等于 'U'
        if (row - 1 >= 0 && m[row - 1][col] == 0) { // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0
          row--; // row 减一
        } else { // 否则
          direction = 'L'; // 把 'L'; 写入 direction
          col--; // col 减一
        }
      } else { // 否则
        if (col - 1 >= 0 && m[row][col - 1] == 0) { // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0
          col--; // col 减一
        } else { // 否则
          direction = 'D'; // 把 'D'; 写入 direction
          row++; // row 加一
        }
      }
    }
    return m; // 返回 映射表
  }

  static String show(int[][] m) { // 定义函数/方法 show
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    for (int[] row : m) { // for (int[] row : 映射表) {
      sb.append(Arrays.toString(row)); // 把 Arrays.toString(row 追加到列表尾部
    }
    return sb.toString(); // 返回 sb.toString()
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
    int[] sizes = {3, 4, 6}; // 把 {3, 4, 6}; 写入 int[] sizes
    int[][][] want = new int[sizes.length][][]; // 把 new int[sizes.长度][][]; 写入 int[][][] want
    want[0] =
        new int[][] {
          {1, 8, 7}, {2, 9, 6}, {3, 4, 5}
        }; // 把 new int[][] {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; 写入 want[0]
    want[1] = new int[][] {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    want[2] =
        new int[][] {
          {1, 20, 19, 18, 17, 16},
          {2, 21, 32, 31, 30, 15},
          {3, 22, 33, 36, 29, 14},
          {4, 23, 34, 35, 28, 13},
          {5, 24, 25, 26, 27, 12},
          {6, 7, 8, 9, 10, 11}
        };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < sizes.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 sizes.长度 就继续
      int[][] got = placeFill(sizes[k]); // 把 placeFill(sizes[下标 k]); 写入 int[][] got
      if (!eq2(got, want[k])) { // 若 取反 eq2(got, want[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL place_fill(" + sizes[k] + ")=" + show(got) + " want " + show(want[k])); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
