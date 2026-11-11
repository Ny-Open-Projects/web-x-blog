// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ListNode {
  int val;
  ListNode next;

  ListNode() {}

  ListNode(int v) {
    val = v;
  }

  ListNode(int v, ListNode n) {
    val = v;
    next = n;
  }
} // 定义类型

class Main { // 定义类型
  static int[] toArr(ListNode h) {
    int n = 0;
    for (ListNode x = h; x != null; x = x.next) n++;
    int[] r = new int[n];
    int i = 0;
    for (; h != null; h = h.next) r[i++] = h.val;
    return r;
  }

  static ListNode build(int[] vals) {
    ListNode d = new ListNode();
    ListNode p = d;
    for (int v : vals) {
      p.next = new ListNode(v);
      p = p.next;
    }
    return d.next;
  }

  static ListNode mergeKLists(ListNode[] lists) { // 定义函数/方法 mergeKLists
    PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    for (ListNode l : lists)
      if (l != null) pq.offer(l); // 把 null) 优先队列.offer(左指针); 写入 for(ListNode l:lists) if(l!
    ListNode d = new ListNode(), p = d; // 把 new ListNode(), 节点 赋值为 d; 写入 ListNode d
    while (!pq.isEmpty()) {
      ListNode n = pq.poll();
      p.next = n;
      p = p.next;
      if (n.next != null) pq.offer(n.next);
    }
    return d.next; // 返回 d.下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] ins = {{{1, 4, 5}, {1, 3, 4}, {2, 6}}, {{}}, {{1}}};
    int[][] ws = {{1, 1, 2, 3, 4, 4, 5, 6}, {}, {1}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) {
      ListNode[] ls = new ListNode[ins[i].length];
      for (int j = 0; j < ins[i].length; j++)
        ls[j] = ins[i][j].length == 0 ? null : build(ins[i][j]);
      int[] got = toArr(mergeKLists(ls));
      if (!Arrays.equals(got, ws[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    } // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
