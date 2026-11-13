// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc3105_solution333 { // 定义类型
  public int longestMonotonicSubarray(int[] nums) { // 定义函数/方法 longestMonotonicSubarray
    if (nums.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int ans = 1; // 把 1 存入 答案
    int length = 1; // 把 1 存入 长度
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
      if (nums[i] > nums[i - 1]) {
        length++;
        ans = Math.max(ans, length);
      } else length = 1; // 否则
    }
    length = 1; // 把 1; 写入 长度
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
      if (nums[i] < nums[i - 1]) {
        length++;
        ans = Math.max(ans, length);
      } else length = 1; // 否则
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc3105_solution333 s =
        new lc3105_solution333(); // 把 new lc3105_solution333(); 写入 lc3105_solution333 s
    int got = s.longestMonotonicSubarray(new int[] {1, 4, 3, 3, 2});
    if (got != 2) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
