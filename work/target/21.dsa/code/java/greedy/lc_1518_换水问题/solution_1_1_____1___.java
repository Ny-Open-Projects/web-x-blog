// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386044
package com.webfault.dsa; // 引入依赖

class lc1518_solution111 { // 定义类型
  static int numWaterBottles(int numBottles, int numExchange) { // 定义函数/方法 numWaterBottles
    int ans = numBottles; // 把 numBottles 存入 答案
    int empty = numBottles; // 把 numBottles 存入 empty
    while (empty >= numExchange) { // 循环，直到不满足「empty 不低于 numExchange」
      int newBottles = empty / numExchange; // 把 empty 除以 numExchange 存入 newBottles
      ans += newBottles; // 答案累加 newBottles
      empty = newBottles + empty % numExchange; // 把 newBottles 加 empty 对…取模 numExchange; 写入 empty
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int got = numWaterBottles(9, 3); // 把 numWaterBottles(9, 3) 存入 got
    if (got != 13) { // 若 got 不等于 13
      throw new RuntimeException("FAILED: got " + got + " want 13");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
