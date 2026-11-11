// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc107391023_solution55 { // 定义类型
  // 单调栈（从 i=0 开始，循环到 n 处理剩余）
  static int getResult(int[] h) { // 定义函数/方法 getResult
    int n = h.length; // 把 h.长度 存入 元素个数
    int res = 0; // 把 0 存入 结果
    Deque<Integer> st = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> st
    for (int i = 0; i <= n; i++) { // 让 下标 i 从 0 开始计数，下标 i 不超过 元素个数 就继续
      int cur = (i == n) ? 0 : h[i]; // 把 (下标 i 等于 元素个数) ? 0 : h[下标 i] 存入 当前值
      while (!st.isEmpty()
          && cur < h[st.peek()]) { // 循环，直到不满足「取反 st.isEmpty() 且 当前值 小于 h[st.peek()]」
        int height = h[st.pop()]; // 把 h[st 弹出 )] 存入 height
        int width =
            st.isEmpty()
                ? i
                : i - st.peek() - 1; // 把 st.isEmpty() ? 下标 i : 下标 i 减 st.peek() 减 1 存入 width
        int area = height * width; // 把 height 乘 width 存入 area
        if (area > res) res = area; // 若 area 超过 结果) 结果 赋值为 area;
      }
      st.push(i); // 把 下标 i 压入栈/数组尾部
    }
    return res; // 返回 结果
  }

  static int run(int n, int[] heights) { // 定义函数/方法 run
    return getResult(heights); // 返回 getResult(heights)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc107391023_solution55 s =
        new lc107391023_solution55(); // 把 new lc107391023_solution55(); 写入 lc107391023_solution55 s
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
