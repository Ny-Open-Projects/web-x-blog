// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094527
package com.webfault.dsa; // 引入依赖

import java.util.HashMap; // 引入依赖

class LRUCacheSol2 { // 定义类型
  static class DLinkedNode { // static class DLinkedNode {
    int key, value; // int key, value;
    DLinkedNode prev, next; // DLinkedNode 前一个, 下一个;

    DLinkedNode() { // DLinkedNode() {
    }

    DLinkedNode(int k, int v) { // DLinkedNode(int 下标 k, int 值) {
      key = k; // 把 下标 k; 写入 key
      value = v; // 把 值; 写入 value
    }
  }

  static class LRUCache { // static class LRUCache {
    int capacity, size; // int capacity, 大小;
    DLinkedNode head, tail; // DLinkedNode 头节点, 尾节点;
    HashMap<Integer, DLinkedNode> cache = new HashMap<Integer, DLinkedNode>();

    LRUCache(int c) { // LRUCache(int 字符) {
      capacity = c; // 把 字符; 写入 capacity
      size = 0; // 把 0; 写入 大小
      head = new DLinkedNode(); // 把 new DLinkedNode(); 写入 头节点
      tail = new DLinkedNode(); // 把 new DLinkedNode(); 写入 尾节点
      head.next = tail; // 把 尾节点; 写入 下一个
      tail.prev = head; // 把 头节点; 写入 前一个
    }

    void addToHead(DLinkedNode n) { // 定义函数/方法 addToHead
      n.prev = head; // 把 头节点; 写入 前一个
      n.next = head.next; // 把 头节点.下一个; 写入 下一个
      head.next.prev = n; // 把 元素个数; 写入 前一个
      head.next = n; // 把 元素个数; 写入 下一个
    }

    void removeNode(DLinkedNode n) { // 定义函数/方法 removeNode
      n.prev.next = n.next; // 把 元素个数.下一个; 写入 下一个
      n.next.prev = n.prev; // 把 元素个数.前一个; 写入 前一个
    }

    void moveToHead(DLinkedNode n) { // 定义函数/方法 moveToHead
      removeNode(n); // removeNode(元素个数);
      addToHead(n); // addToHead(元素个数);
    }

    DLinkedNode removeTail() { // 定义函数/方法 removeTail
      DLinkedNode n = tail.prev; // 把 尾节点.前一个; 写入 DLinkedNode n
      removeNode(n); // removeNode(元素个数);
      return n; // 返回 元素个数
    }

    int get(int k) { // 定义函数/方法 get
      if (!cache.containsKey(k)) return -1; // 若 取反 cache.containsKey(下标 k)，直接返回 减 1
      DLinkedNode n = cache.get(k); // 把 cache 查找 下标 k); 写入 DLinkedNode n
      moveToHead(n); // moveToHead(元素个数);
      return n.value; // 返回 元素个数.value
    }

    void put(int k, int v) { // 定义函数/方法 put
      if (!cache.containsKey(k)) { // 若 取反 cache.containsKey(下标 k
        DLinkedNode node = new DLinkedNode(k, v); // 把 new DLinkedNode(下标 k, 值); 写入 DLinkedNode node
        cache.put(k, node); // cache.put(下标 k, 节点);
        addToHead(node); // addToHead(节点);
        size++; // 大小 加一
        if (size > capacity) { // 若 大小 超过 capacity
          DLinkedNode removed = removeTail(); // 把 removeTail(); 写入 DLinkedNode removed
          cache.remove(removed.key); // cache 弹出 removed.key);
          size--; // 大小 减一
        }
      } else { // 否则
        DLinkedNode n = cache.get(k); // 把 cache 查找 下标 k); 写入 DLinkedNode n
        n.value = v; // 把 值; 写入 n.value
        moveToHead(n); // moveToHead(元素个数);
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    LRUCache c = new LRUCache(2); // 把 new LRUCache(2); 写入 LRUCache c
    c.put(1, 1); // 字符.put(1, 1);
    c.put(2, 2); // 字符.put(2, 2);
    int g1 = c.get(1); // 把 字符 查找 1) 存入 g1
    c.put(3, 3); // 字符.put(3, 3);
    int g2 = c.get(2); // 把 字符 查找 2) 存入 g2
    c.put(4, 4); // 字符.put(4, 4);
    int g3 = c.get(1); // 把 字符 查找 1) 存入 g3
    int g4 = c.get(3); // 把 字符 查找 3) 存入 g4
    int g5 = c.get(4); // 把 字符 查找 4) 存入 g5
    int[] got = {g1, g2, g3, g4, g5}; // 把 {g1, g2, g3, g4, g5}; 写入 int[] got
    int[] want = {1, -1, -1, 3, 4}; // 把 {1, 减 1, 减 1, 3, 4}; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
