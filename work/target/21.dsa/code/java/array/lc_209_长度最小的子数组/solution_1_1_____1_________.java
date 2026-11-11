// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc209_solution111 { // 定义类型
  public int minSubArrayLen(int target, int[] nums) { // 定义函数/方法 minSubArrayLen
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    int ans = Integer.MAX_VALUE; // 把 Integer.MAX_VALUE 存入 答案
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      int sum = 0; // 把 0 存入 累计和
      for (int j = i; j < n; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
        sum += nums[j]; // 累计和累加 数组[下标 j]
        if (sum >= target) { // 若 累计和 不低于 目标值
          ans = Math.min(ans, j - i + 1); // 把 Math.取较小值 答案, 下标 j 减 下标 i 加 1); 写入 答案
          break; // 跳出循环
        }
      }
    }
    return ans == Integer.MAX_VALUE ? 0 : ans; // 返回 答案 等于 Integer.MAX_VALUE ? 0 : 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc209_solution111 s =
        new lc209_solution111(); // 把 new lc209_solution111(); 写入 lc209_solution111 s
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
