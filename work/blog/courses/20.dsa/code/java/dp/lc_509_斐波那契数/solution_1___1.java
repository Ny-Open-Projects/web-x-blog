// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package com.webfault.dsa; // 引入依赖

/**
 * LeetCode 509. 斐波那契数 忠实翻译 python/dp/lc_509_斐波那契数/solution_1___1.py 朴素递归：fib(n) = fib(n-1) +
 * fib(n-2)
 */
class Main { // 定义类型

  int fib(int n) { // 定义函数/方法 fib
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    if (n == 1) return 1; // 若 元素个数 等于 1，直接返回 1
    return fib(n - 1) + fib(n - 2); // 返回 fib(元素个数 减 1) 加 fib(元素个数 减 2)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    int[][] cases = { // 把 { 写入 int[][] cases
      {0, 0}, // 边界：n=0
      {1, 1}, // 边界：n=1
      {2, 1},
      {5, 5},
      {10, 55},
      {30, 832040} // {30, 832040}
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      int got = s.fib(c[0]); // 把 字符串.fib(字符[0]) 存入 got
      if (got != c[1]) { // 若 got 不等于 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL fib(" + c[0] + ")=" + got + " want " + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
