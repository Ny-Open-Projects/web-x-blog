// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847570
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class solution_1_1_____1______ { // 定义类型
  static int maxSubArray(int[] nums) { // 定义函数/方法 maxSubArray
    int best = nums[0]; // 把 数组[0] 存入 当前最优
    int cur = nums[0]; // 把 数组[0] 存入 当前值
    for (int i = 1; i < nums.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      cur = Math.max(nums[i], cur + nums[i]); // 把 Math.取较大值 数组[下标 i], 当前值 加 数组[下标 i]); 写入 当前值
      best = Math.max(best, cur); // 把 Math.取较大值 当前最优, 当前值); 写入 当前最优
    }
    return best; // 返回 当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean fail = false; // 把 false; 写入 boolean fail
    fail |= !check(new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6);
    fail |= !check(new int[] {1}, 1); // 把 取反 check(new int[]{1}, 1); 写入 fail |
    fail |=
        !check(
            new int[] {5, 4, -1, 7, 8},
            23); // 把 取反 check(new int[]{5, 4, 减 1, 7, 8}, 23); 写入 fail |
    if (fail) throw new RuntimeException("FAILED"); // 若 fail) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean check(int[] nums, int want) { // 定义判定函数 check
    int got = maxSubArray(nums); // 把 maxSubArray(数组) 存入 got
    if (got != want) { // 若 got 不等于 want
      System.out.println(
          "FAIL maxSubArray(" + Arrays.toString(nums) + ")=" + got + " want " + want); // 打印输出
      return false; // 返回 false
    }
    return true; // 返回 true
  }
}
