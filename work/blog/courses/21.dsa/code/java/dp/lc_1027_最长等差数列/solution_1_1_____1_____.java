// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831173
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1027_solution111 { // 定义类型
  public int longestArithSeqLength(int[] nums) { // 定义函数/方法 longestArithSeqLength
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n <= 2) return n; // 若 元素个数 不超过 2，直接返回 元素个数
    HashMap<Integer, Integer>[] dp =
        new HashMap[n]; // 把 new HashMap[元素个数]; 写入 HashMap<Integer, Integer>[] dp
    for (int i = 0; i < n; i++) dp[i] = new HashMap<>(); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    int ans = 2; // 把 2 存入 答案
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        int d = nums[i] - nums[j]; // 把 数组[下标 i] 减 数组[下标 j] 存入 d
        int prev = dp[j].getOrDefault(d, 1); // 把 DP 表[下标 j].getOrDefault(d, 1) 存入 前一个
        int cur = prev + 1; // 把 前一个 加 1 存入 当前值
        dp[i].put(d, cur); // DP 表[下标 i].put(d, 当前值);
        if (cur > ans) ans = cur; // 若 当前值 超过 答案) 答案 赋值为 当前值;
      }
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc1027_solution111 s =
        new lc1027_solution111(); // 把 new lc1027_solution111(); 写入 lc1027_solution111 s
    int got = s.longestArithSeqLength(new int[] {9, 4, 7, 2, 10});
    if (got != 3) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
