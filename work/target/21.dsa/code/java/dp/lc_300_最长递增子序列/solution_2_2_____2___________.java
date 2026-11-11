// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144823912
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static int lengthOfLIS(int[] nums) { // 定义函数/方法 lengthOfLIS
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    java.util.ArrayList<Integer> dp = new java.util.ArrayList<>();
    for (int num : nums) { // for (int num : 数组) {
      int i = 0; // 把 0 存入 下标 i
      while (i < dp.size() && dp.get(i) < num) i++;
      if (i == dp.size()) dp.add(num); // 若 下标 i 等于 DP 表.大小()) DP 表 追加 num);
      else dp.set(i, num); // 否则
    }
    return dp.size(); // 返回 DP 表.大小()
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
