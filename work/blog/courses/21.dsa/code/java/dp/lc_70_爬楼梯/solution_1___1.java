// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
package com.webfault.dsa; // 引入依赖

class solution_1___1 { // 定义类型
  static int climbStairs(int n) { // 定义函数/方法 climbStairs
    if (n <= 1) return 1; // 若 元素个数 不超过 1，直接返回 1
    int prev = 1, cur = 1; // 把 1, 当前值 赋值为 1 存入 前一个
    for (int k = 2; k <= n; k++) { // 让 下标 k 从 2 开始计数，下标 k 不超过 元素个数 就继续
      int tmp = cur; // 把 当前值 存入 临时变量
      cur = prev + cur; // 把 前一个 加 当前值; 写入 当前值
      prev = tmp; // 把 临时变量; 写入 前一个
    }
    return cur; // 返回 当前值
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean fail = false; // 把 false; 写入 boolean fail
    fail |= !check(2, 2); // 把 取反 check(2, 2); 写入 fail |
    fail |= !check(3, 3); // 把 取反 check(3, 3); 写入 fail |
    fail |= !check(10, 89); // 把 取反 check(10, 89); 写入 fail |
    if (fail) throw new RuntimeException("FAILED"); // 若 fail) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean check(int n, int want) { // 定义判定函数 check
    int got = climbStairs(n); // 把 climbStairs(元素个数) 存入 got
    if (got != want) { // 若 got 不等于 want
      System.out.println("FAIL climbStairs(" + n + ")=" + got + " want " + want); // 打印输出
      return false; // 返回 false
    }
    return true; // 返回 true
  }
}
