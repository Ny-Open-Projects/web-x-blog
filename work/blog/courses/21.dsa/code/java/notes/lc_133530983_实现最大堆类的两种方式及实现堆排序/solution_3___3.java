// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc133A3 { // 定义类型
  static class MaxHeap { // static class MaxHeap {
    ArrayList<Integer> heap =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> heap

    void swap(int i, int j) {
      int t = heap.get(i);
      heap.set(i, heap.get(j));
      heap.set(j, t);
    }

    int parent(int i) {
      return (i - 1) >> 1;
    } // int parent(int 下标 i) { return (下标 i 减 1) 超过 超过 1; }

    int left(int i) {
      return (i << 1) + 1;
    } // int 左边界(int 下标 i) { return (下标 i 小于 小于 1) 加 1; }

    int right(int i) {
      return (i << 1) + 2;
    } // int 右边界(int 下标 i) { return (下标 i 小于 小于 1) 加 2; }

    void shiftUp(int idx) { // 定义函数/方法 shiftUp
      if (idx == 0) return; // 若 idx 等于 0) return;
      int p = parent(idx); // 把 parent(idx) 存入 节点
      if (heap.get(p) < heap.get(idx)) {
        swap(p, idx);
        shiftUp(p);
      } // 若 堆 查找 节点) 小于 堆 查找 idx)) { 交换 节点, idx); shiftUp(节点); }
    }

    void shiftDown(int idx) { // 定义函数/方法 shiftDown
      if (idx >= heap.size() - 1) return; // 若 idx 不低于 堆.大小() 减 1) return;
      int size = heap.size(); // 把 堆.大小() 存入 大小
      int l = left(idx), r = right(idx); // 把 左边界(idx), 右指针 赋值为 右边界(idx) 存入 左指针
      if (l < size && heap.get(l) > heap.get(idx)) {
        swap(l, idx);
        shiftDown(l);
      }
      if (r < size && heap.get(r) > heap.get(idx)) {
        swap(r, idx);
        shiftDown(r);
      }
    }

    void insert(int v) {
      heap.add(v);
      shiftUp(heap.size() - 1);
    } // void insert(int 值) { 堆 追加 值); shiftUp(堆.大小() 减 1); }

    void pop() { // 定义函数/方法 pop
      if (heap.size() <= 1) return; // 若 堆.大小() 不超过 1) return;
      heap.set(0, heap.remove(heap.size() - 1)); // 堆.set(0, 堆 弹出 堆.大小() 减 1));
      shiftDown(0); // shiftDown(0);
    }

    int peak() {
      return heap.get(0);
    } // int peak() { return 堆 查找 0); }

    int size() {
      return heap.size();
    } // int 大小() { return 堆.大小(); }

    ArrayList<Integer> sort(int[] arr) { // 定义函数/方法 sort
      for (int n : arr) insert(n); // for (int 元素个数 : 数组) insert(元素个数);
      ArrayList<Integer> result =
          new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> result
      while (size() > 1) {
        result.add(peak());
        pop();
      } // 循环，直到不满足「大小() 超过 1) { 结果 追加 peak()); pop(); }」
      result.add(peak()); // 结果 追加 peak());
      return result; // 返回 结果
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc133A3 s = new Lc133A3(); // 把 new Lc133A3(); 写入 Lc133A3 s
    MaxHeap mh = new MaxHeap(); // 把 new MaxHeap(); 写入 MaxHeap mh
    ArrayList<Integer> got = mh.sort(new int[] {1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98}); // 排序
    ArrayList<Integer> want =
        new ArrayList<>(Arrays.asList(98, 13, 11, 11, 10, 9, 9, 5, 3, 3, 1, 1, -1));
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!got.equals(want)) {
      ok = false;
      System.out.println("FAIL got " + got + " want " + want);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
