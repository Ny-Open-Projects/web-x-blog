// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc209_solution44 { // 定义类型
  public int minSubArrayLen(int target, int[] nums) { // 定义函数/方法 minSubArrayLen
    int len = nums.length; // 把 数组.长度 存入 长度
    int slow = 0, fast = 0; // 把 0, 快指针 赋值为 0 存入 慢指针
    int sum = 0; // 把 0 存入 累计和
    int result = len + 1; // 把 长度 加 1 存入 结果
    while (fast < len) { // 循环，直到不满足「快指针 小于 长度」
      sum += nums[fast++]; // 累计和累加 数组[快指针 加一 ]
      while (sum >= target) { // 循环，直到不满足「累计和 不低于 目标值」
        int subLen = fast - slow; // 把 快指针 减 慢指针 存入 subLen
        result = Math.min(result, subLen); // 把 Math.取较小值 结果, subLen); 写入 结果
        sum -= nums[slow++]; // 累计和累减 数组[慢指针 加一 ]
      }
    }
    return result == len + 1 ? 0 : result; // 返回 结果 等于 长度 加 1 ? 0 : 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc209_solution44 s = new lc209_solution44(); // 把 new lc209_solution44(); 写入 lc209_solution44 s
    int[] targets = {7, 11, 11, 4, 15, 0}; // 把 {7, 11, 11, 4, 15, 0}; 写入 int[] targets
    int[][] numsArr = { // 把 { 写入 int[][] numsArr
      {2, 3, 1, 2, 4, 3},
      {1, 2, 3, 4, 5},
      {1, 1, 1, 1, 1, 1, 1, 1},
      {1, 4, 4},
      {1, 2, 3, 4, 5, 6, 7, 8},
      {} // {}
    };
    int[] want = {2, 3, 0, 1, 2, 0}; // 把 {2, 3, 0, 1, 2, 0}; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < want.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
      int got =
          s.minSubArrayLen(
              targets[i], numsArr[i]); // 把 字符串.minSubArrayLen(targets[下标 i], numsArr[下标 i]) 存入 got
      if (got != want[i]) { // 若 got 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL case " + i + " got " + got + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
