// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134633617
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static int maxProfit(int[] prices) { // 定义函数/方法 maxProfit
    int profit = 0; // 把 0 存入 profit
    for (int i = 1; i < prices.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
      if (prices[i] > prices[i - 1]) { // 若 价格序列[下标 i] 超过 价格序列[下标 i 减 1]
        profit += prices[i] - prices[i - 1]; // profit累加 价格序列[下标 i] 减 价格序列[下标 i 减 1]
      }
    }
    return profit; // 返回 profit
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = { // 把 { 写入 int[][] ins
      {7, 1, 5, 3, 6, 4},
      {1, 2, 3, 4, 5},
      {7, 6, 4, 3, 1},
      {},
      {1},
      {1, 2},
    };
    int[] wants = {7, 4, 0, 0, 0, 1}; // 把 {7, 4, 0, 0, 0, 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < ins.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 ins.长度 就继续
      int got = maxProfit(ins[k]); // 把 maxProfit(ins[下标 k]) 存入 got
      if (got != wants[k]) { // 若 got 不等于 wants[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL maxProfit("
                + java.util.Arrays.toString(ins[k])
                + ")="
                + got
                + " want "
                + wants[k]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
