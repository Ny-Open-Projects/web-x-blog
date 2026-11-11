// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc3105_solution222 { // 定义类型
  public int longestMonotonicSubarray(int[] nums) { // 定义函数/方法 longestMonotonicSubarray
    if (nums.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int ans = 1; // 把 1 存入 答案
    int i = 0; // 把 0 存入 下标 i
    while (i < n) { // 循环，直到不满足「下标 i 小于 元素个数」
      int j = i; // 把 下标 i 存入 下标 j
      while (j + 1 < n && nums[j + 1] > nums[j]) j++;
      ans = Math.max(ans, j - i + 1); // 把 Math.取较大值 答案, 下标 j 减 下标 i 加 1); 写入 答案
      j = i; // 把 下标 i; 写入 下标 j
      while (j + 1 < n && nums[j + 1] < nums[j]) j++;
      ans = Math.max(ans, j - i + 1); // 把 Math.取较大值 答案, 下标 j 减 下标 i 加 1); 写入 答案
      i++; // 下标 i 加一
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc3105_solution222 s =
        new lc3105_solution222(); // 把 new lc3105_solution222(); 写入 lc3105_solution222 s
    int got = s.longestMonotonicSubarray(new int[] {1, 4, 3, 3, 2});
    if (got != 2) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
