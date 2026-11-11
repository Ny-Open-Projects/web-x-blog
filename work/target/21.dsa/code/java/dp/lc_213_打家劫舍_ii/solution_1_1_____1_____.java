// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc213_solution111 { // 定义类型
  public int rob(int[] nums) { // 定义函数/方法 rob
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    if (n == 1) return nums[0]; // 若 元素个数 等于 1，直接返回 数组[0]
    if (n == 2) return Math.max(nums[0], nums[1]); // 若 元素个数 等于 2，直接返回 Math.取较大值 数组[0], 数组[1])
    int[] dp1 = new int[n]; // 把 new int[元素个数]; 写入 int[] dp1
    int[] dp2 = new int[n]; // 把 new int[元素个数]; 写入 int[] dp2
    dp1[0] = nums[0]; // 把 数组[0]; 写入 dp1[0]
    dp1[1] = Math.max(nums[0], nums[1]); // 把 Math.取较大值 数组[0], 数组[1]); 写入 dp1[1]
    for (int i = 2; i < n; i++) { // 让 下标 i 从 2 开始计数，下标 i 小于 元素个数 减 1 就继续
      dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }
    dp2[1] = nums[1]; // 把 数组[1]; 写入 dp2[1]
    for (int i = 2; i < n; i++) { // 让 下标 i 从 2 开始计数，下标 i 小于 元素个数 就继续
      dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + nums[i]);
    }
    return Math.max(dp1[n - 2], dp2[n - 1]); // 返回 Math.取较大值 dp1[元素个数 减 2], dp2[元素个数 减 1])
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc213_solution111 s =
        new lc213_solution111(); // 把 new lc213_solution111(); 写入 lc213_solution111 s
    int got = s.rob(new int[] {2, 3, 2}); // 把 字符串.rob(new int[]{2, 3, 2}) 存入 got
    if (got != 3) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
