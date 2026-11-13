// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831489
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc926_solution222 { // 定义类型
  public int minFlipsMonoIncr(String s) { // 定义函数/方法 minFlipsMonoIncr
    int one = 0; // 把 0 存入 one
    int dp = 0; // 把 0 存入 DP 表
    for (int i = 0; i < s.length(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.长度() 就继续
      char c = s.charAt(i); // 逐字符处理
      if (c == '0') { // 若 字符 等于 '0'
        dp = Math.min(one, dp + 1); // 把 Math.取较小值 one, DP 表 加 1); 写入 DP 表
      } else { // 否则
        one++; // one 加一
      }
    }
    return dp; // 返回 DP 表
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc926_solution222 s =
        new lc926_solution222(); // 把 new lc926_solution222(); 写入 lc926_solution222 s
    int got = s.minFlipsMonoIncr("00110"); // 把 字符串.minFlipsMonoIncr(「00110」) 存入 got
    if (got != 1) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
