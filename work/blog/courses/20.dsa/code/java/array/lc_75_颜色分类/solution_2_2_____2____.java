// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370043
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型

  static void sortColors(int[] nums) { // 定义函数/方法 sortColors
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int p0 = 0, p2 = n - 1; // 把 0, p2 赋值为 元素个数 减 1 存入 p0
    int i = 0; // 把 0 存入 下标 i
    while (i <= p2) { // 循环，直到不满足「下标 i 不超过 p2」
      while (i <= p2 && nums[i] == 2) { // 循环，直到不满足「下标 i 不超过 p2 且 数组[下标 i] 等于 2」
        int tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
        nums[i] = nums[p2]; // 把 数组[p2]; 写入 nums[i]
        nums[p2] = tmp; // 把 临时变量; 写入 nums[p2]
        p2--; // p2 减一
      }
      if (nums[i] == 0) { // 若 数组[下标 i] 等于 0
        int tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
        nums[i] = nums[p0]; // 把 数组[p0]; 写入 nums[i]
        nums[p0] = tmp; // 把 临时变量; 写入 nums[p0]
        p0++; // p0 加一
      }
      i++; // 下标 i 加一
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
