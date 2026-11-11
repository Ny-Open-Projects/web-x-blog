// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849130
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class solution_3_3_____3_________ { // 定义类型
  static int maxProfit(int[] prices) { // 定义函数/方法 maxProfit
    int n = prices.length; // 把 价格序列.长度 存入 元素个数
    int maxprofit = 0; // 把 0 存入 maxprofit
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = i + 1; j < n; j++) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
        int profit = prices[j] - prices[i]; // 把 价格序列[下标 j] 减 价格序列[下标 i] 存入 profit
        if (profit > maxprofit) { // 若 profit 超过 maxprofit
          maxprofit = profit; // 把 profit; 写入 maxprofit
        }
      }
    }
    return maxprofit; // 返回 maxprofit
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean fail = false; // 把 false; 写入 boolean fail
    fail |=
        !check(
            new int[] {7, 1, 5, 3, 6, 4},
            5); // 把 取反 check(new int[]{7, 1, 5, 3, 6, 4}, 5); 写入 fail |
    fail |=
        !check(new int[] {7, 6, 4, 3, 1}, 0); // 把 取反 check(new int[]{7, 6, 4, 3, 1}, 0); 写入 fail |
    fail |= !check(new int[] {1, 2, 3}, 2); // 把 取反 check(new int[]{1, 2, 3}, 2); 写入 fail |
    if (fail) throw new RuntimeException("FAILED"); // 若 fail) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean check(int[] prices, int want) { // 定义判定函数 check
    int got = maxProfit(prices); // 把 maxProfit(价格序列) 存入 got
    if (got != want) { // 若 got 不等于 want
      System.out.println(
          "FAIL maxProfit(" + Arrays.toString(prices) + ")=" + got + " want " + want); // 打印输出
      return false; // 返回 false
    }
    return true; // 返回 true
  }
}
