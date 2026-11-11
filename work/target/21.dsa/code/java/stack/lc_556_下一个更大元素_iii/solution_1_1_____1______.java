// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc556_solution111 { // 定义类型
  static int nextGreaterElement(int n) { // 定义函数/方法 nextGreaterElement
    int MAX = 2147483647; // 把 2147483647 存入 MAX
    char[] nums =
        String.valueOf(n).toCharArray(); // 把 String.valueOf(元素个数).toCharArray(); 写入 char[] nums
    int i = nums.length - 2; // 把 数组.长度 减 2 存入 下标 i
    while (i >= 0 && nums[i] >= nums[i + 1])
      i--; // 循环，直到不满足「下标 i 不低于 0 且 数组[下标 i] 不低于 数组[下标 i 加 1]) 下标 i 减一 ;」
    if (i < 0) return -1; // 若 下标 i 小于 0，直接返回 减 1
    int j = nums.length - 1; // 把 数组.长度 减 1 存入 下标 j
    while (nums[j] <= nums[i]) j--; // 循环，直到不满足「数组[下标 j] 不超过 数组[下标 i]) 下标 j 减一 ;」
    char t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
    int lo = i + 1, hi = nums.length - 1; // 把 下标 i 加 1, 右边界 赋值为 数组.长度 减 1 存入 左边界
    while (lo < hi) {
      char z = nums[lo];
      nums[lo] = nums[hi];
      nums[hi] = z;
      lo++;
      hi--;
    }
    try { // try {
      long ans = Long.parseLong(new String(nums)); // 把 Long.parseLong(new String(数组)); 写入 long ans
      return ans > MAX ? -1 : (int) ans; // 返回 答案 超过 MAX ? 减 1 : (int) 答案
    } catch (Exception e) {
      return -1;
    } // } catch (Exception e) { return 减 1; }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (nextGreaterElement(1) != -1) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
