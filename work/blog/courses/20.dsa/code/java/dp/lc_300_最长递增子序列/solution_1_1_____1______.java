// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144823912
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static int lengthOfLIS(int[] nums) { // 定义函数/方法 lengthOfLIS
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    int[] dp = new int[n]; // 把 new int[元素个数]; 写入 int[] dp
    for (int i = 0; i < n; i++) dp[i] = 1; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
    int best = dp[0]; // 把 DP 表[0] 存入 当前最优
    for (int v : dp) if (v > best) best = v; // 把 值; 写入 for (int v : dp) if (v > best) best
    return best; // 返回 当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {10, 9, 2, 5, 3, 7, 101, 18},
      {0, 1, 0, 3, 2, 3},
      {7, 7, 7, 7},
      {1, 3, 6, 7, 9, 4, 10, 5, 6},
    };
    int[] wants = {4, 4, 1, 6}; // 把 {4, 4, 1, 6}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      int got = lengthOfLIS(cases[ci]); // 把 lengthOfLIS(cases[ci]) 存入 got
      if (got != wants[ci]) { // 若 got 不等于 wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL case " + ci + " got " + got + " want " + wants[ci]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
