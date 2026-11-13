// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831489
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc926_solution111 { // 定义类型
  public int minFlipsMonoIncr(String s) { // 定义函数/方法 minFlipsMonoIncr
    int n = s.length(); // 把 字符串.长度() 存入 元素个数
    int dp0 = 0, dp1 = 0; // 把 0, dp1 赋值为 0 存入 dp0
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      char c = s.charAt(i); // 逐字符处理
      int dp0New = dp0; // 把 dp0 存入 dp0New
      int dp1New = Math.min(dp0, dp1); // 把 Math.取较小值 dp0, dp1) 存入 dp1New
      if (c == '1') { // 若 字符 等于 '1'
        dp0New++; // dp0New 加一
      } else { // 否则
        dp1New++; // dp1New 加一
      }
      dp0 = dp0New; // 把 dp0New; 写入 dp0
      dp1 = dp1New; // 把 dp1New; 写入 dp1
    }
    return Math.min(dp0, dp1); // 返回 Math.取较小值 dp0, dp1)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc926_solution111 s =
        new lc926_solution111(); // 把 new lc926_solution111(); 写入 lc926_solution111 s
    int got = s.minFlipsMonoIncr("00110"); // 把 字符串.minFlipsMonoIncr(「00110」) 存入 got
    if (got != 1) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
