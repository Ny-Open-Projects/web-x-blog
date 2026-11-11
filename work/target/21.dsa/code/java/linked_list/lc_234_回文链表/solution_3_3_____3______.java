// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096059
package com.webfault.dsa; // 引入依赖

class lc234 { // 定义类型
  static class ListNode {
    int val;
    ListNode next;

    ListNode(int v) {
      val = v;
    }
  }

  boolean isPalindrome(ListNode head) { // 定义判定函数 isPalindrome
    java.util.ArrayList<Integer> vals = new java.util.ArrayList<Integer>();
    while (head != null) {
      vals.add(head.val);
      head = head.next;
    } // 循环，直到不满足「头节点 不等于 null) { vals 追加 头节点.值); 头节点 赋值为 头节点.下一个; }」
    int l = 0, r = vals.size() - 1; // 把 0, 右指针 赋值为 vals.大小() 减 1 存入 左指针
    while (l < r) { // 循环，直到不满足「左指针 小于 右指针」
      if (!vals.get(l).equals(vals.get(r)))
        return false; // 若 取反 vals 查找 左指针).equals(vals 查找 右指针))，直接返回 false
      l++;
      r--; // 左指针 加一 ; 右指针 减一 ;
    }
    return true; // 返回 true
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

  public static void main(String[] args) { // public static void main(String[] args) {
    lc234 s = new lc234(); // 把 new lc234(); 写入 lc234 s
    int[][] cases = {
      {}, {1, 2, 1}, {1, 2}, {1, 2, 2, 1}
    }; // 把 {{}, {1, 2, 1}, {1, 2}, {1, 2, 2, 1}}; 写入 int[][] cases
    boolean[] wants = {true, true, false, true}; // 把 {true, true, false, true}; 写入 boolean[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < wants.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 wants.长度 就继续
      boolean got =
          s.isPalindrome(build(cases[i])); // 把 字符串.isPalindrome(build(cases[下标 i])); 写入 boolean got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
