// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_1___1.py (stable count sort: prefix sums + backfill)
  static int[] countSort(int[] nums) { // 定义函数/方法 countSort
    if (nums.length == 0) return nums; // 若 数组.长度 等于 0，直接返回 数组
    int maxVal = nums[0], minVal = nums[0]; // 把 数组[0], minVal 赋值为 数组[0] 存入 maxVal
    for (int v : nums) {
      if (v > maxVal) maxVal = v;
      if (v < minVal) minVal = v;
    }
    int rangeVal = maxVal - minVal + 1; // 把 maxVal 减 minVal 加 1 存入 rangeVal
    int[] count = new int[rangeVal]; // 把 new int[rangeVal]; 写入 int[] count
    int[] output = new int[nums.length]; // 把 new int[数组.长度]; 写入 int[] output
    for (int num : nums)
      count[num - minVal] += 1; // 把 1; 写入 for (int num : nums) count[num - minVal] +
    for (int i = 1; i < rangeVal; i++)
      count[i] += count[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 rangeVal 就继续
    for (int i = nums.length - 1; i >= 0; i--) { // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 不低于 0 就继续
      output[count[nums[i] - minVal] - 1] =
          nums[i]; // 把 数组[下标 i]; 写入 output[count[nums[i] - minVal] - 1]
      count[nums[i] - minVal] -= 1; // 把 1; 写入 count[nums[i] - minVal] -
    }
    return output; // 返回 输出
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {3, 1, 2},
      {5, -3, 0, 5, -1},
      {1, 2, 3},
      {},
      {7},
      {1},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3},
      {-3, -1, 0, 5, 5},
      {1, 2, 3},
      {},
      {7},
      {1},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      int[] got = countSort(cases[ci]); // 把 countSort(cases[ci]); 写入 int[] got
      if (!Arrays.equals(got, wants[ci])) { // 若 取反 Arrays.equals(got, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL countSort("
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
