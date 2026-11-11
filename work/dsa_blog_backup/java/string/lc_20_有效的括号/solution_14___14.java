// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型
  public boolean isValid(String s) { // 定义判定函数 isValid
    Deque<Character> stack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Character> stack
    Map<Character, Character> pairs =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Character> pairs
    pairs.put(')', '('); // pairs.put(')', '(');
    pairs.put(']', '['); // pairs.put(']', '[');
    pairs.put('}', '{'); // pairs.put('}', '{');
    for (int i = 0; i < s.length(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.长度() 就继续
      char ch = s.charAt(i); // 逐字符处理
      if (pairs.containsKey(ch)) { // 若 pairs.containsKey(字符
        char top = stack.isEmpty() ? '#' : stack.pop(); // 弹出栈顶元素
        if (top != pairs.get(ch)) return false; // 若 top 不等于 pairs 查找 字符)，直接返回 false
      } else { // 否则
        stack.push(ch); // 把 字符 压入栈/数组尾部
      }
    }
    return stack.isEmpty(); // 返回 栈.isEmpty()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[] inputs = {"()", "()[]{}", "(]"}; // 把 {「()」, 「()」, 「()」}; 写入 String[] inputs
    boolean[] wants = {true, true, false}; // 把 {true, true, false}; 写入 boolean[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < inputs.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 inputs.长度 就继续
      boolean got = s.isValid(inputs[i]); // 把 字符串.isValid(inputs[下标 i]); 写入 boolean got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL isValid(" + inputs[i] + ")=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
