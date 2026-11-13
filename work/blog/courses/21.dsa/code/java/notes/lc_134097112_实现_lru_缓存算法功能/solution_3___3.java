// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class LruS3 { // 定义类型
  static class Node { // static class Node {
    int key, value; // int key, value;
    Node prev, next; // Node 前一个, 下一个;

    Node() {} // Node() {}

    Node(int k, int v) {
      key = k;
      value = v;
    } // 把 下标 k; value 赋值为 值; } 写入 Node(int k, int v) { key
  }

  static class LRUCache { // static class LRUCache {
    int capacity; // int capacity;
    Map<Integer, Node> data = new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Node> data
    Node head = new Node(), tail = new Node(); // 把 new Node(), 尾节点 赋值为 new Node(); 写入 Node head

    LRUCache(int c) { // LRUCache(int 字符) {
      capacity = c; // 把 字符; 写入 capacity
      head.next = tail;
      tail.prev = head; // 把 尾节点; 尾节点.前一个 赋值为 头节点; 写入 下一个
    }

    void remove(Node n) {
      n.prev.next = n.next;
      n.next.prev = n.prev;
    } // 把 元素个数.下一个; 元素个数.下一个.前一个 赋值为 元素个数.前一个; } 写入 下一个

    void addToTail(Node n) { // 定义函数/方法 addToTail
      n.prev = tail.prev;
      n.next = tail; // 把 尾节点.前一个; 元素个数.下一个 赋值为 尾节点; 写入 前一个
      tail.prev.next = n;
      tail.prev = n; // 把 元素个数; 尾节点.前一个 赋值为 元素个数; 写入 下一个
    }

    void set(int key, int value) { // 定义函数/方法 set
      if (data.containsKey(key))
        remove(data.get(key)); // 若 data.containsKey(key)) remove(data 查找 key));
      Node node = new Node(key, value); // 把 new Node(key, value); 写入 Node node
      data.put(key, node); // data.put(key, 节点);
      addToTail(node); // addToTail(节点);
      if (data.size() > capacity) { // 若 data.大小() 超过 capacity
        Node lru = head.next; // 把 头节点.下一个; 写入 Node lru
        remove(lru); // remove(lru);
        data.remove(lru.key); // data 弹出 lru.key);
      }
    }

    Integer get(int key) { // 定义函数/方法 get
      if (!data.containsKey(key)) return null; // 若 取反 data.containsKey(key)，直接返回 null
      Node node = data.get(key); // 把 data 查找 key); 写入 Node node
      remove(node); // remove(节点);
      addToTail(node); // addToTail(节点);
      return node.value; // 返回 节点.value
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    LRUCache c = new LRUCache(2); // 把 new LRUCache(2); 写入 LRUCache c
    c.set(1, 1);
    c.set(2, 2); // 字符.set(1, 1); 字符.set(2, 2);
    Integer[] got = new Integer[5]; // 把 new Integer[5]; 写入 Integer[] got
    got[0] = c.get(1); // 把 字符 查找 1); 写入 got[0]
    c.set(3, 3); // 字符.set(3, 3);
    got[1] = c.get(2); // 把 字符 查找 2); 写入 got[1]
    c.set(4, 4); // 字符.set(4, 4);
    got[2] = c.get(1); // 把 字符 查找 1); 写入 got[2]
    got[3] = c.get(3); // 把 字符 查找 3); 写入 got[3]
    got[4] = c.get(4); // 把 字符 查找 4); 写入 got[4]
    Integer[] want = {1, null, null, 3, 4}; // 把 { 1, null, null, 3, 4 }; 写入 Integer[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    if (got.length != want.length) ok = false; // 若 got.长度 不等于 want.长度) ok 赋值为 false;
    else
      for (int i = 0; i < got.length; i++) { // 否则
        if (got[i] == null ? want[i] != null : !got[i].equals(want[i])) {
          ok = false; // 把 false; 写入 ok
          System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
        }
      }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
