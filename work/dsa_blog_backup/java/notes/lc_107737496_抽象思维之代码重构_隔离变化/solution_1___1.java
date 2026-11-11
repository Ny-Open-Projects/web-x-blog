// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_1：递归式逆时针螺旋填充
class Main { // 定义类型

  static void fill(int[][] matrix, int[] num, int begin, int size) { // 定义函数/方法 fill
    if (size == 0) { // 若 大小 等于 0
      return; // return;
    }
    if (size == 1) { // 若 大小 等于 1
      matrix[begin][begin] = num[0]; // 把 num[0]; 写入 matrix[begin][begin]
      num[0]++; // num[0] 加一 ;
      return; // return;
    }
    for (int j = 0; j < size - 1; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
      matrix[begin + j][begin] = num[0]++; // 把 num[0] 加一 ; 写入 matrix[begin + j][begin]
    }
    for (int j = 0; j < size - 1; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
      matrix[begin + size - 1][begin + j] =
          num[0]++; // 把 num[0] 加一 ; 写入 matrix[begin + size - 1][begin + j]
    }
    for (int j = size - 1; j > 0; j--) { // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
      matrix[begin + j][begin + size - 1] =
          num[0]++; // 把 num[0] 加一 ; 写入 matrix[begin + j][begin + size - 1]
    }
    for (int j = size - 1; j > 0; j--) { // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
      matrix[begin][begin + j] = num[0]++; // 把 num[0] 加一 ; 写入 matrix[begin][begin + j]
    }
    fill(matrix, num, begin + 1, size - 2); // fill(矩阵, num, begin 加 1, 大小 减 2);
  }

  static int[][] generateSquareMatrix(int n) { // 定义函数/方法 generateSquareMatrix
    int[][] m = new int[n][n]; // 把 new int[元素个数][元素个数]; 写入 int[][] m
    fill(m, new int[] {1}, 0, n); // fill(映射表, new int[] {1}, 0, 元素个数);
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
    int[] sizes = {1, 2, 3, 4}; // 把 {1, 2, 3, 4}; 写入 int[] sizes
    int[][][] want = new int[sizes.length][][]; // 把 new int[sizes.长度][][]; 写入 int[][][] want
    want[0] = new int[][] {{1}}; // 把 new int[][] {{1}}; 写入 want[0]
    want[1] = new int[][] {{1, 4}, {2, 3}}; // 把 new int[][] {{1, 4}, {2, 3}}; 写入 want[1]
    want[2] =
        new int[][] {
          {1, 8, 7}, {2, 9, 6}, {3, 4, 5}
        }; // 把 new int[][] {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; 写入 want[2]
    want[3] = new int[][] {{1, 12, 11, 10}, {2, 13, 16, 9}, {3, 14, 15, 8}, {4, 5, 6, 7}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < sizes.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 sizes.长度 就继续
      int[][] got =
          generateSquareMatrix(sizes[k]); // 把 generateSquareMatrix(sizes[下标 k]); 写入 int[][] got
      if (!eq2(got, want[k])) { // 若 取反 eq2(got, want[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL generate_square_matrix("
                + sizes[k]
                + ")="
                + show(got)
                + " want "
                + show(want[k])); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
