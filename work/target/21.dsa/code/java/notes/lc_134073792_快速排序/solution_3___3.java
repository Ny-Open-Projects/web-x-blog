// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class QuickS3 { // 定义类型
  static void swap(int[] a, int i, int j) {
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
  }

  static int partition(int[] array, int low, int high) { // 定义函数/方法 partition
    int mid = low + (high - low) / 2; // 把 (low 加 high) 除以 2 存入 中点
    if (array[low] > array[high])
      swap(array, low, high); // 若 array[low] 超过 array[high]) 交换 array, low, high);
    if (array[mid] > array[high])
      swap(array, mid, high); // 若 array[中点] 超过 array[high]) 交换 array, 中点, high);
    if (array[mid] > array[low])
      swap(array, mid, low); // 若 array[中点] 超过 array[low]) 交换 array, 中点, low);
    int pivot = array[low]; // 把 array[low] 存入 pivot
    int i = low + 1; // 把 low 加 1 存入 下标 i
    for (int j = i; j <= high; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 不超过 high 就继续
      if (array[j] <= pivot) {
        swap(array, i, j);
        i++;
      }
    }
    swap(array, low, i - 1); // 交换 array 与 low, 下标 i 减 1
    return i - 1; // 返回 下标 i 减 1
  }

  static void quickSort(int[] a, int low, int high) { // 定义函数/方法 quickSort
    if (low < high) { // 若 low 小于 high
      int pi = partition(a, low, high); // 把 partition(数组, low, high) 存入 pi
      quickSort(a, low, pi - 1); // quickSort(数组, low, pi 减 1);
      quickSort(a, pi + 1, high); // quickSort(数组, pi 加 1, high);
    }
  }

  static int[] quickSortWrapper(int[] a) { // 定义函数/方法 quickSortWrapper
    if (a.length > 0) quickSort(a, 0, a.length - 1); // 若 数组.长度 超过 0) quickSort(数组, 0, 数组.长度 减 1);
    return a; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{9, -20, 99, 3, 6, 8, 10, 1, 2, 1}, {-20, 1, 1, 2, 3, 6, 8, 9, 10, 99}},
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{}, {}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] in = c[0].clone(); // 把 字符[0].clone(); 写入 int[] in
      quickSortWrapper(in); // quickSortWrapper(in);
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
