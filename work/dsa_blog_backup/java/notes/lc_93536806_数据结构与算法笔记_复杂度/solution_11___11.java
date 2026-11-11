// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  int[][] matrix_multiply(int[][] a, int[][] b) { // 定义函数/方法 matrix_multiply
    int n = a.length; // 把 数组.长度 存入 元素个数
    int[][] c = new int[n][n]; // 把 new int[元素个数][元素个数]; 写入 int[][] c
    for (int i = 0; i < n; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int j = 0; j < n; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
      for (int k = 0; k < n; k++) // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
        c[i][j] += a[i][k] * b[k][j]; // c[i][j]累加 数组[下标 i][下标 k] 乘 b[下标 k][下标 j]
    return c; // 返回 字符
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    int[][] a = {{1, 2}, {3, 4}}; // 把 {{1, 2}, {3, 4}}; 写入 int[][] a
    int[][] b = {{5, 6}, {7, 8}}; // 把 {{5, 6}, {7, 8}}; 写入 int[][] b
    int[][] want = {{19, 22}, {43, 50}}; // 把 {{19, 22}, {43, 50}}; 写入 int[][] want
    int[][] a1 = {{5}}; // 把 {{5}}; 写入 int[][] a1
    int[][] b1 = {{2}}; // 把 {{2}}; 写入 int[][] b1
    int[][] want1 = {{10}}; // 把 {{10}}; 写入 int[][] want1
    int[][] got = s.matrix_multiply(a, b); // 把 字符串.matrix_multiply(数组, b); 写入 int[][] got
    int[][] got1 = s.matrix_multiply(a1, b1); // 把 字符串.matrix_multiply(a1, b1); 写入 int[][] got1
    boolean ok = true; // 把 true; 写入 boolean ok
    if (got.length != want.length) ok = false; // 若 got.长度 不等于 want.长度) ok 赋值为 false;
    else
      for (int i = 0; i < want.length; i++) // 否则
      if (!java.util.Arrays.equals(got[i], want[i])) ok = false;
    if (got1.length != want1.length) ok = false; // 若 got1.长度 不等于 want1.长度) ok 赋值为 false;
    else
      for (int i = 0; i < want1.length; i++) // 否则
      if (!java.util.Arrays.equals(got1[i], want1[i])) ok = false;
    if (!ok) {
      System.out.println("FAIL");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
