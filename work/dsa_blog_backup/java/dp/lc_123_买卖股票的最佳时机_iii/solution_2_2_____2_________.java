// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144849793
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc123_solution222 { // 定义类型
  public int maxProfit(int[] prices) { // 定义函数/方法 maxProfit
    int n = prices.length; // 把 价格序列.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    int buy1 = -prices[0]; // 把 减 价格序列[0] 存入 buy1
    int buy2 = -prices[0]; // 把 减 价格序列[0] 存入 buy2
    int sell1 = 0; // 把 0 存入 sell1
    int sell2 = 0; // 把 0 存入 sell2
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
      buy1 = Math.max(buy1, -prices[i]); // 把 Math.取较大值 buy1, 减 价格序列[下标 i]); 写入 buy1
      sell1 = Math.max(sell1, buy1 + prices[i]); // 把 Math.取较大值 sell1, buy1 加 价格序列[下标 i]); 写入 sell1
      buy2 = Math.max(buy2, sell1 - prices[i]); // 把 Math.取较大值 buy2, sell1 减 价格序列[下标 i]); 写入 buy2
      sell2 = Math.max(sell2, buy2 + prices[i]); // 把 Math.取较大值 sell2, buy2 加 价格序列[下标 i]); 写入 sell2
    }
    return sell2; // 返回 sell2
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc123_solution222 s =
        new lc123_solution222(); // 把 new lc123_solution222(); 写入 lc123_solution222 s
    int got =
        s.maxProfit(
            new int[] {
              3, 3, 5, 0, 0, 3, 1, 4
            }); // 把 字符串.maxProfit(new int[]{3, 3, 5, 0, 0, 3, 1, 4}) 存入 got
    if (got != 6) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
