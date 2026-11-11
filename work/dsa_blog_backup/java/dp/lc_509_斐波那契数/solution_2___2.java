// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package com.webfault.dsa; // 引入依赖

import java.util.HashMap; // 引入依赖
import java.util.Map; // 引入依赖

/** LeetCode 509. 斐波那契数 忠实翻译 python/dp/lc_509_斐波那契数/solution_2___2.py 带记忆化的递归 */
class Main { // 定义类型

  Map<Integer, Integer> memo; // Map 小于 Integer, Integer 超过 记忆化表;

  int fib(int n) { // 定义函数/方法 fib
    if (memo == null) { // 若 记忆化表 等于 null
      memo = new HashMap<Integer, Integer>(); // 把 new HashMap 小于 Integer, Integer 超过 (); 写入 记忆化表
    }
    if (n <= 1) { // 若 元素个数 不超过 1
      return n; // 返回 元素个数
    }
    if (memo.containsKey(Integer.valueOf(n))) { // 若 记忆化表.containsKey(Integer.valueOf(元素个数
      return memo.get(Integer.valueOf(n))
          .intValue(); // 返回 记忆化表 查找 Integer.valueOf(元素个数)).intValue()
    }
    int v = fib(n - 1) + fib(n - 2); // 把 fib(元素个数 减 1) 加 fib(元素个数 减 2) 存入 值
    memo.put(
        Integer.valueOf(n),
        Integer.valueOf(v)); // 记忆化表.put(Integer.valueOf(元素个数), Integer.valueOf(值));
    return v; // 返回 值
  }

  public static void main(String[] args) { // public static void main(String[] args) {
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
      Main s = new Main(); // 把 new Main(); 写入 Main s
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
