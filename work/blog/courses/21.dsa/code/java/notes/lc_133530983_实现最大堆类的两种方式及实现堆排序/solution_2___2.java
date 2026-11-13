// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc133B2 { // 定义类型
  static class MaxHeap { // static class MaxHeap {
    ArrayList<Integer> heap =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> heap

    static void swap(ArrayList<Integer> a, int i, int j) { // 定义函数/方法 swap
      if (i == j) return; // 若 下标 i 等于 下标 j) return;
      int t = a.get(i);
      a.set(i, a.get(j));
      a.set(j, t);
    }

    static void maxHeapify(ArrayList<Integer> a, int i, int size) { // 定义函数/方法 maxHeapify
      int l = (i << 1) + 1, r = (i << 1) + 2, largest = i;
      if (l < size && a.get(l) > a.get(largest))
        largest = l; // 若 左指针 小于 大小 且 数组 查找 左指针) 超过 数组 查找 largest)) largest 赋值为 左指针;
      if (r < size && a.get(r) > a.get(largest))
        largest = r; // 若 右指针 小于 大小 且 数组 查找 右指针) 超过 数组 查找 largest)) largest 赋值为 右指针;
      if (largest != i) {
        swap(a, i, largest);
        maxHeapify(a, largest, size);
      }
    }

    ArrayList<Integer> sort() { // 定义函数/方法 sort
      ArrayList<Integer> arr = heap; // 把 堆; 写入 ArrayList<Integer> arr
      int n = arr.size(); // 把 数组.大小() 存入 元素个数
      if (n <= 1) return arr; // 若 元素个数 不超过 1，直接返回 数组
      for (int i = n / 2 - 1; i >= 0; i--)
        maxHeapify(arr, i, n); // 让 下标 i 从 元素个数 除以 2 减 1 开始计数，下标 i 不低于 0 就继续
      for (int j = 0; j < n - 1; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 减 1 就继续
        swap(arr, 0, n - 1 - j); // 交换 数组 与 0, 元素个数 减 1 减 下标 j
        maxHeapify(arr, 0, n - 1 - j - 1); // maxHeapify(数组, 0, 元素个数 减 1 减 下标 j 减 1);
      }
      return arr; // 返回 数组
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc133B2 s = new Lc133B2(); // 把 new Lc133B2(); 写入 Lc133B2 s
    MaxHeap mh = new MaxHeap(); // 把 new MaxHeap(); 写入 MaxHeap mh
    mh.heap = new ArrayList<>(Arrays.asList(1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98));
    ArrayList<Integer> got = mh.sort(); // 排序
    ArrayList<Integer> want =
        new ArrayList<>(Arrays.asList(-1, 1, 1, 3, 3, 5, 9, 9, 10, 11, 11, 13, 98));
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!got.equals(want)) {
      ok = false;
      System.out.println("FAIL got " + got + " want " + want);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
