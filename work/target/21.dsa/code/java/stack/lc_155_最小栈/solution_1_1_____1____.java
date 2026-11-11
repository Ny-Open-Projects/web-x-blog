// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc155_solution111 { // 定义类型
  static class MinStack { // static class MinStack {
    Deque<Integer> xStack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> xStack
    Deque<Integer> minStack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> minStack

    MinStack() {
      minStack.push(Integer.MAX_VALUE);
    } // 把 Integer.MAX_VALUE 压入栈/数组尾部

    void push(int val) {
      xStack.push(val);
      minStack.push(Math.min(minStack.peek(), val));
    } // 把 值 压入栈/数组尾部

    void pop() {
      xStack.pop();
      minStack.pop();
    } // 弹出栈顶元素

    int top() {
      return xStack.peek();
    } // int top() { return xStack.peek(); }

    int getMin() {
      return minStack.peek();
    } // int getMin() { return minStack.peek(); }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    MinStack m = new MinStack(); // 把 new MinStack(); 写入 MinStack m
    m.push(-2);
    m.push(0);
    m.push(-3); // 把 减 2 压入栈/数组尾部
    List<Integer> out = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> out
    out.add(m.getMin()); // out 追加 映射表.getMin());
    m.pop(); // 弹出栈顶元素
    out.add(m.top()); // out 追加 映射表.top());
    out.add(m.getMin()); // out 追加 映射表.getMin());
    List<Integer> want =
        Arrays.asList(-3, 0, -2); // 把 Arrays.asList( 减 3, 0, 减 2); 写入 List<Integer> want
    if (!out.equals(want)) throw new RuntimeException("FAILED " + out);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
