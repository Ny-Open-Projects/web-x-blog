// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853675
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型

  static int minCostClimbingStairs(int[] cost) { // 定义函数/方法 minCostClimbingStairs
    int n = cost.length; // 把 cost.长度 存入 元素个数
    int prev2 = cost[0]; // 把 cost[0] 存入 prev2
    int prev1 = cost[1]; // 把 cost[1] 存入 prev1
    for (int i = 2; i < n; i++) { // 让 下标 i 从 2 开始计数，下标 i 小于 元素个数 就继续
      int cur = cost[i] + Math.min(prev1, prev2); // 把 cost[下标 i] 加 Math.取较小值 prev1, prev2) 存入 当前值
      prev2 = prev1; // 把 prev1; 写入 prev2
      prev1 = cur; // 把 当前值; 写入 prev1
    }
    return Math.min(prev1, prev2); // 返回 Math.取较小值 prev1, prev2)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{10, 15, 20}, {15}},
      {{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}, {6}},
    };
    for (int k = 0; k < cases.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 cases.长度 就继续
      int[] cost = cases[k][0]; // 把 cases[下标 k][0]; 写入 int[] cost
      int want = cases[k][1][0]; // 把 cases[下标 k][1][0] 存入 want
      int got = minCostClimbingStairs(cost); // 把 minCostClimbingStairs(cost) 存入 got
      if (got != want) { // 若 got 不等于 want
        System.out.println("FAIL: got " + got + " expected " + want); // 打印输出
        throw new RuntimeException(
            "self-check failed"); // throw new RuntimeException(「self 减 check failed」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
