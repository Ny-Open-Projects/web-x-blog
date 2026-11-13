// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355902
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc877_solution222 { // 定义类型
  public boolean stoneGame(int[] piles) { // 定义函数/方法 stoneGame
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc877_solution222 s =
        new lc877_solution222(); // 把 new lc877_solution222(); 写入 lc877_solution222 s
    boolean got =
        s.stoneGame(
            new int[] {5, 3, 4, 5}); // 把 字符串.stoneGame(new int[]{5, 3, 4, 5}); 写入 boolean got
    if (got != true) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
