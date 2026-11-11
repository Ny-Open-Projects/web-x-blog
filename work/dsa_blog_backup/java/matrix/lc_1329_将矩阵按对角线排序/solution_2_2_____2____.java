// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1329_solution222 { // 定义类型
  public int[][] diagonalSort(int[][] mat) { // 定义函数/方法 diagonalSort
    int m = mat.length; // 把 mat.长度 存入 映射表
    int n = mat[0].length; // 把 mat[0].长度 存入 元素个数
    for (int k = 1 - n; k < m; k++) { // 让 下标 k 从 1 减 元素个数 开始计数，下标 k 小于 映射表 就继续
      int left_i = Math.max(0, k); // 把 Math.取较大值 0, 下标 k) 存入 left_i
      int left_j = Math.max(0, -k); // 把 Math.取较大值 0, 减 下标 k) 存入 left_j
      int right_i = Math.min(m - 1, n - 1 + k); // 把 Math.取较小值 映射表 减 1, 元素个数 减 1 加 下标 k) 存入 right_i
      int right_j = Math.min(m - 1 - k, n - 1); // 把 Math.取较小值 映射表 减 1 减 下标 k, 元素个数 减 1) 存入 right_j
      int len = right_i - left_i + 1; // 把 right_i 减 left_i 加 1 存入 长度
      int[] a = new int[len]; // 把 new int[长度]; 写入 int[] a
      for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        a[i] = mat[left_i + i][left_j + i]; // 把 mat[left_i 加 下标 i][left_j 加 下标 i]; 写入 a[i]
      }
      Arrays.sort(a); // 排序
      for (int i = 0; i < len; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
        mat[left_i + i][left_j + i] = a[i]; // 把 数组[下标 i]; 写入 mat[left_i + i][left_j + i]
      }
    }
    return mat; // 返回 mat
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc1329_solution222 s =
        new lc1329_solution222(); // 把 new lc1329_solution222(); 写入 lc1329_solution222 s
    int[][][] tests = { // 把 { 写入 int[][][] tests
      {{3, 3, 1, 1}, {2, 2, 1, 2}, {1, 1, 1, 2}},
      {{10, 6, 8}, {15, 11, 7}, {14, 5, 12}},
      {{5}} // { {5} }
    };
    int[][][] wants = { // 把 { 写入 int[][][] wants
      {{1, 1, 1, 1}, {1, 2, 2, 2}, {1, 2, 3, 3}},
      {{10, 6, 8}, {5, 11, 7}, {14, 15, 12}},
      {{5}} // { {5} }
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int t = 0; t < tests.length; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 tests.长度 就继续
      int[][] got = s.diagonalSort(tests[t]); // 把 字符串.diagonalSort(tests[另一字符串]); 写入 int[][] got
      if (!Arrays.deepEquals(got, wants[t])) { // 若 取反 Arrays.deepEquals(got, wants[另一字符串]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL diagonalSort case "
                + t
                + " got "
                + Arrays.deepToString(got)
                + " want "
                + Arrays.deepToString(wants[t])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
