// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class QuickS2 { // 定义类型
  static void swap(int[] a, int i, int j) {
    int t = a[i];
    a[i] = a[j];
    a[j] = t;
  }

  static int partition(int[] nums, int low, int high) { // 定义函数/方法 partition
    int pivot = nums[high]; // 把 数组[high] 存入 pivot
    int i = low - 1; // 把 low 减 1 存入 下标 i
    for (int j = low; j < high; j++) { // 让 下标 j 从 low 开始计数，下标 j 小于 high 就继续
      if (nums[j] <= pivot) { // 若 数组[下标 j] 不超过 pivot
        i++; // 下标 i 加一
        swap(nums, i, j); // 交换 数组 与 下标 i, 下标 j
      }
    }
    swap(nums, i + 1, high); // 交换 数组 与 下标 i 加 1, high
    return i + 1; // 返回 下标 i 加 1
  }

  static void quickSort(int[] nums, int low, int high) { // 定义函数/方法 quickSort
    if (low < high) { // 若 low 小于 high
      int pi = partition(nums, low, high); // 把 partition(数组, low, high) 存入 pi
      quickSort(nums, low, pi - 1); // quickSort(数组, low, pi 减 1);
      quickSort(nums, pi + 1, high); // quickSort(数组, pi 加 1, high);
    }
  }

  static int[] quickSort(int[] nums) { // 定义函数/方法 quickSort
    if (nums.length > 0)
      quickSort(nums, 0, nums.length - 1); // 若 数组.长度 超过 0) quickSort(数组, 0, 数组.长度 减 1);
    return nums; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{3, 1, 2, 5, 4}, {1, 2, 3, 4, 5}},
      {{15, 4, 23, 52, 1}, {1, 4, 15, 23, 52}},
      {{1}, {1}},
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] in = c[0].clone(); // 把 字符[0].clone(); 写入 int[] in
      quickSort(in); // quickSort(in);
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
