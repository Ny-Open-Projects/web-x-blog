// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc232_solution111 { // 定义类型
  static class MyQueue { // static class MyQueue {
    Deque<Integer> inStack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> inStack
    Deque<Integer> outStack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> outStack

    void push(int x) {
      inStack.push(x);
    } // 把 x 压入栈/数组尾部

    void in2out() {
      while (!inStack.isEmpty()) outStack.push(inStack.pop());
    } // 把 inStack 弹出 压入栈/数组尾部

    int pop() {
      if (outStack.isEmpty()) in2out();
      return outStack.pop();
    } // 弹出栈顶元素

    int peek() {
      if (outStack.isEmpty()) in2out();
      return outStack.peek();
    }

    boolean empty() {
      return inStack.isEmpty() && outStack.isEmpty();
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    MyQueue q = new MyQueue(); // 把 new MyQueue(); 写入 MyQueue q
    q.push(1);
    q.push(2); // 把 1 压入栈/数组尾部
    List<Object> out = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Object> out
    out.add(q.peek()); // out 追加 节点.peek());
    out.add(q.pop()); // 弹出栈顶元素
    out.add(q.empty()); // out 追加 节点 是否为空);
    q.push(3); // 把 3 压入栈/数组尾部
    out.add(q.pop()); // 弹出栈顶元素
    out.add(q.pop()); // 弹出栈顶元素
    List<Object> want =
        Arrays.asList(
            1, 1, false, 2, 3); // 把 Arrays.asList(1, 1, false, 2, 3); 写入 List<Object> want
    if (!out.equals(want)) throw new RuntimeException("FAILED " + out);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
