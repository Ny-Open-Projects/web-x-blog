// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc148_solution55 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  static ListNode sortList(ListNode head) { // 定义函数/方法 sortList
    if (head == null || head.next == null) return head; // 若 头节点 等于 null 或 头节点.下一个 等于 null，直接返回 头节点
    ListNode slow = head, fast = head; // 把 头节点, 快指针 赋值为 头节点; 写入 ListNode slow
    while (fast.next != null
        && fast.next.next != null) { // 循环，直到不满足「快指针.下一个 不等于 null 且 快指针.下一个.下一个 不等于 null」
      slow = slow.next; // 把 慢指针.下一个; 写入 慢指针
      fast = fast.next.next; // 把 快指针.下一个.下一个; 写入 快指针
    }
    ListNode mid = slow.next; // 把 慢指针.下一个; 写入 ListNode mid
    slow.next = null; // 把 null; 写入 下一个
    ListNode left = sortList(head); // 把 sortList(头节点); 写入 ListNode left
    ListNode right = sortList(mid); // 把 sortList(中点); 写入 ListNode right
    return merge(left, right); // 返回 merge(左边界, 右边界)
  }

  private static ListNode merge(
      ListNode l1, ListNode l2) { // private static ListNode merge(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0); // 把 new ListNode(0); 写入 ListNode dummy
    ListNode cur = dummy; // 把 哨兵节点; 写入 ListNode cur
    while (l1 != null && l2 != null) { // 循环，直到不满足「l1 不等于 null 且 l2 不等于 null」
      if (l1.val <= l2.val) {
        cur.next = l1;
        l1 = l1.next;
      } // 若 l1.值 不超过 l2.值) { 当前值.下一个 赋值为 l1; l1 赋值为 l1.下一个; }
      else {
        cur.next = l2;
        l2 = l2.next;
      } // 否则
      cur = cur.next; // 把 当前值.下一个; 写入 当前值
    }
    cur.next = (l1 != null) ? l1 : l2; // 把 (l1 不等于 null) ? l1 : l2; 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  static ListNode build(int[] vals) { // 定义函数/方法 build
    if (vals.length == 0) return null; // 若 vals.长度 等于 0，直接返回 null
    ListNode head = new ListNode(vals[0]); // 把 new ListNode(vals[0]); 写入 ListNode head
    ListNode c = head; // 把 头节点; 写入 ListNode c
    for (int i = 1; i < vals.length; i++) {
      c.next = new ListNode(vals[i]);
      c = c.next;
    } // 让 下标 i 从 1 开始计数，下标 i 小于 vals.长度 就继续
    return head; // 返回 头节点
  }

  static boolean eq(ListNode h, int[] want) { // 定义函数/方法 eq
    int i = 0; // 把 0 存入 下标 i
    while (h != null) { // 循环，直到不满足「h 不等于 null」
      if (i >= want.length || h.val != want[i])
        return false; // 若 下标 i 不低于 want.长度 或 h.值 不等于 want[下标 i]，直接返回 false
      i++;
      h = h.next; // 把 h.下一个; 写入 i++; h
    }
    return i == want.length; // 返回 下标 i 等于 want.长度
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] inputs = {{4, 2, 1, 3}, {4, 19, 14, 5, -3, 1}, {1}};
    int[][] wants = {{1, 2, 3, 4}, {-3, 1, 4, 5, 14, 19}, {1}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int idx = 0; idx < inputs.length; idx++) { // 让 idx 从 0 开始计数，idx 小于 inputs.长度 就继续
      if (!eq(
          sortList(build(inputs[idx])),
          wants[idx])) { // 若 取反 eq(sortList(build(inputs[idx])), wants[idx]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL in=" + Arrays.toString(inputs[idx])); // 打印输出
      }
    }
    if (sortList(null) != null) {
      ok = false;
      System.out.println("FAIL null");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
