// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_12___12.py (count_sort stable: prefix sums + backfill
  // in place)
  static void countSort(int[] lst) { // 定义函数/方法 countSort
    int length = lst.length; // 把 lst.长度 存入 长度
    if (length < 2) return; // 若 长度 小于 2) return;
    int maxVal = lst[0], minVal = lst[0]; // 把 lst[0], minVal 赋值为 lst[0] 存入 maxVal
    for (int num : lst) {
      if (num > maxVal) maxVal = num;
      if (num < minVal) minVal = num;
    }
    int[] countList =
        new int[maxVal - minVal + 1]; // 把 new int[maxVal 减 minVal 加 1]; 写入 int[] countList
    int[] result = new int[length]; // 把 new int[长度]; 写入 int[] result
    for (int num : lst)
      countList[num - minVal] += 1; // 把 1; 写入 for (int num : lst) countList[num - minVal] +
    for (int j = 1; j < countList.length; j++)
      countList[j] += countList[j - 1]; // 让 下标 j 从 1 开始计数，下标 j 小于 countList.长度 就继续
    for (int k = length - 1; k >= 0; k--) { // 让 下标 k 从 长度 减 1 开始计数，下标 k 不低于 0 就继续
      int currentIndex =
          countList[lst[k] - minVal] - 1; // 把 countList[lst[下标 k] 减 minVal] 减 1 存入 currentIndex
      result[currentIndex] = lst[k]; // 把 lst[下标 k]; 写入 result[currentIndex]
      countList[lst[k] - minVal] -= 1; // 把 1; 写入 countList[lst[k] - minVal] -
    }
    for (int i = 0; i < length; i++) lst[i] = result[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 长度 就继续
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {3, 1, 2},
      {5, -3, 0, 5, -1},
      {1, 2, 3},
      {},
      {7},
      {1},
      {2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3},
      {-3, -1, 0, 5, 5},
      {1, 2, 3},
      {},
      {7},
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
