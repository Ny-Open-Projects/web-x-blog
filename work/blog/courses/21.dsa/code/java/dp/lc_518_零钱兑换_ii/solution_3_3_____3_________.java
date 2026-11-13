// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852221
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc518_solution333 { // 定义类型
  public int change(int amount, int[] coins) { // 定义函数/方法 change
    int n = coins.length; // 把 硬币面额.长度 存入 元素个数
    int[][] f = new int[n + 1][amount + 1]; // 把 new int[元素个数 加 1][目标金额 加 1]; 写入 int[][] f
    f[0][0] = 1; // 把 1; 写入 f[0][0]
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int c = 0; c <= amount; c++) { // 让 字符 从 0 开始计数，字符 不超过 目标金额 就继续
        if (c < coins[i]) { // 若 字符 小于 硬币面额[下标 i]
          f[i + 1][c] = f[i][c]; // 把 f[下标 i][字符]; 写入 f[i + 1][c]
        } else { // 否则
          f[i + 1][c] =
              f[i][c]
                  + f[i + 1][
                      c - coins[i]]; // 把 f[下标 i][字符] 加 f[下标 i 加 1][字符 减 硬币面额[下标 i]]; 写入 f[i + 1][c]
        }
      }
    }
    return f[n][amount]; // 返回 f[元素个数][目标金额]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc518_solution333 s =
        new lc518_solution333(); // 把 new lc518_solution333(); 写入 lc518_solution333 s
    int got = s.change(5, new int[] {1, 2, 5}); // 把 字符串.change(5, new int[]{1, 2, 5}) 存入 got
    if (got != 4) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
