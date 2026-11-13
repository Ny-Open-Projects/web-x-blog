// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_6___6.py (bubble_sort_v1: basic, tmp swap)
  static void bubbleSortV1(int[] nums) { // 定义函数/方法 bubbleSortV1
    int length = nums.length; // 把 数组.长度 存入 长度
    for (int i = 0; i < length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
      for (int j = 0; j < length - 1 - i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 长度 减 1 减 下标 i 就继续
        if (nums[j] > nums[j + 1]) { // 若 数组[下标 j] 超过 数组[下标 j 加 1]
          int tmp = nums[j]; // 把 数组[下标 j] 存入 临时变量
          nums[j] = nums[j + 1]; // 把 数组[下标 j 加 1]; 写入 nums[j]
          nums[j + 1] = tmp; // 把 临时变量; 写入 nums[j + 1]
        }
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {5, 4, 3, 2, 1},
      {1, 2, 3},
      {3, 1, 2},
      {},
      {1},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3, 4, 5},
      {1, 2, 3},
      {1, 2, 3},
      {},
      {1},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      int[] arr = cases[ci].clone(); // 把 cases[ci].clone(); 写入 int[] arr
      bubbleSortV1(arr); // bubbleSortV1(数组);
      if (!Arrays.equals(arr, wants[ci])) { // 若 取反 Arrays.equals(数组, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL bubbleSortV1("
                + Arrays.toString(cases[ci])
                + ")="
                + Arrays.toString(arr)
                + " want="
                + Arrays.toString(wants[ci])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
