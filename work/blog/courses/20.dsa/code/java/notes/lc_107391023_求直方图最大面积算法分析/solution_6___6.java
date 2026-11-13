// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc107391023_solution66 { // 定义类型
  // 分治法：以区间最小高度为高，递归左右
  static int dc(int[] a, int l, int r) { // 定义函数/方法 dc
    if (l > r) return 0; // 若 左指针 超过 右指针，直接返回 0
    if (l == r) return a[l]; // 若 左指针 等于 右指针，直接返回 数组[左指针]
    int minIdx = l; // 把 左指针 存入 minIdx
    for (int i = l; i <= r; i++) { // 让 下标 i 从 左指针 开始计数，下标 i 不超过 右指针 就继续
      if (a[i] < a[minIdx]) minIdx = i; // 若 数组[下标 i] 小于 数组[minIdx]) minIdx 赋值为 下标 i;
    }
    int area = a[minIdx] * (r - l + 1); // 把 数组[minIdx] 乘 (右指针 减 左指针 加 1) 存入 area
    int left = dc(a, l, minIdx - 1); // 把 dc(数组, 左指针, minIdx 减 1) 存入 左边界
    int right = dc(a, minIdx + 1, r); // 把 dc(数组, minIdx 加 1, 右指针) 存入 右边界
    return Math.max(area, Math.max(left, right)); // 返回 Math.取较大值 area, Math.取较大值 左边界, 右边界))
  }

  static int getResult(int n, int[] h) { // 定义函数/方法 getResult
    int[] bars = new int[n]; // 把 new int[元素个数]; 写入 int[] bars
    for (int i = 0; i < n; i++) bars[i] = h[i + 1]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return dc(bars, 0, n - 1); // 返回 dc(bars, 0, 元素个数 减 1)
  }

  static int run(int n, int[] heights) { // 定义函数/方法 run
    int[] h = new int[n + 2]; // 把 new int[元素个数 加 2]; 写入 int[] h
    h[0] = 0; // 把 0; 写入 h[0]
    h[n + 1] = 0; // 把 0; 写入 h[n + 1]
    for (int i = 0; i < n; i++) h[i + 1] = heights[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    return getResult(n, h); // 返回 getResult(元素个数, h)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc107391023_solution66 s =
        new lc107391023_solution66(); // 把 new lc107391023_solution66(); 写入 lc107391023_solution66 s
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
