// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc518_solution444 { // 定义类型
  public int change(int amount, int[] coins) { // 定义函数/方法 change
    int[] f = new int[amount + 1]; // 把 new int[目标金额 加 1]; 写入 int[] f
    f[0] = 1; // 把 1; 写入 f[0]
    for (int x : coins) { // for (int x : 硬币面额) {
      for (int c = x; c <= amount; c++) { // 让 字符 从 x 开始计数，字符 不超过 目标金额 就继续
        f[c] += f[c - x]; // f[c]累加 f[字符 减 x]
      }
    }
    return f[amount]; // 返回 f[目标金额]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc518_solution444 s =
        new lc518_solution444(); // 把 new lc518_solution444(); 写入 lc518_solution444 s
    int got = s.change(5, new int[] {1, 2, 5}); // 把 字符串.change(5, new int[]{1, 2, 5}) 存入 got
    if (got != 4) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
