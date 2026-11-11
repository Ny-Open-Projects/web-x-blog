// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513986
package com.webfault.dsa; // 引入依赖

class Lc83 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode(int v) {
      this.val = v;
    } // 把 值; } 写入 值
  }

  static ListNode build(int[] a) { // 定义函数/方法 build
    ListNode head = null; // 把 null; 写入 ListNode head
    for (int i = a.length - 1; i >= 0; i--) {
      ListNode n = new ListNode(a[i]);
      n.next = head;
      head = n;
    } // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 不低于 0 就继续
    return head; // 返回 头节点
  }

  static boolean eqList(ListNode h, int[] exp) { // 定义函数/方法 eqList
    int i = 0; // 把 0 存入 下标 i
    while (h != null) { // 循环，直到不满足「h 不等于 null」
      if (i >= exp.length || h.val != exp[i])
        return false; // 若 下标 i 不低于 exp.长度 或 h.值 不等于 exp[下标 i]，直接返回 false
      i++;
      h = h.next; // 把 h.下一个; 写入 i++; h
    }
    return i == exp.length; // 返回 下标 i 等于 exp.长度
  }

  static ListNode deleteDuplicates(ListNode head) { // 定义函数/方法 deleteDuplicates
    if (head == null) return null; // 若 头节点 等于 null，直接返回 null
    ListNode dummy = new ListNode(0); // 把 new ListNode(0); 写入 ListNode dummy
    dummy.next = head; // 把 头节点; 写入 下一个
    ListNode prev = dummy; // 把 哨兵节点; 写入 ListNode prev
    ListNode curr = head; // 把 头节点; 写入 ListNode curr
    while (curr != null) { // 循环，直到不满足「当前值 不等于 null」
      while (curr.next != null && curr.val == curr.next.val) curr = curr.next;
      if (prev.next == curr) prev = prev.next; // 若 前一个.下一个 等于 当前值) 前一个 赋值为 前一个.下一个;
      else prev.next = curr.next; // 否则
      curr = curr.next; // 把 当前值.下一个; 写入 当前值
    }
    return dummy.next; // 返回 哨兵节点.下一个
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    java.util.List<Object[]> cases = new java.util.ArrayList<>();
    cases.add(
        new Object[] {
          new int[] {1, 1, 2}, new int[] {2}
        }); // cases 追加 new Object[]{ new int[]{1,1,2}, new int[]{2} });
    cases.add(new Object[] {new int[] {1, 1, 2, 3, 3}, new int[] {2}});
    cases.add(new Object[] {new int[] {1, 2, 3}, new int[] {1, 2, 3}});
    cases.add(new Object[] {null, new int[] {}}); // cases 追加 new Object[]{ null, new int[]{} });
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      int[] inp = (int[]) c[0]; // 把 (int[]) 字符[0]; 写入 int[] inp
      int[] expc = (int[]) c[1]; // 把 (int[]) 字符[1]; 写入 int[] expc
      ListNode head =
          (inp == null)
              ? null
              : build(inp); // 把 (inp 等于 null) ? null : build(inp); 写入 ListNode head
      ListNode got = deleteDuplicates(head); // 把 deleteDuplicates(头节点); 写入 ListNode got
      if (!eqList(got, expc)) { // 若 取反 eqList(got, expc
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL deleteDuplicates want " + java.util.Arrays.toString(expc)); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
