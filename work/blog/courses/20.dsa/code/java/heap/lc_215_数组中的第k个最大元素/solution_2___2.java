// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
package com.webfault.dsa; // 引入依赖

import java.util.PriorityQueue; // 引入依赖

// 方案2: 自定义 MinHeap 封装（大小为 k 的小顶堆）
class Main { // 定义类型
  static class MinHeap { // static class MinHeap {
    private final PriorityQueue<Integer> heap = new PriorityQueue<>();

    int size() {
      return heap.size();
    } // int 大小() { return 堆.大小(); }

    int peak() {
      return heap.peek();
    } // int peak() { return 堆.peek(); }

    void insert(int val) {
      heap.offer(val);
    } // void insert(int 值) { 堆.offer(值); }

    int pop() {
      return heap.poll();
    } // int pop() { return 堆.poll(); }
  }

  static int findKthLargest(int[] nums, int k) { // 定义函数/方法 findKthLargest
    MinHeap h = new MinHeap(); // 把 new MinHeap(); 写入 MinHeap h
    for (int n : nums) { // for (int 元素个数 : 数组) {
      h.insert(n); // h 插入 元素个数);
      if (h.size() > k) { // 若 h.大小() 超过 下标 k
        h.pop(); // 弹出栈顶元素
      }
    }
    return h.peak(); // 返回 h.peak()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = {{3, 2, 1, 5, 6, 4}, {3, 2, 3, 1, 2, 4, 5, 5, 6}, {1}, {2, 1}, {5, 5, 5}};
    int[] ks = {2, 4, 1, 2, 2}; // 把 {2, 4, 1, 2, 2}; 写入 int[] ks
    int[] wants = {5, 4, 1, 1, 5}; // 把 {5, 4, 1, 1, 5}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < cases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
      int got = findKthLargest(cases[i], ks[i]); // 把 findKthLargest(cases[下标 i], ks[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL findKthLargest(case"
                + i
                + ", k="
                + ks[i]
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
