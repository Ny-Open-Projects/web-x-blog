// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc148_solution22 { // 定义类型
  static class ListNode { // static class ListNode {
    int val; // int 值;
    ListNode next; // ListNode 下一个;

    ListNode(int v) {
      val = v;
    } // 把 值; } 写入 ListNode(int v) { val
  }

  public ListNode sortList(ListNode head) { // 定义函数/方法 sortList
    List<ListNode> arr = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<ListNode> arr
    ListNode current = head; // 把 头节点; 写入 ListNode current
    while (current != null) { // 循环，直到不满足「current 不等于 null」
      arr.add(current); // 数组 追加 current);
      current = current.next; // 把 current.下一个; 写入 current
    }
    arr.sort((a, b) -> a.val - b.val); // 排序
    if (arr.isEmpty()) return null; // 若 数组.isEmpty()，直接返回 null
    ListNode newHead = arr.get(0); // 把 数组 查找 0); 写入 ListNode newHead
    ListNode c = newHead; // 把 newHead; 写入 ListNode c
    for (int i = 1; i < arr.size(); i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.大小() 就继续
      c.next = arr.get(i); // 把 数组 查找 下标 i); 写入 下一个
      c = c.next; // 把 字符.下一个; 写入 字符
    }
    c.next = null; // 把 null; 写入 下一个
    return newHead; // 返回 newHead
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
    lc148_solution22 s = new lc148_solution22(); // 把 new lc148_solution22(); 写入 lc148_solution22 s
    int[][] inputs = {{4, 2, 1, 3}, {4, 19, 14, 5, -3, 1}, {1}};
    int[][] wants = {{1, 2, 3, 4}, {-3, 1, 4, 5, 14, 19}, {1}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int idx = 0; idx < inputs.length; idx++) { // 让 idx 从 0 开始计数，idx 小于 inputs.长度 就继续
      if (!eq(
          s.sortList(build(inputs[idx])),
          wants[idx])) { // 若 取反 eq(字符串.sortList(build(inputs[idx])), wants[idx]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL in=" + Arrays.toString(inputs[idx])); // 打印输出
      }
    }
    if (s.sortList(null) != null) {
      ok = false;
      System.out.println("FAIL null");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
