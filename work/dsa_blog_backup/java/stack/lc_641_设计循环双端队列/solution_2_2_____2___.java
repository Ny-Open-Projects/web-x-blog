// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385578
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc641_solution222 { // 定义类型
  static class Node { // static class Node {
    int val;
    Node prev;
    Node next; // int 值; Node 前一个; Node 下一个;

    Node(int v) {
      val = v;
    } // 把 值; } 写入 Node(int v) { val
  }

  static class MyCircularDeque { // static class MyCircularDeque {
    Node head = null, tail = null; // 把 null, 尾节点 赋值为 null; 写入 Node head
    int capacity;
    int size = 0; // 把 0; 写入 int capacity; int size

    MyCircularDeque(int k) {
      capacity = k;
    } // 把 下标 k; } 写入 MyCircularDeque(int k) { capacity

    boolean insertFront(int v) { // 定义函数/方法 insertFront
      if (isFull()) return false; // 若 isFull()，直接返回 false
      Node n = new Node(v); // 把 new Node(值); 写入 Node n
      if (isEmpty()) {
        head = n;
        tail = n;
      } // 若 isEmpty()) { 头节点 赋值为 元素个数; 尾节点 赋值为 元素个数; }
      else {
        n.next = head;
        head.prev = n;
        head = n;
      } // 否则
      size++;
      return true; // 大小 加一 ; return true;
    }

    boolean insertLast(int v) { // 定义函数/方法 insertLast
      if (isFull()) return false; // 若 isFull()，直接返回 false
      Node n = new Node(v); // 把 new Node(值); 写入 Node n
      if (isEmpty()) {
        head = n;
        tail = n;
      } // 若 isEmpty()) { 头节点 赋值为 元素个数; 尾节点 赋值为 元素个数; }
      else {
        tail.next = n;
        n.prev = tail;
        tail = n;
      } // 否则
      size++;
      return true; // 大小 加一 ; return true;
    }

    boolean deleteFront() { // 定义函数/方法 deleteFront
      if (isEmpty()) return false; // 若 isEmpty()，直接返回 false
      head = head.next; // 把 头节点.下一个; 写入 头节点
      if (head != null) head.prev = null;
      else tail = null; // 若 头节点 不等于 null) 头节点.前一个 赋值为 null; else 尾节点 赋值为 null;
      size--;
      return true; // 大小 减一 ; return true;
    }

    boolean deleteLast() { // 定义函数/方法 deleteLast
      if (isEmpty()) return false; // 若 isEmpty()，直接返回 false
      tail = tail.prev; // 把 尾节点.前一个; 写入 尾节点
      if (tail != null) tail.next = null;
      else head = null; // 若 尾节点 不等于 null) 尾节点.下一个 赋值为 null; else 头节点 赋值为 null;
      size--;
      return true; // 大小 减一 ; return true;
    }

    int getFront() {
      if (isEmpty()) return -1;
      return head.val;
    } // int getFront() { if (isEmpty()) return 减 1; return 头节点.值; }

    int getRear() {
      if (isEmpty()) return -1;
      return tail.val;
    } // int getRear() { if (isEmpty()) return 减 1; return 尾节点.值; }

    boolean isEmpty() {
      return size == 0;
    } // 把 赋值为 0; } 写入 boolean isEmpty() { return size

    boolean isFull() {
      return size == capacity;
    } // 把 赋值为 capacity; } 写入 boolean isFull() { return size
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
