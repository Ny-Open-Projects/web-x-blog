// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class SelS3 { // 定义类型
  static int[] selectionSort(int[] nums) { // 定义函数/方法 selectionSort
    int[] arr = nums.clone(); // 把 数组.clone(); 写入 int[] arr
    int length = arr.length; // 把 数组.长度 存入 长度
    for (int i = 0; i < length - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 减 1 就继续
      int minIndex = i; // 把 下标 i 存入 minIndex
      for (int j = i + 1; j < length; j++)
        if (arr[j] < arr[minIndex]) minIndex = j; // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 长度 就继续
      if (i != minIndex) {
        int t = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = t;
      }
    }
    return arr; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{1, 2, 3}, {1, 2, 3}},
      {{3, 1, 2}, {1, 2, 3}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got =
          SelS3.selectionSort(c[0].clone()); // 把 SelS3.selectionSort(字符[0].clone()); 写入 int[] got
      if (!Arrays.equals(got, c[1])) { // 若 取反 Arrays.equals(got, 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL "
                + Arrays.toString(c[0])
                + " -> "
                + Arrays.toString(got)
                + " want "
                + Arrays.toString(c[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
