// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144829935
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc3105_solution111 { // 定义类型
  public int longestMonotonicSubarray(int[] nums) { // 定义函数/方法 longestMonotonicSubarray
    if (nums.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int ans = 1, inc = 1, dec = 1; // 把 1, inc 赋值为 1, dec 赋值为 1 存入 答案
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
      if (nums[i] > nums[i - 1]) { // 若 数组[下标 i] 超过 数组[下标 i 减 1]
        inc++;
        dec = 1; // 把 1; 写入 inc++; dec
      } else if (nums[i] < nums[i - 1]) { // 否则，若 数组[下标 i] 小于 数组[下标 i 减 1]
        dec++;
        inc = 1; // 把 1; 写入 dec++; inc
      } else { // 否则
        inc = 1;
        dec = 1; // 把 1; dec 赋值为 1; 写入 inc
      }
      ans = Math.max(ans, Math.max(inc, dec)); // 把 Math.取较大值 答案, Math.取较大值 inc, dec)); 写入 答案
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc3105_solution111 s =
        new lc3105_solution111(); // 把 new lc3105_solution111(); 写入 lc3105_solution111 s
    int got = s.longestMonotonicSubarray(new int[] {1, 4, 3, 3, 2});
    if (got != 2) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
