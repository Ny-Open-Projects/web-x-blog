// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class Main { // 定义类型
  static int[] grayCode(int n) { // 定义函数/方法 grayCode
    int[] res = new int[1 << n]; // 把 new int[1 小于 小于 元素个数]; 写入 int[] res
    for (int i = 0; i < (1 << n); i++)
      res[i] = i ^ (i >> 1); // 让 下标 i 从 0 开始计数，下标 i 小于 (1 小于 小于 元素个数) 就继续
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] ins = {0, 1, 2};
    int[][] ws = {{0}, {0, 1}, {0, 1, 3, 2}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      int[] got = grayCode(ins[i]); // 把 grayCode(ins[下标 i]); 写入 int[] got
      if (!Arrays.equals(got, ws[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
