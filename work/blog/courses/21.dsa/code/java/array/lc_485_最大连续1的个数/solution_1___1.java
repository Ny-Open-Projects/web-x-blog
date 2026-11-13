package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型

  static int findMaxConsecutiveOnes(int[] nums) { // 定义函数/方法 findMaxConsecutiveOnes
    int best = 0, cur = 0; // 把 0, 当前值 赋值为 0 存入 当前最优
    for (int x : nums) { // for (int x : 数组) {
      if (x == 1) { // 若 x 等于 1
        cur++; // 当前值 加一
        if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
      } else { // 否则
        cur = 0; // 把 0; 写入 当前值
      }
    }
    return best; // 返回 当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{1, 1, 0, 1, 1, 1}, {3}},
      {{1, 0, 1, 1, 0, 1}, {2}},
      {{0}, {0}},
    };
    for (int k = 0; k < cases.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 cases.长度 就继续
      int[] nums = cases[k][0]; // 把 cases[下标 k][0]; 写入 int[] nums
      int want = cases[k][1][0]; // 把 cases[下标 k][1][0] 存入 want
      int got = findMaxConsecutiveOnes(nums); // 把 findMaxConsecutiveOnes(数组) 存入 got
      if (got != want) { // 若 got 不等于 want
        System.out.println("FAIL: got " + got + " expected " + want); // 打印输出
        throw new RuntimeException(
            "self-check failed"); // throw new RuntimeException(「self 减 check failed」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
