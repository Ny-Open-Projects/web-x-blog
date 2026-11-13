// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc2_solution22 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode() {} // ListNode() {}

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  public ListNode addTwoNumbers(ListNode l1, ListNode l2) { // 定义函数/方法 addTwoNumbers
    if (l1 == null && l2 == null) { // 若 l1 等于 null 且 l2 等于 null
      return null; // 返回 null
    } else if (l1 == null) { // 否则，若 l1 等于 null
      return l2; // 返回 l2
    } else if (l2 == null) { // 否则，若 l2 等于 null
      return l1; // 返回 l1
    }
    ListNode head = null, tail = null; // 把 null, 尾节点 赋值为 null; 写入 ListNode head
    int carry = 0; // 把 0 存入 carry
    while (l1 != null || l2 != null) { // 循环，直到不满足「l1 不等于 null 或 l2 不等于 null」
      int val1 = l1 != null ? l1.val : 0; // 把 l1 不等于 null ? l1.值 : 0 存入 val1
      int val2 = l2 != null ? l2.val : 0; // 把 l2 不等于 null ? l2.值 : 0 存入 val2
      int sum = val1 + val2 + carry; // 把 val1 加 val2 加 carry 存入 累计和
      if (head == null) { // 若 头节点 等于 null
        head = tail = new ListNode(sum % 10); // 把 尾节点 赋值为 new ListNode(累计和 对…取模 10); 写入 头节点
      } else { // 否则
        tail.next = new ListNode(sum % 10); // 把 new ListNode(累计和 对…取模 10); 写入 下一个
        tail = tail.next; // 把 尾节点.下一个; 写入 尾节点
      }
      carry = sum / 10; // 把 累计和 除以 10; 写入 carry
      if (l1 != null) l1 = l1.next; // 若 l1 不等于 null) l1 赋值为 l1.下一个;
      if (l2 != null) l2 = l2.next; // 若 l2 不等于 null) l2 赋值为 l2.下一个;
    }
    if (carry > 0) { // 若 carry 超过 0
      tail.next = new ListNode(carry); // 把 new ListNode(carry); 写入 下一个
    }
    return head; // 返回 头节点
  }

  static ListNode build(int[] vals) { // 定义函数/方法 build
    ListNode dummy = new ListNode(0),
        cur = dummy; // 把 new ListNode(0), 当前值 赋值为 哨兵节点; 写入 ListNode dummy
    for (int v : vals) {
      cur.next = new ListNode(v);
      cur = cur.next;
    } // 把 new ListNode(值); 当前值 赋值为 当前值.下一个; } 写入 下一个
    return dummy.next; // 返回 哨兵节点.下一个
  }

  static List<Integer> toList(ListNode h) { // 定义函数/方法 toList
    List<Integer> r = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> r
    while (h != null) {
      r.add(h.val);
      h = h.next;
    } // 循环，直到不满足「h 不等于 null) { 右指针 追加 h.值); h 赋值为 h.下一个; }」
    return r; // 返回 右指针
  }

  static boolean eqList(ListNode a, ListNode b) { // 定义函数/方法 eqList
    while (a != null && b != null) {
      if (a.val != b.val) return false;
      a = a.next;
      b = b.next;
    }
    return a == null && b == null; // 返回 数组 等于 null 且 b 等于 null
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc2_solution22 s = new lc2_solution22(); // 把 new lc2_solution22(); 写入 lc2_solution22 s
    Object[] t1 = new Object[] {new int[] {2, 4, 3}, new int[] {5, 6, 4}, new int[] {7, 0, 8}};
    Object[] t2 = new Object[] {new int[] {0}, new int[] {0}, new int[] {0}};
    Object[] t3 = new Object[] {new int[] {9, 9}, new int[] {1}, new int[] {0, 0, 1}};
    Object[][] tests = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 Object[][] tests
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests) { // for (Object[] 另一字符串 : tests) {
      ListNode got = s.addTwoNumbers(build((int[]) t[0]), build((int[]) t[1]));
      if (!eqList(got, build((int[]) t[2]))) { // 若 取反 eqList(got, build((int[]) 另一字符串[2]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL addTwoNumbers("
                + Arrays.toString((int[]) t[0])
                + ","
                + Arrays.toString((int[]) t[1])
                + ")="
                + toList(got)
                + " want "
                + Arrays.toString((int[]) t[2])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
