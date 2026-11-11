// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_10___10.py (bubble_sort_v5: early stop + jump)
  static void bubbleSortV5(int[] nums) { // 定义函数/方法 bubbleSortV5
    int length = nums.length; // 把 数组.长度 存入 长度
    int k = length - 1; // 跳跃标识
    int last = 0; // 内层循环标识
    int i = 0; // 最外层循环标识
    boolean sorted = false; // 哨兵变量
    while (i < length - 1 && !sorted) { // 循环，直到不满足「下标 i 小于 长度 减 1 且 取反 sorted」
      sorted = true; // 把 true; 写入 sorted
      for (int j = 0; j < k; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 k 就继续
        if (nums[j] > nums[j + 1]) { // 若 数组[下标 j] 超过 数组[下标 j 加 1]
          int t = nums[j];
          nums[j] = nums[j + 1];
          nums[j + 1] = t;
          last = j; // 把 下标 j; 写入 last
          sorted = false; // 把 false; 写入 sorted
        }
      }
      k = last; // 把 last; 写入 下标 k
      i += 1; // 下标 i累加 1
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
      bubbleSortV5(arr); // bubbleSortV5(数组);
      if (!Arrays.equals(arr, wants[ci])) { // 若 取反 Arrays.equals(数组, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL bubbleSortV5("
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
