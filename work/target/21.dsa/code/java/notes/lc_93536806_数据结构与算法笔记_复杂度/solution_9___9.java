// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  int fib_recursive(int n) { // 定义函数/方法 fib_recursive
    if (n < 2) return n; // 若 元素个数 小于 2，直接返回 元素个数
    return fib_recursive(n - 1)
        + fib_recursive(n - 2); // 返回 fib_recursive(元素个数 减 1) 加 fib_recursive(元素个数 减 2)
  }

  int fib_iterative(int n) { // 定义函数/方法 fib_iterative
    if (n < 2) return n; // 若 元素个数 小于 2，直接返回 元素个数
    int a = 0, b = 1; // 把 0, b 赋值为 1 存入 数组
    for (int k = 2; k <= n; k++) {
      int t = b;
      b = a + b;
      a = t;
    } // 让 下标 k 从 2 开始计数，下标 k 不超过 元素个数 就继续
    return b; // 返回 b
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.fib_recursive(0) != 0) {
      ok = false;
      System.out.println("FAIL fib_recursive0");
    }
    if (s.fib_iterative(0) != 0) {
      ok = false;
      System.out.println("FAIL fib_iterative0");
    }
    if (s.fib_recursive(10) != 55) {
      ok = false;
      System.out.println("FAIL fib_recursive");
    }
    if (s.fib_iterative(10) != 55) {
      ok = false;
      System.out.println("FAIL fib_iterative");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
