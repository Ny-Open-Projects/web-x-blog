// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class SeqS1 { // 定义类型
  static int seqSearch(int[] arr, int target) { // 定义函数/方法 seqSearch
    for (int i = 0; i < arr.length; i++)
      if (arr[i] == target) return i; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] arrs = {
      {1, 2, 3}, {1, 2, 3}, {5, 4, 3, 2, 1}
    }; // 把 { {1, 2, 3}, {1, 2, 3}, {5, 4, 3, 2, 1} }; 写入 int[][] arrs
    int[] targets = {1, 9, 3}; // 把 { 1, 9, 3 }; 写入 int[] targets
    int[] wants = {0, -1, 2}; // 把 { 0, 减 1, 2 }; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < arrs.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 arrs.长度 就继续
      int got =
          SeqS1.seqSearch(
              arrs[i].clone(),
              targets[i]); // 把 SeqS1.seqSearch(arrs[下标 i].clone(), targets[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL seqSearch("
                + Arrays.toString(arrs[i])
                + ","
                + targets[i]
                + ")="
                + got
                + " want "
                + wants[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
