// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096505
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc876_solution333 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  public ListNode middleNode(ListNode head) { // 定义函数/方法 middleNode
    List<ListNode> nodes = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<ListNode> nodes
    ListNode curr = head; // 把 头节点; 写入 ListNode curr
    while (curr != null) { // 循环，直到不满足「当前值 不等于 null」
      nodes.add(curr); // nodes 追加 当前值);
      curr = curr.next; // 把 当前值.下一个; 写入 当前值
    }
    int n = nodes.size(); // 把 nodes.大小() 存入 元素个数
    return nodes.get((n - 1) / 2); // 返回 nodes 查找 (元素个数 减 1) 除以 2)
  }

  static ListNode build(int[] a) { // 定义函数/方法 build
    ListNode dummy = new ListNode(0),
        cur = dummy; // 把 new ListNode(0), 当前值 赋值为 哨兵节点; 写入 ListNode dummy
    for (int v : a) {
      cur.next = new ListNode(v);
      cur = cur.next;
    } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc876_solution333 s =
        new lc876_solution333(); // 把 new lc876_solution333(); 写入 lc876_solution333 s
    Object[] t1 =
        new Object[] {
          new int[] {1, 2, 3, 4, 5}, 3
        }; // 把 new Object[]{new int[]{1, 2, 3, 4, 5}, 3}; 写入 Object[] t1
    Object[] t2 =
        new Object[] {
          new int[] {1, 2, 3, 4}, 2
        }; // 把 new Object[]{new int[]{1, 2, 3, 4}, 2}; 写入 Object[] t2
    Object[] t3 =
        new Object[] {new int[] {1}, 1}; // 把 new Object[]{new int[]{1}, 1}; 写入 Object[] t3
    Object[][] tests = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 Object[][] tests
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests) { // for (Object[] 另一字符串 : tests) {
      int[] inp = (int[]) t[0]; // 把 (int[]) 另一字符串[0]; 写入 int[] inp
      int want = (int) t[1]; // 把 (int) 另一字符串[1] 存入 want
      ListNode got = s.middleNode(build(inp)); // 把 字符串.middleNode(build(inp)); 写入 ListNode got
      if (got == null || got.val != want) { // 若 got 等于 null 或 got.值 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL middleNode("
                + Arrays.toString(inp)
                + ")="
                + (got == null ? "null" : got.val)
                + " want "
                + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
