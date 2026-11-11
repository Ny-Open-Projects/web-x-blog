// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc69_solution444 { // 定义类型
  // x 的平方根：牛顿迭代法
  // 忠实于 Python ref_mySqrt 求整数平方根的等价结果
  public int mySqrt(int x) { // 定义函数/方法 mySqrt
    if (x == 0) return 0; // 若 x 等于 0，直接返回 0
    double C = x, x0 = x; // 把 x, x0 赋值为 x 存入 C
    while (true) { // 循环，直到不满足「true」
      double xi = 0.5 * (x0 + C / x0); // 把 0.5 乘 (x0 加 C 除以 x0) 存入 xi
      if (Math.abs(x0 - xi) < 1e-7) { // 若 Math.取绝对值 x0 减 xi) 小于 1e 减 7
        break; // 跳出循环
      }
      x0 = xi; // 把 xi; 写入 x0
    }
    return (int) x0; // 返回 (int) x0
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc69_solution444 s = new lc69_solution444(); // 把 new lc69_solution444(); 写入 lc69_solution444 s
    int[][] cases = {{4, 2}, {8, 2}, {16, 4}, {2147395599, 46339}};
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      int got = s.mySqrt(c[0]); // 把 字符串.mySqrt(字符[0]) 存入 got
      if (got != c[1]) { // 若 got 不等于 字符[1]
        System.out.println("FAIL: mySqrt(" + c[0] + ")=" + got + " want " + c[1]); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
