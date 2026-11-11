// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class Main { // 定义类型
  static int findContentChildren(int[] g, int[] s) { // 定义函数/方法 findContentChildren
    Arrays.sort(g);
    Arrays.sort(s); // 排序
    int i = 0, j = 0, ans = 0; // 把 0, 下标 j 赋值为 0, 答案 赋值为 0 存入 下标 i
    while (i < g.length && j < s.length) { // 循环，直到不满足「下标 i 小于 g.长度 且 下标 j 小于 字符串.长度」
      if (s[j] >= g[i]) {
        ans++;
        i++;
        j++;
      } else {
        j++;
      }
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] g = {{1, 2, 3}, {1, 2}, {1, 2, 3}};
    int[][] s = {{1, 1}, {1, 2, 3}, {3}};
    int[] ws = {1, 2, 1};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < g.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 g.长度 就继续
      int got = findContentChildren(g[i], s[i]); // 把 findContentChildren(g[下标 i], 字符串[下标 i]) 存入 got
      if (got != ws[i]) {
        ok = false;
        System.out.println("FAIL " + got + " want " + ws[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
