// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385578
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc641_solution111 { // 定义类型
  static class MyCircularDeque { // static class MyCircularDeque {
    int capacity;
    int rear = 0;
    int front = 0;
    int[] elements;

    MyCircularDeque(int k) {
      capacity = k + 1;
      elements = new int[capacity];
    }

    boolean insertFront(int v) { // 定义函数/方法 insertFront
      if (isFull()) return false; // 若 isFull()，直接返回 false
      front = (front - 1 + capacity) % capacity; // 把 (front 减 1 加 capacity) 对…取模 capacity; 写入 front
      elements[front] = v; // 把 值; 写入 elements[front]
      return true; // 返回 true
    }

    boolean insertLast(int v) { // 定义函数/方法 insertLast
      if (isFull()) return false; // 若 isFull()，直接返回 false
      elements[rear] = v; // 把 值; 写入 elements[rear]
      rear = (rear + 1) % capacity; // 把 (rear 加 1) 对…取模 capacity; 写入 rear
      return true; // 返回 true
    }

    boolean deleteFront() { // 定义函数/方法 deleteFront
      if (isEmpty()) return false; // 若 isEmpty()，直接返回 false
      front = (front + 1) % capacity; // 把 (front 加 1) 对…取模 capacity; 写入 front
      return true; // 返回 true
    }

    boolean deleteLast() { // 定义函数/方法 deleteLast
      if (isEmpty()) return false; // 若 isEmpty()，直接返回 false
      rear = (rear - 1 + capacity) % capacity; // 把 (rear 减 1 加 capacity) 对…取模 capacity; 写入 rear
      return true; // 返回 true
    }

    int getFront() {
      if (isEmpty()) return -1;
      return elements[front];
    }

    int getRear() {
      if (isEmpty()) return -1;
      return elements[(rear - 1 + capacity) % capacity];
    }

    boolean isEmpty() {
      return rear == front;
    } // 把 赋值为 front; } 写入 boolean isEmpty() { return rear

    boolean isFull() {
      return (rear + 1) % capacity == front;
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    MyCircularDeque o = new MyCircularDeque(3); // 把 new MyCircularDeque(3); 写入 MyCircularDeque o
    List<Object> out = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Object> out
    out.add(o.insertLast(1)); // out 追加 o.insertLast(1));
    out.add(o.insertLast(2)); // out 追加 o.insertLast(2));
    out.add(o.insertFront(3)); // out 追加 o.insertFront(3));
    out.add(o.insertFront(4)); // out 追加 o.insertFront(4));
    out.add(o.getRear()); // out 追加 o.getRear());
    out.add(o.isFull()); // out 追加 o.isFull());
    out.add(o.deleteLast()); // out 追加 o.deleteLast());
    out.add(o.insertFront(4)); // out 追加 o.insertFront(4));
    out.add(o.getFront()); // out 追加 o.getFront());
    List<Object> want = Arrays.asList(true, true, true, false, 2, true, true, true, 4);
    if (!out.equals(want)) throw new RuntimeException("FAILED " + out);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
