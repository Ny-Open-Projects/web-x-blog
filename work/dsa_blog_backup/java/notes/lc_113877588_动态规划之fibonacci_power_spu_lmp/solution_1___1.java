// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc113877588_solution11 { // 定义类型
  // 记忆化 Fibonacci
  static Map<Integer, Integer> memo =
      new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 static Map<Integer, Integer> memo

  static int fibonacci(int n) { // 定义函数/方法 fibonacci
    if (n <= 1) return n; // 若 元素个数 不超过 1，直接返回 元素个数
    if (memo.containsKey(n)) return memo.get(n); // 若 记忆化表.containsKey(元素个数)，直接返回 记忆化表 查找 元素个数)
    int v = fibonacci(n - 1) + fibonacci(n - 2); // 把 fibonacci(元素个数 减 1) 加 fibonacci(元素个数 减 2) 存入 值
    memo.put(n, v); // 记忆化表.put(元素个数, 值);
    return v; // 返回 值
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (fibonacci(10) != 55) { // 若 fibonacci(10) 不等于 55
      System.out.println("FAIL"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
