// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145346697
package com.webfault.dsa; // 引入依赖

import java.util.HashMap; // 引入依赖
import java.util.Map; // 引入依赖

class LFUCacheSol { // 定义类型
  static class Node { // static class Node {
    int key, value, freq; // int key, value, 频次表;
    Node prev, next; // Node 前一个, 下一个;

    Node(int k, int v) {
      key = k;
      value = v;
      freq = 1;
    }
  }

  static class DoublyLinkedList { // static class DoublyLinkedList {
    Node head = new Node(0, 0); // 把 new Node(0, 0); 写入 Node head
    Node tail = new Node(0, 0); // 把 new Node(0, 0); 写入 Node tail
    int size = 0; // 把 0 存入 大小

    DoublyLinkedList() {
      head.next = tail;
      tail.prev = head;
    } // 把 尾节点; 尾节点.前一个 赋值为 头节点; } 写入 下一个

    void add(Node node) { // 定义函数/方法 add
      node.prev = head; // 把 头节点; 写入 前一个
      node.next = head.next; // 把 头节点.下一个; 写入 下一个
      head.next.prev = node; // 把 节点; 写入 前一个
      head.next = node; // 把 节点; 写入 下一个
      size++; // 大小 加一
    }

    void remove(Node node) { // 定义函数/方法 remove
      node.prev.next = node.next; // 把 节点.下一个; 写入 下一个
      node.next.prev = node.prev; // 把 节点.前一个; 写入 前一个
      size--; // 大小 减一
    }

    Node removeLast() { // 定义函数/方法 removeLast
      if (size == 0) return null; // 若 大小 等于 0，直接返回 null
      Node node = tail.prev; // 把 尾节点.前一个; 写入 Node node
      remove(node); // remove(节点);
      return node; // 返回 节点
    }

    boolean isEmpty() {
      return size == 0;
    } // 把 赋值为 0; } 写入 boolean isEmpty() { return size
  }

  int capacity, size, minFreq; // int capacity, 大小, minFreq;
  Map<Integer, Node> keyToNode =
      new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Node> keyToNode
  Map<Integer, DoublyLinkedList> freqToList = new HashMap<>();

  LFUCacheSol(int capacity) {
    this.capacity = capacity;
    this.size = 0;
    this.minFreq = 0;
  }

  void updateFreq(Node node) { // 定义函数/方法 updateFreq
    int freq = node.freq; // 把 节点.频次表 存入 频次表
    DoublyLinkedList lst = freqToList.get(freq); // 把 freqToList 查找 频次表); 写入 DoublyLinkedList lst
    lst.remove(node); // lst 弹出 节点);
    if (lst.isEmpty()) { // 若 lst.isEmpty(
      freqToList.remove(freq); // freqToList 弹出 频次表);
      if (minFreq == freq) minFreq++; // 若 minFreq 等于 频次表) minFreq 加一 ;
    }
    node.freq++; // 节点.频次表 加一 ;
    if (!freqToList.containsKey(node.freq)) freqToList.put(node.freq, new DoublyLinkedList());
    freqToList.get(node.freq).add(node); // freqToList 查找 节点.频次表) 追加 节点);
  }

  int get(int key) { // 定义函数/方法 get
    if (!keyToNode.containsKey(key)) return -1; // 若 取反 keyToNode.containsKey(key)，直接返回 减 1
    Node node = keyToNode.get(key); // 把 keyToNode 查找 key); 写入 Node node
    updateFreq(node); // updateFreq(节点);
    return node.value; // 返回 节点.value
  }

  void put(int key, int value) { // 定义函数/方法 put
    if (capacity <= 0) return; // 若 capacity 不超过 0) return;
    if (keyToNode.containsKey(key)) { // 若 keyToNode.containsKey(key
      Node node = keyToNode.get(key); // 把 keyToNode 查找 key); 写入 Node node
      node.value = value; // 把 value; 写入 node.value
      updateFreq(node); // updateFreq(节点);
    } else { // 否则
      if (size >= capacity) { // 若 大小 不低于 capacity
        DoublyLinkedList minList =
            freqToList.get(minFreq); // 把 freqToList 查找 minFreq); 写入 DoublyLinkedList minList
        Node removed = minList.removeLast(); // 把 minList.removeLast(); 写入 Node removed
        if (removed != null) { // 若 removed 不等于 null
          keyToNode.remove(removed.key); // keyToNode 弹出 removed.key);
          size--; // 大小 减一
        }
      }
      Node node = new Node(key, value); // 把 new Node(key, value); 写入 Node node
      keyToNode.put(key, node); // keyToNode.put(key, 节点);
      if (!freqToList.containsKey(1)) freqToList.put(1, new DoublyLinkedList());
      freqToList.get(1).add(node); // freqToList 查找 1) 追加 节点);
      minFreq = 1; // 把 1; 写入 minFreq
      size++; // 大小 加一
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    LFUCacheSol lfu = new LFUCacheSol(2); // 把 new LFUCacheSol(2); 写入 LFUCacheSol lfu
    lfu.put(1, 1); // lfu.put(1, 1);
    lfu.put(2, 2); // lfu.put(2, 2);
    int[] got = new int[6]; // 把 new int[6]; 写入 int[] got
    got[0] = lfu.get(1); // 把 lfu 查找 1); 写入 got[0]
    lfu.put(3, 3); // lfu.put(3, 3);
    got[1] = lfu.get(2); // 把 lfu 查找 2); 写入 got[1]
    got[2] = lfu.get(3); // 把 lfu 查找 3); 写入 got[2]
    lfu.put(4, 4); // lfu.put(4, 4);
    got[3] = lfu.get(1); // 把 lfu 查找 1); 写入 got[3]
    got[4] = lfu.get(3); // 把 lfu 查找 3); 写入 got[4]
    got[5] = lfu.get(4); // 把 lfu 查找 4); 写入 got[5]
    int[] want = {1, -1, 3, -1, 3, 4}; // 把 {1, 减 1, 3, 减 1, 3, 4}; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < want.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL step " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
