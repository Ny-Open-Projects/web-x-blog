// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Node {
  int val;
  Node left;
  Node right;
  Node next;

  Node() {}

  Node(int v) {
    val = v;
  }

  Node(int v, Node l, Node r, Node n) {
    val = v;
    left = l;
    right = r;
    next = n;
  }
} // 定义类型

class Main { // 定义类型
  static Node connect(Node root) { // 定义函数/方法 connect
    if (root == null) return null; // 若 根节点 等于 null，直接返回 null
    LinkedList<Node> q = new LinkedList<>();
    q.add(root); // 把 new LinkedList 小于 超过 (); 节点 追加 根节点); 写入 LinkedList<Node> q
    while (!q.isEmpty()) {
      int n = q.size();
      Node prev = null;
      for (int k = 0; k < n; k++) {
        Node x = q.poll();
        if (prev != null) prev.next = x;
        prev = x;
        if (x.left != null) q.add(x.left);
        if (x.right != null) q.add(x.right);
      }
    } // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    return root; // 返回 根节点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Node n1 = new Node(1);
    n1.left = new Node(2);
    n1.right = new Node(3);
    n1.left.left = new Node(4);
    n1.left.right = new Node(5);
    n1.right.left = new Node(6);
    n1.right.right = new Node(7);
    connect(n1); // connect(n1);
    // level2 next chain: 2->3 ; level3: 4->5->6->7
    if (n1.left.next != n1.right) {
      System.out.println("FAIL lvl2");
      throw new RuntimeException("FAILED");
    }
    if (n1.left.left.next != n1.left.right
        || n1.left.right.next != n1.right.left
        || n1.right.left.next != n1.right.right) {
      System.out.println("FAIL lvl3");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
