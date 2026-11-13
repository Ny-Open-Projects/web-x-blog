// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc213_solution222 { // 定义类型
  public int rob(int[] nums) { // 定义函数/方法 rob
    int len = nums.length; // 把 数组.长度 存入 长度
    if (len == 0) return 0; // 若 长度 等于 0，直接返回 0
    if (len == 1) return nums[0]; // 若 长度 等于 1，直接返回 数组[0]
    if (len == 2) return Math.max(nums[0], nums[1]); // 若 长度 等于 2，直接返回 Math.取较大值 数组[0], 数组[1])
    int ret1 = robRange(nums, 0, len - 2); // 把 robRange(数组, 0, 长度 减 2) 存入 ret1
    int ret2 = robRange(nums, 1, len - 1); // 把 robRange(数组, 1, 长度 减 1) 存入 ret2
    return Math.max(ret1, ret2); // 返回 Math.取较大值 ret1, ret2)
  }

  private int robRange(int[] nums, int start, int end) { // 定义函数/方法 robRange
    int dp0 = 0, dp1 = 0; // 把 0, dp1 赋值为 0 存入 dp0
    for (int i = start; i <= end; i++) { // 让 下标 i 从 起点 开始计数，下标 i 不超过 终点 就继续
      int tmp = dp1; // 把 dp1 存入 临时变量
      dp1 = Math.max(dp0 + nums[i], dp1); // 把 Math.取较大值 dp0 加 数组[下标 i], dp1); 写入 dp1
      dp0 = tmp; // 把 临时变量; 写入 dp0
    }
    return dp1; // 返回 dp1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc213_solution222 s =
        new lc213_solution222(); // 把 new lc213_solution222(); 写入 lc213_solution222 s
    int got = s.rob(new int[] {2, 3, 2}); // 把 字符串.rob(new int[]{2, 3, 2}) 存入 got
    if (got != 3) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
