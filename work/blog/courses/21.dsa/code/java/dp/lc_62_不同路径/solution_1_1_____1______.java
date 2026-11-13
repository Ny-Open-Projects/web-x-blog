// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc62_solution111 { // 定义类型
  // 不同路径：排列组合 C(m+n-2, m-1)
  // 忠实于 Python 参考实现 ref_uniquePaths 的等价数学形式
  public int uniquePaths(int m, int n) { // 定义函数/方法 uniquePaths
    int k = Math.min(m - 1, n - 1); // 把 Math.取较小值 映射表 减 1, 元素个数 减 1) 存入 下标 k
    long result = 1; // 把 1; 写入 long result
    for (int i = 1; i <= k; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 下标 k 就继续
      result *= (m + n - 1 - i); // 把 (映射表 加 元素个数 减 1 减 下标 i); 写入 result *
      result = result / i; // 把 结果 除以 下标 i; 写入 结果
    }
    return (int) result; // 返回 (int) 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc62_solution111 s = new lc62_solution111(); // 把 new lc62_solution111(); 写入 lc62_solution111 s
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
