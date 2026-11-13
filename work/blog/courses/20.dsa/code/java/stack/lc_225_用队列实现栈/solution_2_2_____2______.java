// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113825
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc225_solution222 { // 定义类型
  static class MyStack { // static class MyStack {
    Deque<Integer> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> q

    void push(int x) { // 定义函数/方法 push
      int n = q.size(); // 把 节点.大小() 存入 元素个数
      q.addLast(x); // 节点.addLast(x);
      for (int i = 0; i < n; i++) q.addLast(q.removeFirst()); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    }

    int pop() {
      return q.removeFirst();
    } // int pop() { return 节点.removeFirst(); }

    int top() {
      return q.peekFirst();
    } // int top() { return 节点.peekFirst(); }

    boolean empty() {
      return q.isEmpty();
    } // boolean empty() { return 节点.isEmpty(); }
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
