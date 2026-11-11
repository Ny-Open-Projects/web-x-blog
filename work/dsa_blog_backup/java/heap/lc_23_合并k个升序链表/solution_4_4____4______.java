// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc23 { // 定义类型
  static class ListNode {
    int val;
    ListNode next;

    ListNode(int v) {
      val = v;
    }
  }

  ListNode mergeKLists(ListNode[] lists) { // 定义函数/方法 mergeKLists
    ListNode res = new ListNode(0);
    ListNode p = res; // 把 new ListNode(0); ListNode 节点 赋值为 结果; 写入 ListNode res
    PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    for (ListNode l : lists)
      if (l != null) pq.offer(l); // 把 null) 优先队列.offer(左指针); 写入 for(ListNode l: lists) if(l!
    while (!pq.isEmpty()) { // 循环，直到不满足「取反 优先队列.isEmpty(」
      ListNode n = pq.poll(); // 把 优先队列.poll(); 写入 ListNode n
      p.next = n;
      p = n; // 把 元素个数; 节点 赋值为 元素个数; 写入 下一个
      if (n.next != null) pq.offer(n.next); // 若 元素个数.下一个 不等于 null) 优先队列.offer(元素个数.下一个);
    }
    return res.next; // 返回 结果.下一个
  }

  ListNode build(int[] vals) {
    ListNode d = new ListNode(0), c = d;
    for (int v : vals) {
      c.next = new ListNode(v);
      c = c.next;
    }
    return d.next;
  }

  List<Integer> toList(ListNode n) {
    List<Integer> r = new ArrayList<>();
    while (n != null) {
      r.add(n.val);
      n = n.next;
    }
    return r;
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc23 s = new Lc23(); // 把 new Lc23(); 写入 Lc23 s
    ListNode[] lists = {
      s.build(new int[] {1, 4, 5}), s.build(new int[] {1, 3, 4}), s.build(new int[] {2, 6})
    };
    List<Integer> got =
        s.toList(
            s.mergeKLists(lists)); // 把 字符串.toList(字符串.mergeKLists(lists)); 写入 List<Integer> got
    List<Integer> want =
        Arrays.asList(
            1, 1, 2, 3, 4, 4, 5, 6); // 把 Arrays.asList(1,1,2,3,4,4,5,6); 写入 List<Integer> want
    boolean ok = true; // 把 true; 写入 boolean ok
    if (got.size() != want.size()) ok = false; // 若 got.大小() 不等于 want.大小()) ok 赋值为 false;
    else
      for (int i = 0; i < want.size(); i++) if (!got.get(i).equals(want.get(i))) ok = false; // 否则
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
