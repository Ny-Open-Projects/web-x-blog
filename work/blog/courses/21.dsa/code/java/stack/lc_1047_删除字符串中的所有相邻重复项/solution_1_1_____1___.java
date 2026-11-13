// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114201
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1047_solution111 { // 定义类型
  static String removeDuplicates(String s) { // 定义函数/方法 removeDuplicates
    Deque<Character> stk = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Character> stk
    for (char c : s.toCharArray()) { // for (char 字符 : 字符串.toCharArray()) {
      if (!stk.isEmpty() && stk.peek() == c)
        stk.pop(); // 若 取反 栈.isEmpty() 且 栈.peek() 等于 字符) 栈 弹出 );
      else stk.push(c); // 否则
    }
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    for (char c : stk) sb.append(c); // 把 字符 追加到列表尾部
    return sb.reverse().toString(); // 返回 sb.reverse().toString()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[] ins = {
      "abc", "abbaca", "azxxzy", "aabbcc", ""
    }; // 把 {「abc」, 「abc」, 「abc」, 「abc」, 「abc」}; 写入 String[] ins
    String[] want = {
      "abc", "ca", "ay", "", ""
    }; // 把 {「abc」, 「abc」, 「abc」, 「abc」, 「abc」}; 写入 String[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      String r = removeDuplicates(ins[i]); // 把 removeDuplicates(ins[下标 i]) 存入 右指针
      if (!r.equals(want[i])) {
        ok = false;
        System.out.println("FAIL in=" + ins[i] + " got=" + r + " want=" + want[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
