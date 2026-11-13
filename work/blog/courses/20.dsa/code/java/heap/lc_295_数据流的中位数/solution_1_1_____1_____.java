// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc295_solution111 { // 定义类型
  static class MinHeap { // static class MinHeap {
    PriorityQueue<Integer> heap =
        new PriorityQueue<>(); // 把 new PriorityQueue 小于 超过 (); 写入 PriorityQueue<Integer> heap

    int size() {
      return heap.size();
    } // int 大小() { return 堆.大小(); }

    Integer peek() {
      return heap.peek();
    } // Integer peek() { return 堆.peek(); }

    void insert(int val) {
      heap.offer(val);
    } // void insert(int 值) { 堆.offer(值); }

    int pop() {
      return heap.poll();
    } // int pop() { return 堆.poll(); }
  }

  static class MaxHeap { // static class MaxHeap {
    PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());

    int size() {
      return heap.size();
    } // int 大小() { return 堆.大小(); }

    Integer peek() {
      return heap.peek();
    } // Integer peek() { return 堆.peek(); }

    void insert(int val) {
      heap.offer(val);
    } // void insert(int 值) { 堆.offer(值); }

    int pop() {
      return heap.poll();
    } // int pop() { return 堆.poll(); }
  }

  static class MedianFinder { // static class MedianFinder {
    MaxHeap maxHeap = new MaxHeap(); // 把 new MaxHeap(); 写入 MaxHeap maxHeap
    MinHeap minHeap = new MinHeap(); // 把 new MinHeap(); 写入 MinHeap minHeap

    void addNum(int num) { // 定义函数/方法 addNum
      if (maxHeap.size() == 0
          || num <= maxHeap.peek()) { // 若 maxHeap.大小() 等于 0 或 num 不超过 maxHeap.peek(
        maxHeap.insert(num); // maxHeap 插入 num);
      } else { // 否则
        minHeap.insert(num); // minHeap 插入 num);
      }
      if (maxHeap.size() > minHeap.size() + 1) { // 若 maxHeap.大小() 超过 minHeap.大小() 加 1
        minHeap.insert(maxHeap.pop()); // 弹出栈顶元素
      } else if (minHeap.size() > maxHeap.size()) { // 否则，若 minHeap.大小() 超过 maxHeap.大小(
        maxHeap.insert(minHeap.pop()); // 弹出栈顶元素
      }
    }

    double findMedian() { // 定义函数/方法 findMedian
      if (maxHeap.size() == minHeap.size()) { // 若 maxHeap.大小() 等于 minHeap.大小(
        return (maxHeap.peek() + minHeap.peek())
            / 2.0; // 返回 (maxHeap.peek() 加 minHeap.peek()) 除以 2.0
      }
      return maxHeap.peek(); // 返回 maxHeap.peek()
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    MedianFinder mf = new MedianFinder(); // 把 new MedianFinder(); 写入 MedianFinder mf
    for (int x : new int[] {1, 2, 3, 4, 5})
      mf.addNum(x); // for (int x : new int[]{1, 2, 3, 4, 5}) mf.addNum(x);
    double got = mf.findMedian(); // 把 mf.findMedian() 存入 got
    if (got != 3.0) throw new RuntimeException("FAILED: got " + got + " want 3.0");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
