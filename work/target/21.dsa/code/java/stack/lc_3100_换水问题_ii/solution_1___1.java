// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc3100_solution11 { // 定义类型
  static int maxBottlesDrunk(int numBottles, int numExchange) { // 定义函数/方法 maxBottlesDrunk
    int total = numBottles; // 把 numBottles 存入 总和
    while (numBottles >= numExchange) { // 循环，直到不满足「numBottles 不低于 numExchange」
      numBottles += 1 - numExchange; // numBottles累加 1 减 numExchange
      numExchange += 1; // numExchange累加 1
      total += 1; // 总和累加 1
    }
    return total; // 返回 总和
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (maxBottlesDrunk(10, 3) != 13) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
