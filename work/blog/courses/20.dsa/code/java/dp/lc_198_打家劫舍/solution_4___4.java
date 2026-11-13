// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130670245
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class solution_4___4 { // 定义类型
  static int rob(int[] nums) { // 定义函数/方法 rob
    int prev = 0, cur = 0; // 把 0, 当前值 赋值为 0 存入 前一个
    for (int x : nums) { // for (int x : 数组) {
      int nxt = Math.max(cur, prev + x); // 把 Math.取较大值 当前值, 前一个 加 x) 存入 nxt
      prev = cur; // 把 当前值; 写入 前一个
      cur = nxt; // 把 nxt; 写入 当前值
    }
    return cur; // 返回 当前值
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean fail = false; // 把 false; 写入 boolean fail
    fail |= !check(new int[] {1, 2, 3, 1}, 4); // 把 取反 check(new int[]{1, 2, 3, 1}, 4); 写入 fail |
    fail |=
        !check(
            new int[] {2, 7, 9, 3, 1}, 12); // 把 取反 check(new int[]{2, 7, 9, 3, 1}, 12); 写入 fail |
    fail |= !check(new int[] {2, 1, 1, 2}, 4); // 把 取反 check(new int[]{2, 1, 1, 2}, 4); 写入 fail |
    if (fail) throw new RuntimeException("FAILED"); // 若 fail) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean check(int[] nums, int want) { // 定义判定函数 check
    int got = rob(nums); // 把 rob(数组) 存入 got
    if (got != want) { // 若 got 不等于 want
      System.out.println(
          "FAIL rob(" + Arrays.toString(nums) + ")=" + got + " want " + want); // 打印输出
      return false; // 返回 false
    }
    return true; // 返回 true
  }
}
