// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130508569
package com.webfault.dsa; // 引入依赖

class lc237 { // 定义类型
  static class ListNode {
    int val;
    ListNode next;

    ListNode(int v) {
      val = v;
    }
  }

  void deleteNode(ListNode node) { // 定义函数/方法 deleteNode
    if (node != null && node.next != null) { // 若 节点 不等于 null 且 节点.下一个 不等于 null
      node.val = node.next.val; // 把 节点.下一个.值; 写入 值
      node.next = node.next.next; // 把 节点.下一个.下一个; 写入 下一个
    }
  }

  static ListNode build(int[] a) { // 定义函数/方法 build
    ListNode dummy = new ListNode(0);
    ListNode cur = dummy; // 把 new ListNode(0); ListNode 当前值 赋值为 哨兵节点; 写入 ListNode dummy
    for (int v : a) {
      cur.next = new ListNode(v);
      cur = cur.next;
    } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  static java.util.ArrayList<Integer> toList(ListNode head) {
    java.util.ArrayList<Integer> res = new java.util.ArrayList<Integer>();
    while (head != null) {
      res.add(head.val);
      head = head.next;
    } // 循环，直到不满足「头节点 不等于 null) { 结果 追加 头节点.值); 头节点 赋值为 头节点.下一个; }」
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc237 s = new lc237(); // 把 new lc237(); 写入 lc237 s
    ListNode h1 = build(new int[] {4, 5, 1, 9}); // 把 build(new int[]{4, 5, 1, 9}); 写入 ListNode h1
    ListNode target = h1.next; // 把 h1.下一个; 写入 ListNode target
    s.deleteNode(target); // 字符串.deleteNode(目标值);
    java.util.ArrayList<Integer> got1 =
        toList(h1); // 把 toList(h1); 写入 java.util.ArrayList<Integer> got1
    if (got1.size() != 3 || got1.get(0) != 4 || got1.get(1) != 1 || got1.get(2) != 9) {
      throw new RuntimeException("FAILED case1 " + got1);
    }
    try {
      s.deleteNode(null);
    } catch (Exception e) {
      throw new RuntimeException("FAILED case2 threw");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
