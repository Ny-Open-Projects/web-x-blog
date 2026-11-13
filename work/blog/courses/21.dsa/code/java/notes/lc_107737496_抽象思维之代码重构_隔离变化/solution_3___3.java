// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// 忠实翻译 python solution_3：面向对象 Matrix 类，封装填充与清空
class Main { // 定义类型

  static class Matrix { // static class Matrix {
    final int N; // final int N;
    int[][] M; // int[][] M;

    Matrix(int size) { // Matrix(int 大小) {
      this.N = size; // 把 大小; 写入 this.N
      this.M = new int[size][size]; // 把 new int[大小][大小]; 写入 this.M
    }

    void fill(int num, int begin, int size) { // 定义函数/方法 fill
      if (size == 0) { // 若 大小 等于 0
        return; // return;
      }
      if (size == 1) { // 若 大小 等于 1
        M[begin][begin] = num; // 把 num; 写入 M[begin][begin]
        return; // return;
      }
      for (int j = 0; j < size - 1; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
        M[begin + j][begin] = num++; // 把 num 加一 ; 写入 M[begin + j][begin]
      }
      for (int j = 0; j < size - 1; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
        M[begin + size - 1][begin + j] = num++; // 把 num 加一 ; 写入 M[begin + size - 1][begin + j]
      }
      for (int j = size - 1; j > 0; j--) { // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
        M[begin + j][begin + size - 1] = num++; // 把 num 加一 ; 写入 M[begin + j][begin + size - 1]
      }
      for (int j = size - 1; j > 0; j--) { // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
        M[begin][begin + j] = num++; // 把 num 加一 ; 写入 M[begin][begin + j]
      }
      fill(num, begin + 1, size - 2); // fill(num, begin 加 1, 大小 减 2);
    }

    void clear() { // 定义函数/方法 clear
      M = new int[N][N]; // 把 new int[N][N]; 写入 M
    }
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
    int[] sizes = {1, 2, 3}; // 把 {1, 2, 3}; 写入 int[] sizes
    int[][][] want = new int[sizes.length][][]; // 把 new int[sizes.长度][][]; 写入 int[][][] want
    want[0] = new int[][] {{1}}; // 把 new int[][] {{1}}; 写入 want[0]
    want[1] = new int[][] {{1, 4}, {2, 3}}; // 把 new int[][] {{1, 4}, {2, 3}}; 写入 want[1]
    want[2] =
        new int[][] {
          {1, 8, 7}, {2, 9, 6}, {3, 4, 5}
        }; // 把 new int[][] {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}; 写入 want[2]
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < sizes.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 sizes.长度 就继续
      Matrix obj = new Matrix(sizes[k]); // 把 new Matrix(sizes[下标 k]); 写入 Matrix obj
      obj.fill(1, 0, sizes[k]); // obj.fill(1, 0, sizes[下标 k]);
      if (!eq2(obj.M, want[k])) { // 若 取反 eq2(obj.M, want[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL Matrix(" + sizes[k] + ").fill=" + show(obj.M) + " want " + show(want[k])); // 打印输出
      }
      obj.clear(); // obj.clear();
      for (int[] row : obj.M) { // for (int[] row : obj.M) {
        for (int v : row) { // for (int 值 : row) {
          if (v != 0) { // 若 值 不等于 0
            ok = false; // 把 false; 写入 ok
            System.out.println("FAIL clear() 后仍有非零值: " + show(obj.M)); // 打印输出
          }
        }
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
