// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113825
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc225_solution111 { // 定义类型
  static class MyStack { // static class MyStack {
    Deque<Integer> q1 = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> q1
    Deque<Integer> q2 = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> q2

    void push(int x) { // 定义函数/方法 push
      q2.addLast(x); // q2.addLast(x);
      while (!q1.isEmpty())
        q2.addLast(q1.removeFirst()); // 循环，直到不满足「取反 q1.isEmpty()) q2.addLast(q1.removeFirst());」
      Deque<Integer> t = q1;
      q1 = q2;
      q2 = t; // 把 q1; q1 赋值为 q2; q2 赋值为 另一字符串; 写入 Deque<Integer> t
    }

    int pop() {
      return q1.removeFirst();
    } // int pop() { return q1.removeFirst(); }

    int top() {
      return q1.peekFirst();
    } // int top() { return q1.peekFirst(); }

    boolean empty() {
      return q1.isEmpty();
    } // boolean empty() { return q1.isEmpty(); }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    MyStack o = new MyStack(); // 把 new MyStack(); 写入 MyStack o
    o.push(1);
    o.push(2); // 把 1 压入栈/数组尾部
    List<Object> out = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Object> out
    out.add(o.top()); // out 追加 o.top());
    out.add(o.pop()); // 弹出栈顶元素
    out.add(o.empty()); // out 追加 o 是否为空);
    List<Object> want =
        Arrays.asList(2, 2, false); // 把 Arrays.asList(2, 2, false); 写入 List<Object> want
    if (!out.equals(want)) throw new RuntimeException("FAILED " + out);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
