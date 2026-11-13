// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_9___9.py (count_sort basic in-place, non-negative)
  static void countSort(int[] lst) { // 定义函数/方法 countSort
    int length = lst.length; // 把 lst.长度 存入 长度
    if (length < 2) return; // 若 长度 小于 2) return;
    int maxVal = lst[0]; // 把 lst[0] 存入 maxVal
    for (int v : lst)
      if (v > maxVal) maxVal = v; // 把 值; 写入 for (int v : lst) if (v > maxVal) maxVal
    int[] countList = new int[maxVal + 1]; // 把 new int[maxVal 加 1]; 写入 int[] countList
    for (int num : lst) countList[num] += 1; // 把 1; 写入 for (int num : lst) countList[num] +
    int i = 0; // 把 0 存入 下标 i
    for (int j = 0; j <= maxVal; j++) { // 让 下标 j 从 0 开始计数，下标 j 不超过 maxVal 就继续
      for (int c = 0; c < countList[j]; c++) { // 让 字符 从 0 开始计数，字符 小于 countList[下标 j] 就继续
        lst[i] = j; // 把 下标 j; 写入 lst[i]
        i += 1; // 下标 i累加 1
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {3, 1, 2},
      {1, 2, 3},
      {},
      {1},
      {2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3},
      {1, 2, 3},
      {},
      {1},
      {1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 6, 7, 7, 8, 8, 9, 9},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      int[] arr = cases[ci].clone(); // 把 cases[ci].clone(); 写入 int[] arr
      countSort(arr); // countSort(数组);
      if (!Arrays.equals(arr, wants[ci])) { // 若 取反 Arrays.equals(数组, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL countSort("
                + Arrays.toString(cases[ci])
                + ")="
                + Arrays.toString(arr)
                + " want="
                + Arrays.toString(wants[ci])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
