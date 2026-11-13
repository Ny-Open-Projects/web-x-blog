// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370043
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型

  static void sortColors(int[] nums) { // 定义函数/方法 sortColors
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int ptr = 0; // 把 0 存入 ptr
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if (nums[i] == 0) { // 若 数组[下标 i] 等于 0
        int tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
        nums[i] = nums[ptr]; // 把 数组[ptr]; 写入 nums[i]
        nums[ptr] = tmp; // 把 临时变量; 写入 nums[ptr]
        ptr++; // ptr 加一
      }
    }
    for (int i = ptr; i < n; i++) { // 让 下标 i 从 ptr 开始计数，下标 i 小于 元素个数 就继续
      if (nums[i] == 1) { // 若 数组[下标 i] 等于 1
        int tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
        nums[i] = nums[ptr]; // 把 数组[ptr]; 写入 nums[i]
        nums[ptr] = tmp; // 把 临时变量; 写入 nums[ptr]
        ptr++; // ptr 加一
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{2, 0, 2, 1, 1, 0}, {0, 0, 1, 1, 2, 2}},
      {{0}, {0}},
      {{2, 0, 1}, {0, 1, 2}},
    };
    for (int k = 0; k < cases.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 cases.长度 就继续
      int[] input = cases[k][0]; // 把 cases[下标 k][0]; 写入 int[] input
      int[] expected = cases[k][1]; // 把 cases[下标 k][1]; 写入 int[] expected
      sortColors(input); // sortColors(input);
      if (!java.util.Arrays.equals(
          input, expected)) { // 若 取反 java.util.Arrays.equals(input, expected
        System.out.println("FAIL at case " + k); // 打印输出
        throw new RuntimeException(
            "self-check failed"); // throw new RuntimeException(「self 减 check failed」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
