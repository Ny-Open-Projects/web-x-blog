// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_3___3.py (bubble sort with early termination)
  static int[] bubbleSort(int[] nums) { // 定义函数/方法 bubbleSort
    int n = nums.length; // 把 数组.长度 存入 元素个数
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      boolean swapped = false; // 把 false; 写入 boolean swapped
      for (int j = 0; j < n - i - 1; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 下标 i 减 1 就继续
        if (nums[j] > nums[j + 1]) { // 若 数组[下标 j] 超过 数组[下标 j 加 1]
          int t = nums[j];
          nums[j] = nums[j + 1];
          nums[j + 1] = t;
          swapped = true; // 把 true; 写入 swapped
        }
      }
      if (!swapped) break; // 若 取反 swapped) break;
    }
    return nums; // 返回 数组
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
      int[] got = bubbleSort(cases[ci].clone()); // 把 bubbleSort(cases[ci].clone()); 写入 int[] got
      if (!Arrays.equals(got, wants[ci])) { // 若 取反 Arrays.equals(got, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL bubbleSort("
                + Arrays.toString(cases[ci])
                + ")="
                + Arrays.toString(got)
                + " want="
                + Arrays.toString(wants[ci])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
