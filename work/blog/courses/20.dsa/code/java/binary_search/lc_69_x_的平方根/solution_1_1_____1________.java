// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc69_solution111 { // 定义类型
  // x 的平方根：二分查找（忠实翻译 Python ref_mySqrt）
  public int mySqrt(int x) { // 定义函数/方法 mySqrt
    if (x < 2) return x; // 若 x 小于 2，直接返回 x
    int lo = 1, hi = x / 2; // 把 1, 右边界 赋值为 x 除以 2 存入 左边界
    while (lo <= hi) { // 循环，直到不满足「左边界 不超过 右边界」
      int m = lo + (hi - lo) / 2; // 把 (左边界 加 右边界) 除以 2 存入 映射表
      long sq = (long) m * m; // 把 (long) 映射表 乘 映射表; 写入 long sq
      if (sq <= x && x < (long) (m + 1) * (m + 1))
        return m; // 若 sq 不超过 x 且 x 小于 (long) (映射表 加 1) 乘 (映射表 加 1)，直接返回 映射表
      else if (sq > x) hi = m - 1; // 否则，若 sq 超过 x) 右边界 赋值为 映射表 减 1;
      else lo = m + 1; // 否则
    }
    return lo; // 返回 左边界
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc69_solution111 s = new lc69_solution111(); // 把 new lc69_solution111(); 写入 lc69_solution111 s
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
