// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc295_solution222 { // 定义类型
  static class Heap { // static class Heap {
    List<Integer> heap = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> heap
    Comparator<Integer> cmp; // Comparator 小于 Integer 超过 cmp;

    Heap(Comparator<Integer> cmp) {
      this.cmp = cmp;
    } // 把 cmp; } 写入 Heap(Comparator<Integer> cmp) { this.cmp

    int size() {
      return heap.size();
    } // int 大小() { return 堆.大小(); }

    Integer peek() {
      return heap.isEmpty() ? null : heap.get(0);
    } // Integer peek() { return 堆.isEmpty() ? null : 堆 查找 0); }

    void insert(int value) {
      heap.add(value);
      shiftUp(heap.size() - 1);
    } // void insert(int value) { 堆 追加 value); shiftUp(堆.大小() 减 1); }

    int pop() { // 定义函数/方法 pop
      int first = heap.get(0); // 把 堆 查找 0) 存入 first
      int last = heap.remove(heap.size() - 1); // 把 堆 弹出 堆.大小() 减 1) 存入 last
      if (!heap.isEmpty()) {
        heap.set(0, last);
        shiftDown(0);
      } // 若 取反 堆.isEmpty()) { 堆.set(0, last); shiftDown(0); }
      return first; // 返回 first
    }

    void shiftUp(int i) { // 定义函数/方法 shiftUp
      while (i > 0) { // 循环，直到不满足「下标 i 超过 0」
        int p = (i - 1) >> 1; // 把 (下标 i 减 1) 超过 超过 1 存入 节点
        if (cmp.compare(heap.get(p), heap.get(i)) > 0) { // 若 cmp.compare(堆 查找 节点), 堆 查找 下标 i)) 超过 0
          Collections.swap(heap, p, i); // Collections.交换 堆, 节点, 下标 i);
          i = p; // 把 节点; 写入 下标 i
        } else break; // 否则
      }
    }

    void shiftDown(int pi) { // 定义函数/方法 shiftDown
      int size = heap.size(); // 把 堆.大小() 存入 大小
      while (true) { // 循环，直到不满足「true」
        int left = 2 * pi + 1,
            right = 2 * pi + 2,
            largest = pi; // 把 2 乘 pi 加 1, 右边界 赋值为 2 乘 pi 加 2, largest 赋值为 pi 存入 左边界
        if (left < size && cmp.compare(heap.get(largest), heap.get(left)) > 0) largest = left;
        if (right < size && cmp.compare(heap.get(largest), heap.get(right)) > 0) largest = right;
        if (largest != pi) {
          Collections.swap(heap, pi, largest);
          pi = largest;
        } else break; // 否则
      }
    }
  }

  static class MinHeap extends Heap { // static class MinHeap extends Heap {
    MinHeap() {
      super((a, b) -> Integer.compare(a, b));
    } // MinHeap() { super((数组, b) 减 超过 Integer.compare(数组, b)); }
  }

  static class MaxHeap extends Heap { // static class MaxHeap extends Heap {
    MaxHeap() {
      super((a, b) -> Integer.compare(b, a));
    } // MaxHeap() { super((数组, b) 减 超过 Integer.compare(b, 数组)); }
  }

  static class MedianFinder { // static class MedianFinder {
    MinHeap minHeap = new MinHeap(); // 把 new MinHeap(); 写入 MinHeap minHeap
    MaxHeap maxHeap = new MaxHeap(); // 把 new MaxHeap(); 写入 MaxHeap maxHeap

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
