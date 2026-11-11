// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468244
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc133468244_solution22 { // 定义类型
  static class MinHeap { // static class MinHeap {
    List<Integer> heap = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> heap

    int parent(int i) {
      return (i - 1) >> 1;
    } // int parent(int 下标 i) { return (下标 i 减 1) 超过 超过 1; }

    int left(int i) {
      return (i << 1) + 1;
    } // int 左边界(int 下标 i) { return (下标 i 小于 小于 1) 加 1; }

    int right(int i) {
      return (i << 1) + 2;
    } // int 右边界(int 下标 i) { return (下标 i 小于 小于 1) 加 2; }

    void swap(int i, int j) { // 定义函数/方法 swap
      int t = heap.get(i);
      heap.set(i, heap.get(j));
      heap.set(j, t);
    }

    void shiftUp(int i) { // 定义函数/方法 shiftUp
      if (i == 0) return; // 若 下标 i 等于 0) return;
      int pi = parent(i); // 把 parent(下标 i) 存入 pi
      if (heap.get(pi) > heap.get(i)) { // 若 堆 查找 pi) 超过 堆 查找 下标 i
        swap(pi, i); // 交换 pi 与 下标 i
        shiftUp(pi); // shiftUp(pi);
      }
    }

    void shiftDown(int i) { // 定义函数/方法 shiftDown
      int size = heap.size(); // 把 堆.大小() 存入 大小
      int li = left(i),
          ri = right(i),
          smallest = i; // 把 左边界(下标 i), ri 赋值为 右边界(下标 i), smallest 赋值为 下标 i 存入 li
      if (li < size && heap.get(li) < heap.get(i))
        smallest = li; // 若 li 小于 大小 且 堆 查找 li) 小于 堆 查找 下标 i)) smallest 赋值为 li;
      if (ri < size && heap.get(ri) < heap.get(smallest))
        smallest = ri; // 若 ri 小于 大小 且 堆 查找 ri) 小于 堆 查找 smallest)) smallest 赋值为 ri;
      if (smallest != i) { // 若 smallest 不等于 下标 i
        swap(smallest, i); // 交换 smallest 与 下标 i
        shiftDown(smallest); // shiftDown(smallest);
      }
    }

    void insert(int v) { // 定义函数/方法 insert
      heap.add(v); // 堆 追加 值);
      shiftUp(heap.size() - 1); // shiftUp(堆.大小() 减 1);
    }

    void pop() { // 定义函数/方法 pop
      if (heap.isEmpty()) return; // 若 堆.isEmpty()) return;
      heap.set(0, heap.remove(heap.size() - 1)); // 堆.set(0, 堆 弹出 堆.大小() 减 1));
      shiftDown(0); // shiftDown(0);
    }

    Integer peak() {
      return heap.isEmpty() ? null : heap.get(0);
    } // Integer peak() { return 堆.isEmpty() ? null : 堆 查找 0); }

    int size() {
      return heap.size();
    } // int 大小() { return 堆.大小(); }
  }

  static void assertEq(List<Integer> a, int[] b) { // 定义函数/方法 assertEq
    if (a.size() != b.length) throw new RuntimeException("FAILED size " + a.size());
    for (int i = 0; i < b.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 b.长度 就继续
      if (a.get(i) != b[i]) throw new RuntimeException("FAILED at " + i + " got " + a.get(i));
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    MinHeap heap = new MinHeap(); // 把 new MinHeap(); 写入 MinHeap heap
    for (int v : new int[] {3, 1, 6, 5, 2, 4})
      heap.insert(v); // for (int 值 : new int[]{3, 1, 6, 5, 2, 4}) 堆 插入 值);
    assertEq(heap.heap, new int[] {1, 2, 4, 5, 3, 6}); // 断言校验
    if (heap.peak() != 1)
      throw new RuntimeException(
          "FAILED peek"); // 若 堆.peak() 不等于 1) throw new RuntimeException(「FAILED peek」);
    heap.pop(); // 弹出栈顶元素
    assertEq(heap.heap, new int[] {2, 3, 4, 5, 6}); // 断言校验
    heap.pop(); // 弹出栈顶元素
    assertEq(heap.heap, new int[] {3, 5, 4, 6}); // 断言校验
    if (heap.size() != 4)
      throw new RuntimeException(
          "FAILED size2"); // 若 堆.大小() 不等于 4) throw new RuntimeException(「FAILED size2」);
    MinHeap empty = new MinHeap(); // 把 new MinHeap(); 写入 MinHeap empty
    if (empty.peak() != null) throw new RuntimeException("FAILED empty peek");
    empty.pop(); // 弹出栈顶元素
    if (empty.size() != 0) throw new RuntimeException("FAILED empty size");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
