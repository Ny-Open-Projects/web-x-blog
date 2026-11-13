// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc213_solution444 { // 定义类型
  public int rob(int[] nums) { // 定义函数/方法 rob
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    if (n == 1) return nums[0]; // 若 元素个数 等于 1，直接返回 数组[0]
    if (n == 2) return Math.max(nums[0], nums[1]); // 若 元素个数 等于 2，直接返回 Math.取较大值 数组[0], 数组[1])
    int left =
        helper(
            Arrays.copyOfRange(
                nums, 2, n - 1)); // 把 helper(Arrays.copyOfRange(数组, 2, 元素个数 减 1)) 存入 左边界
    int right =
        helper(Arrays.copyOfRange(nums, 1, n)); // 把 helper(Arrays.copyOfRange(数组, 1, 元素个数)) 存入 右边界
    return Math.max(nums[0] + left, right); // 返回 Math.取较大值 数组[0] 加 左边界, 右边界)
  }

  private int helper(int[] arr) { // 定义函数/方法 helper
    int f0 = 0, f1 = 0; // 把 0, f1 赋值为 0 存入 f0
    for (int x : arr) { // for (int x : 数组) {
      int nf1 = Math.max(f1, f0 + x); // 把 Math.取较大值 f1, f0 加 x) 存入 nf1
      f0 = f1; // 把 f1; 写入 f0
      f1 = nf1; // 把 nf1; 写入 f1
    }
    return f1; // 返回 f1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc213_solution444 s =
        new lc213_solution444(); // 把 new lc213_solution444(); 写入 lc213_solution444 s
    int got = s.rob(new int[] {2, 3, 2}); // 把 字符串.rob(new int[]{2, 3, 2}) 存入 got
    if (got != 3) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
