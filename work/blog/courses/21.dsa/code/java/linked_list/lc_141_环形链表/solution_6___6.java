// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc141S6 { // 定义类型
  static class ListNode {
    int val;
    ListNode next;

    ListNode(int v) {
      val = v;
    }
  }

  static ListNode build(int[] vals, int pos) { // 定义函数/方法 build
    if (vals.length == 0) return null; // 若 vals.长度 等于 0，直接返回 null
    ListNode[] nodes = new ListNode[vals.length]; // 把 new ListNode[vals.长度]; 写入 ListNode[] nodes
    for (int i = 0; i < vals.length; i++)
      nodes[i] = new ListNode(vals[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 vals.长度 就继续
    for (int i = 0; i < vals.length - 1; i++)
      nodes[i].next = nodes[i + 1]; // 让 下标 i 从 0 开始计数，下标 i 小于 vals.长度 减 1 就继续
    if (pos >= 0 && vals.length > 0) nodes[vals.length - 1].next = nodes[pos];
    return nodes[0]; // 返回 nodes[0]
  }

  static boolean hasCycle(ListNode head) { // 定义函数/方法 hasCycle
    while (head != null && head.next != null) { // 循环，直到不满足「头节点 不等于 null 且 头节点.下一个 不等于 null」
      if (head.next == head) return true; // 若 头节点.下一个 等于 头节点，直接返回 true
      ListNode nxt = head.next; // 把 头节点.下一个; 写入 ListNode nxt
      head.next = head; // 把 头节点; 写入 下一个
      head = nxt; // 把 nxt; 写入 头节点
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc141S6 s = new Lc141S6(); // 把 new Lc141S6(); 写入 Lc141S6 s
    boolean[] got = { // 把 { 写入 boolean[] got
      s.hasCycle(build(new int[] {3, 2, 0, -4}, 1)),
      s.hasCycle(build(new int[] {1, 2}, 0)),
      s.hasCycle(build(new int[] {1}, -1)),
      s.hasCycle(null) // 字符串.hasCycle(null)
    };
    boolean[] want = {true, true, false, false}; // 把 {true, true, false, false}; 写入 boolean[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got[i] + " want " + want[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
