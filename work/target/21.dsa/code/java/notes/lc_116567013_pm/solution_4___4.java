// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
package com.webfault.dsa; // 引入依赖

class lc116567013_solution44 { // 定义类型
  // KMP next 表（单独呈现）
  static int[] buildNext(String P) { // 定义函数/方法 buildNext
    int m = P.length(); // 把 P.长度() 存入 映射表
    int[] N = new int[m]; // 把 new int[映射表]; 写入 int[] N
    N[0] = -1; // 把 减 1; 写入 N[0]
    int j = 0, t = -1; // 把 0, 另一字符串 赋值为 减 1 存入 下标 j
    while (j < m - 1) { // 循环，直到不满足「下标 j 小于 映射表 减 1」
      if (t < 0 || P.charAt(j) == P.charAt(t)) { // 若 另一字符串 小于 0 或 P 取字符 下标 j) 等于 P 取字符 另一字符串
        j++; // 下标 j 加一
        t++; // 另一字符串 加一
        N[j] = t; // 把 另一字符串; 写入 N[j]
      } else { // 否则
        t = N[t]; // 把 N[另一字符串]; 写入 另一字符串
      }
    }
    return N; // 返回 N
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] table = buildNext("ababaca"); // 把 buildNext(「ababaca」); 写入 int[] table
    int[] expect = {-1, 0, 0, 1, 2, 3, 0}; // 把 { 减 1, 0, 0, 1, 2, 3, 0}; 写入 int[] expect
    if (table.length != expect.length) {
      System.out.println("FAIL len");
      throw new RuntimeException("FAILED");
    }
    for (int i = 0; i < expect.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 expect.长度 就继续
      if (table[i] != expect[i]) { // 若 table[下标 i] 不等于 expect[下标 i]
        System.out.println("FAIL at " + i + " got " + table[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
