// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc107391023_solution11 { // 定义类型
  // 暴力 O(n^3)：枚举所有区间，求区间最小高度
  static int getResult(int n, int[] h) { // 定义函数/方法 getResult
    int res = 0; // 把 0 存入 结果
    for (int a = 1; a <= n; a++) { // 让 数组 从 1 开始计数，数组 不超过 元素个数 就继续
      for (int b = a; b <= n; b++) { // 让 b 从 数组 开始计数，b 不超过 元素个数 就继续
        int minH = h[a]; // 把 h[数组] 存入 minH
        for (int c = a; c <= b; c++) { // 让 字符 从 数组 开始计数，字符 不超过 b 就继续
          if (h[c] < minH) minH = h[c]; // 若 h[字符] 小于 minH) minH 赋值为 h[字符];
        }
        int area = (b - a + 1) * minH; // 把 (b 减 数组 加 1) 乘 minH 存入 area
        if (area > res) res = area; // 若 area 超过 结果) 结果 赋值为 area;
      }
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
    lc107391023_solution11 s =
        new lc107391023_solution11(); // 把 new lc107391023_solution11(); 写入 lc107391023_solution11 s
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
