// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class QuickS5 { // 定义类型
  static void swap(int[] a, int i, int j) {
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
  }

  static int partition(int[] arr, int left, int right) { // 定义函数/方法 partition
    int pivot = arr[left]; // 把 数组[左边界] 存入 pivot
    int i = left + 1, j = right; // 把 左边界 加 1, 下标 j 赋值为 右边界 存入 下标 i
    while (i <= j) { // 循环，直到不满足「下标 i 不超过 下标 j」
      while (i <= j && arr[j] >= pivot)
        j--; // 循环，直到不满足「下标 i 不超过 下标 j 且 数组[下标 j] 不低于 pivot) 下标 j 减一 ;」
      while (i <= j && arr[i] <= pivot)
        i++; // 循环，直到不满足「下标 i 不超过 下标 j 且 数组[下标 i] 不超过 pivot) 下标 i 加一 ;」
      if (i <= j) {
        swap(arr, i, j);
      } // 若 下标 i 不超过 下标 j) { 交换 数组, 下标 i, 下标 j); }
    }
    swap(arr, left, j); // 交换 数组 与 左边界, 下标 j
    return j; // 返回 下标 j
  }

  static void quickSortFn(int[] arr, int left, int right) { // 定义函数/方法 quickSortFn
    if (left < right) { // 若 左边界 小于 右边界
      int pi = partition(arr, left, right); // 把 partition(数组, 左边界, 右边界) 存入 pi
      quickSortFn(arr, left, pi - 1); // quickSortFn(数组, 左边界, pi 减 1);
      quickSortFn(arr, pi + 1, right); // quickSortFn(数组, pi 加 1, 右边界);
    }
  }

  static int[] quickSortV2(int[] arr) { // 定义函数/方法 quickSortV2
    if (arr.length > 0)
      quickSortFn(arr, 0, arr.length - 1); // 若 数组.长度 超过 0) quickSortFn(数组, 0, 数组.长度 减 1);
    return arr; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {
        {-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20},
        {-100, -30, -20, -9, -2, 0, 0, 1, 1, 1, 3, 3, 4, 5, 9, 9, 20, 88, 88, 99, 100}
      },
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{}, {}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] in = c[0].clone(); // 把 字符[0].clone(); 写入 int[] in
      quickSortV2(in); // quickSortV2(in);
      if (!Arrays.equals(in, c[1])) { // 若 取反 Arrays.equals(in, 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL "
                + Arrays.toString(c[0])
                + " -> "
                + Arrays.toString(in)
                + " want "
                + Arrays.toString(c[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
