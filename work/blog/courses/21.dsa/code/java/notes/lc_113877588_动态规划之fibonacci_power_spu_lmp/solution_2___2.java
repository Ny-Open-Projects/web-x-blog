// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113877588
package com.webfault.dsa; // 引入依赖

class lc113877588_solution22 { // 定义类型
  // 快速幂 O(log n)
  static long power(long base, int exp) { // 定义函数/方法 power
    if (exp == 0) return 1; // 若 exp 等于 0，直接返回 1
    long half = power(base, exp >> 1); // 把 power(base, exp 超过 超过 1); 写入 long half
    if ((exp & 1) == 0) return half * half; // 若 (exp 按位与 1) 等于 0，直接返回 half 乘 half
    return half * half * base; // 返回 half 乘 half 乘 base
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (power(2, 10) != 1024) { // 若 power(2, 10) 不等于 1024
      System.out.println("FAIL"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
