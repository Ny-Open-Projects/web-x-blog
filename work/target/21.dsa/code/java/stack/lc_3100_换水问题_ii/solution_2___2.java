// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc3100_solution22 { // 定义类型
  static int maxBottlesDrunk(int numBottles, int numExchange) { // 定义函数/方法 maxBottlesDrunk
    int result = 0, emptyBottles = 0; // 把 0, emptyBottles 赋值为 0 存入 结果
    boolean flag = true; // 把 true; 写入 boolean flag
    while (flag) { // 循环，直到不满足「flag」
      flag = false; // 把 false; 写入 flag
      if (numBottles > 0) { // 若 numBottles 超过 0
        result += numBottles; // 结果累加 numBottles
        emptyBottles += numBottles; // emptyBottles累加 numBottles
        numBottles = 0; // 把 0; 写入 numBottles
        flag = true; // 把 true; 写入 flag
      }
      if (emptyBottles >= numExchange) { // 若 emptyBottles 不低于 numExchange
        numBottles += 1; // numBottles累加 1
        emptyBottles -= numExchange; // emptyBottles累减 numExchange
        numExchange += 1; // numExchange累加 1
        flag = true; // 把 true; 写入 flag
      }
    }
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (maxBottlesDrunk(10, 3) != 13) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
