// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class CqA { // 定义类型
  int capacity; // int capacity;
  int[] data; // int[] data;
  int front; // int front;
  int rear; // int rear;
  int size; // int 大小;

  CqA(int k) { // CqA(int 下标 k) {
    capacity = k; // 把 下标 k; 写入 capacity
    data = new int[k]; // 把 new int[下标 k]; 写入 data
    front = 0; // 把 0; 写入 front
    rear = 0; // 把 0; 写入 rear
    size = 0; // 把 0; 写入 大小
  }

  boolean enQueue(int v) { // 定义函数/方法 enQueue
    if (isFull()) return false; // 若 isFull()，直接返回 false
    data[rear] = v; // 把 值; 写入 data[rear]
    rear = (rear + 1) % capacity; // 把 (rear 加 1) 对…取模 capacity; 写入 rear
    size++; // 大小 加一
    return true; // 返回 true
  }

  boolean deQueue() { // 定义函数/方法 deQueue
    if (isEmpty()) return false; // 若 isEmpty()，直接返回 false
    front = (front + 1) % capacity; // 把 (front 加 1) 对…取模 capacity; 写入 front
    size--; // 大小 减一
    return true; // 返回 true
  }

  int Front() {
    return isEmpty() ? -1 : data[front];
  } // int Front() { return isEmpty() ? 减 1 : data[front]; }

  int Rear() {
    return isEmpty() ? -1 : data[(rear - 1 + capacity) % capacity];
  }

  boolean isEmpty() {
    return size == 0;
  } // 把 赋值为 0; } 写入 boolean isEmpty() { return size

  boolean isFull() {
    return size == capacity;
  } // 把 赋值为 capacity; } 写入 boolean isFull() { return size

  public static void main(String[] args) { // public static void main(String[] args) {
    CqA q = new CqA(3); // 把 new CqA(3); 写入 CqA q
    List<Object> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Object> res
    res.add(q.enQueue(1)); // 结果 追加 节点.enQueue(1));
    res.add(q.enQueue(2)); // 结果 追加 节点.enQueue(2));
    res.add(q.enQueue(3)); // 结果 追加 节点.enQueue(3));
    res.add(q.enQueue(4)); // 结果 追加 节点.enQueue(4));
    res.add(q.Rear()); // 结果 追加 节点.Rear());
    res.add(q.isFull()); // 结果 追加 节点.isFull());
    res.add(q.deQueue()); // 结果 追加 节点.deQueue());
    res.add(q.enQueue(4)); // 结果 追加 节点.enQueue(4));
    res.add(q.Rear()); // 结果 追加 节点.Rear());
    List<Object> want = Arrays.asList(true, true, true, false, 3, true, true, true, 4);
    boolean ok = res.equals(want); // 把 结果.equals(want); 写入 boolean ok
    if (!ok) {
      System.out.println("FAIL got=" + res);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
