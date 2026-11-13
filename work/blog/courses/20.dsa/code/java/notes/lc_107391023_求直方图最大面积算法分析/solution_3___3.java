// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc107391023_solution33 { // 定义类型
  // 卡位法：对每个柱子向左右扩展找到第一个更矮的位置
  static int getResult(int n, int[] h) { // 定义函数/方法 getResult
    int res = 0; // 把 0 存入 结果
    for (int i = 1; i <= n; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
      int L = i, R = i; // 把 下标 i, R 赋值为 下标 i 存入 L
      while (L - 1 >= 1 && h[L - 1] >= h[i])
        L--; // 循环，直到不满足「L 减 1 不低于 1 且 h[L 减 1] 不低于 h[下标 i]) L 减一 ;」
      while (R + 1 <= n && h[R + 1] >= h[i])
        R++; // 循环，直到不满足「R 加 1 不超过 元素个数 且 h[R 加 1] 不低于 h[下标 i]) R 加一 ;」
      int area = h[i] * (R - L + 1); // 把 h[下标 i] 乘 (R 减 L 加 1) 存入 area
      if (area > res) res = area; // 若 area 超过 结果) 结果 赋值为 area;
    }
    return res; // 返回 结果
  }

  static int run(int n, int[] heights) { // 定义函数/方法 run
    int[] h = new int[n + 2]; // 把 new int[元素个数 加 2]; 写入 int[] h
    h[0] = 0; // 把 0; 写入 h[0]
    h[n + 1] = 0; // 把 0; 写入 h[n + 1]
    for (int i = 0; i < n; i++) h[i + 1] = heights[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return getResult(n, h); // 返回 getResult(元素个数, h)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc107391023_solution33 s =
        new lc107391023_solution33(); // 把 new lc107391023_solution33(); 写入 lc107391023_solution33 s
    if (s.run(5, new int[] {2, 3, 3, 3, 2})
        != 10) { // 若 字符串.run(5, new int[]{2, 3, 3, 3, 2}) 不等于 10
      System.out.println("FAIL 1"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    if (s.run(1, new int[] {5}) != 5) { // 若 字符串.run(1, new int[]{5}) 不等于 5
      System.out.println("FAIL 2"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
