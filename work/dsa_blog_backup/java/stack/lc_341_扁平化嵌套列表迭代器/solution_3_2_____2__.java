// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345560
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc341_solution322 { // 定义类型
  static class NestedInteger { // static class NestedInteger {
    Integer _int; // Integer _int;
    List<NestedInteger> _list; // List 小于 NestedInteger 超过 _list;

    NestedInteger(Integer v) {
      _int = v;
      _list = null;
    } // 把 值; _list 赋值为 null; } 写入 NestedInteger(Integer v) { _int

    NestedInteger(List<NestedInteger> l) {
      _list = l;
      _int = null;
    }

    boolean isInteger() {
      return _int != null;
    } // 把 null; } 写入 boolean isInteger() { return _int !

    int getInteger() {
      return _int;
    } // int getInteger() { return _int; }

    List<NestedInteger> getList() {
      return _list;
    } // List 小于 NestedInteger 超过 getList() { return _list; }
  }

  static class NestedIterator { // static class NestedIterator {
    Deque<NestedInteger> stack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<NestedInteger> stack

    NestedIterator(List<NestedInteger> nl) { // NestedIterator(List 小于 NestedInteger 超过 nl) {
      for (int i = nl.size() - 1; i >= 0; i--)
        stack.push(nl.get(i)); // 让 下标 i 从 nl.大小() 减 1 开始计数，下标 i 不低于 0 就继续
    }

    boolean hasNext() { // 定义函数/方法 hasNext
      while (!stack.isEmpty()) { // 循环，直到不满足「取反 栈.isEmpty(」
        if (stack.peek().isInteger()) return true; // 若 栈.peek().isInteger()，直接返回 true
        List<NestedInteger> cur = stack.pop().getList(); // 弹出栈顶元素
        for (int i = cur.size() - 1; i >= 0; i--)
          stack.push(cur.get(i)); // 让 下标 i 从 当前值.大小() 减 1 开始计数，下标 i 不低于 0 就继续
      }
      return false; // 返回 false
    }

    int next() {
      return stack.pop().getInteger();
    } // 弹出栈顶元素
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<NestedInteger> nested =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<NestedInteger> nested
    nested.add(new NestedInteger(1)); // nested 追加 new NestedInteger(1));
    List<NestedInteger> inner =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<NestedInteger> inner
    inner.add(new NestedInteger(2)); // inner 追加 new NestedInteger(2));
    inner.add(new NestedInteger(3)); // inner 追加 new NestedInteger(3));
    nested.add(new NestedInteger(inner)); // nested 追加 new NestedInteger(inner));
    NestedIterator it =
        new NestedIterator(nested); // 把 new NestedIterator(nested); 写入 NestedIterator it
    List<Integer> out = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> out
    while (it.hasNext()) out.add(it.next()); // 循环，直到不满足「it.hasNext()) out 追加 it.下一个());」
    List<Integer> want = Arrays.asList(1, 2, 3); // 把 Arrays.asList(1, 2, 3); 写入 List<Integer> want
    if (!out.equals(want)) throw new RuntimeException("FAILED " + out);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
