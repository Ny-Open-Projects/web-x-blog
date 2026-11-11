// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package com.webfault.dsa; // 引入依赖

/**
 * LeetCode 509. 斐波那契数 忠实翻译 python/dp/lc_509_斐波那契数/solution_4___4.py 两个变量 start/end 滚动迭代，用临时变量保存旧
 * end
 */
class Main { // 定义类型

  int fib(int n) { // 定义函数/方法 fib
    if (n == 0) { // 若 元素个数 等于 0
      return 0; // 返回 0
    }
    if (n == 1) { // 若 元素个数 等于 1
      return 1; // 返回 1
    }
    int start = 0; // 把 0 存入 起点
    int end = 1; // 把 1 存入 终点
    for (int i = 2; i <= n; i++) { // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
      int endTmp = end; // 把 终点 存入 endTmp
      end = end + start; // 把 终点 加 起点; 写入 终点
      start = endTmp; // 把 endTmp; 写入 起点
    }
    return end; // 返回 终点
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
