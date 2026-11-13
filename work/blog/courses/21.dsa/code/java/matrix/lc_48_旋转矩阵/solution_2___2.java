// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型

  static void rotate(int[][] matrix) { // 定义函数/方法 rotate
    int n = matrix.length; // 把 矩阵.长度 存入 元素个数
    for (int i = 0; i < n / 2; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 除以 2 就继续
      int[] tmp = matrix[i]; // 把 矩阵[下标 i]; 写入 int[] tmp
      matrix[i] = matrix[n - 1 - i]; // 把 矩阵[元素个数 减 1 减 下标 i]; 写入 matrix[i]
      matrix[n - 1 - i] = tmp; // 把 临时变量; 写入 matrix[n - 1 - i]
    }
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        int tmp = matrix[i][j]; // 把 矩阵[下标 i][下标 j] 存入 临时变量
        matrix[i][j] = matrix[j][i]; // 把 矩阵[下标 j][下标 i]; 写入 matrix[i][j]
        matrix[j][i] = tmp; // 把 临时变量; 写入 matrix[j][i]
      }
    }
  }

  static boolean eqMatrix(int[][] a, int[][] b) { // 定义函数/方法 eqMatrix
    if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i].length != b[i].length) return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
      for (int j = 0; j < a[i].length; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
        if (a[i][j] != b[i][j]) return false; // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]，直接返回 false
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] inputs = { // 把 { 写入 int[][][] inputs
      {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
      {{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}},
    };
    int[][][] expecteds = { // 把 { 写入 int[][][] expecteds
      {{7, 4, 1}, {8, 5, 2}, {9, 6, 3}},
      {{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}},
    };
    for (int k = 0; k < inputs.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 inputs.长度 就继续
      int[][] input = inputs[k]; // 把 inputs[下标 k]; 写入 int[][] input
      int[][] expected = expecteds[k]; // 把 expecteds[下标 k]; 写入 int[][] expected
      rotate(input); // rotate(input);
      if (!eqMatrix(input, expected)) { // 若 取反 eqMatrix(input, expected
        System.out.println("FAIL at case " + k); // 打印输出
        throw new RuntimeException(
            "self-check failed"); // throw new RuntimeException(「self 减 check failed」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
