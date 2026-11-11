// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Node { // 定义类型
  int val; // int 值;
  Node left, right, next; // Node 左边界, 右边界, 下一个;

  Node() {} // Node() {}

  Node(int val) {
    this.val = val;
  } // 把 值; } 写入 值

  Node(int val, Node left, Node right) {
    this.val = val;
    this.left = left;
    this.right = right;
  } // 把 值; this.左边界 赋值为 左边界; this.右边界 赋值为 右边界; } 写入 值
}

class Solution { // 定义类型
  public Node connect(Node root) { // 定义函数/方法 connect
    if (root == null) return null; // 若 根节点 等于 null，直接返回 null
    Deque<Node> queue = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Node> queue
    queue.offer(root); // 队列.offer(根节点);
    while (!queue.isEmpty()) { // 循环，直到不满足「取反 队列.isEmpty(」
      int n = queue.size(); // 把 队列.大小() 存入 元素个数
      Node prev = null; // 把 null; 写入 Node prev
      for (int k = 0; k < n; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
        Node node = queue.poll(); // 把 队列.poll(); 写入 Node node
        if (prev != null) prev.next = node; // 若 前一个 不等于 null) 前一个.下一个 赋值为 节点;
        prev = node; // 把 节点; 写入 前一个
        if (node.left != null) queue.offer(node.left); // 若 节点.左边界 不等于 null) 队列.offer(节点.左边界);
        if (node.right != null) queue.offer(node.right); // 若 节点.右边界 不等于 null) 队列.offer(节点.右边界);
      }
    }
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    Node root = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3, null, new Node(7)));
    s.connect(root); // 字符串.connect(根节点);
    boolean ok = true; // 把 true; 写入 boolean ok
    if (root.left.next == null || root.left.next.val != 3) {
      ok = false;
      System.out.println("FAIL level1 next");
    }
    if (root.left.left.next == null || root.left.left.next.val != 5) {
      ok = false;
      System.out.println("FAIL level2 a");
    }
    if (root.left.left.next == null
        || root.left.left.next.next == null
        || root.left.left.next.next.val != 7) {
      ok = false;
      System.out.println("FAIL level2 b");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
