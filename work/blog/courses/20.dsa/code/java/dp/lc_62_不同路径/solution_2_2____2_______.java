// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc62_solution222 { // 定义类型
  // 不同路径：组合优化版（单循环累加）
  // 忠实于 Python 参考实现 ref_uniquePaths 的等价数学形式
  public int uniquePaths(int m, int n) { // 定义函数/方法 uniquePaths
    long ans = 1; // 把 1; 写入 long ans
    for (int x = n, y = 1; y < m; x++, y++) { // 让 x 从 元素个数, y 赋值为 1 开始计数，y 小于 映射表 就继续
      ans = ans * x / y; // 把 答案 乘 x 除以 y; 写入 答案
    }
    return (int) ans; // 返回 (int) 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc62_solution222 s = new lc62_solution222(); // 把 new lc62_solution222(); 写入 lc62_solution222 s
    int[][] cases = {
      {3, 7, 28}, {3, 2, 3}, {1, 1, 1}
    }; // 把 {{3, 7, 28}, {3, 2, 3}, {1, 1, 1}}; 写入 int[][] cases
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      int got = s.uniquePaths(c[0], c[1]); // 把 字符串.uniquePaths(字符[0], 字符[1]) 存入 got
      if (got != c[2]) { // 若 got 不等于 字符[2]
        System.out.println(
            "FAIL: uniquePaths(" + c[0] + "," + c[1] + ")=" + got + " want " + c[2]); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
