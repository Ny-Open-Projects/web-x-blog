// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144853482
package com.webfault.dsa; // 引入依赖

class Lc714S1 { // 定义类型
  int maxProfit(int[] prices, int fee) { // 定义函数/方法 maxProfit
    int cash = 0; // 把 0 存入 cash
    int hold = -prices[0]; // 把 减 价格序列[0] 存入 hold
    for (int i = 1; i < prices.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
      cash =
          Math.max(
              cash, hold + prices[i] - fee); // 把 Math.取较大值 cash, hold 加 价格序列[下标 i] 减 fee); 写入 cash
      hold = Math.max(hold, cash - prices[i]); // 把 Math.取较大值 hold, cash 减 价格序列[下标 i]); 写入 hold
    }
    return cash; // 返回 cash
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc714S1 s = new Lc714S1(); // 把 new Lc714S1(); 写入 Lc714S1 s
    int[][] cases = { // 把 { 写入 int[][] cases
      {1, 3, 2, 8, 4, 9},
      {1, 2, 3, 4, 5},
      {1, 3, 7, 5, 10, 3},
    };
    int[] fees = {2, 1, 3}; // 把 {2,1,3}; 写入 int[] fees
    int[] wants = {8, 3, 6}; // 把 {8,3,6}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < cases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
      int got = s.maxProfit(cases[i], fees[i]); // 把 字符串.maxProfit(cases[下标 i], fees[下标 i]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
