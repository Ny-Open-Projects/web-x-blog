// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134358253
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc21S3 { // 定义类型
  static class ListNode { // static class ListNode {
    int val;
    ListNode next; // int 值; ListNode 下一个;

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v){ val
  }

  static ListNode build(Integer[] vals) { // 定义函数/方法 build
    ListNode dummy = new ListNode(0);
    ListNode p = dummy; // 把 new ListNode(0); ListNode 节点 赋值为 哨兵节点; 写入 ListNode dummy
    for (Integer v : vals) {
      p.next = new ListNode(v);
      p = p.next;
    } // 把 new ListNode(值); 节点 赋值为 节点.下一个; } 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  static int[] toArr(ListNode n) { // 定义函数/方法 toArr
    java.util.ArrayList<Integer> l = new java.util.ArrayList<>();
    while (n != null) {
      l.add(n.val);
      n = n.next;
    }
    int[] r = new int[l.size()]; // 把 new int[左指针.大小()]; 写入 int[] r
    for (int i = 0; i < r.length; i++) r[i] = l.get(i); // 让 下标 i 从 0 开始计数，下标 i 小于 右指针.长度 就继续
    return r; // 返回 右指针
  }

  static void check(int[] got, int[] want) { // 定义判定函数 check
    if (got.length != want.length)
      throw new RuntimeException("FAILED len got=" + got.length + " want=" + want.length);
    for (int i = 0; i < got.length; i++)
      if (got[i] != want[i])
        throw new RuntimeException(
            "FAILED at "
                + i
                + " got="
                + got[i]
                + " want="
                + want[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
  }

  static ListNode mergeTwoLists(ListNode list1, ListNode list2) { // 定义函数/方法 mergeTwoLists
    ListNode res = new ListNode(0); // 把 new ListNode(0); 写入 ListNode res
    ListNode p = res; // 把 结果; 写入 ListNode p
    ListNode p1 = list1, p2 = list2; // 把 list1, p2 赋值为 list2; 写入 ListNode p1
    while (p1 != null && p2 != null) { // 循环，直到不满足「p1 不等于 null 且 p2 不等于 null」
      if (p1.val < p2.val) {
        p.next = p1;
        p1 = p1.next;
      } // 若 p1.值 小于 p2.值) { 节点.下一个 赋值为 p1; p1 赋值为 p1.下一个; }
      else {
        p.next = p2;
        p2 = p2.next;
      } // 否则
      p = p.next; // 把 节点.下一个; 写入 节点
    }
    p.next = (p1 != null) ? p1 : p2; // 把 (p1 不等于 null) ? p1 : p2; 写入 下一个
    return res.next; // 返回 结果.下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    check(
        toArr(mergeTwoLists(build(new Integer[] {1, 2, 4}), build(new Integer[] {1, 3, 4}))),
        new int[] {1, 1, 2, 3, 4, 4});
    check(
        toArr(mergeTwoLists(build(new Integer[] {1, 3, 5}), build(new Integer[] {2, 4, 6}))),
        new int[] {1, 2, 3, 4, 5, 6});
    check(toArr(mergeTwoLists(build(new Integer[] {}), build(new Integer[] {0}))), new int[] {0});
    check(toArr(mergeTwoLists(build(new Integer[] {5}), build(new Integer[] {}))), new int[] {5});
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
