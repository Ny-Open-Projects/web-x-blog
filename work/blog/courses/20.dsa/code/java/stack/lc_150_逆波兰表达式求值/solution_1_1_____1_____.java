// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113233
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static int evalRPN(String[] tokens) { // 定义函数/方法 evalRPN
    java.util.LinkedList<Integer> stack = new java.util.LinkedList<>();
    for (String token : tokens) { // for (String token : tokens) {
      if (!token.equals("+") && !token.equals("-") && !token.equals("*") && !token.equals("/")) {
        stack.add(Integer.parseInt(token)); // 栈 追加 Integer.转整数(token));
      } else { // 否则
        int num2 = stack.pollLast(); // 把 栈.pollLast() 存入 num2
        int num1 = stack.pollLast(); // 把 栈.pollLast() 存入 num1
        if (token.equals("+")) stack.add(num1 + num2); // 若 token.equals(「 加 」)) 栈 追加 num1 加 num2);
        else if (token.equals("-"))
          stack.add(num1 - num2); // 否则，若 token.equals(「 减 」)) 栈 追加 num1 减 num2);
        else if (token.equals("*"))
          stack.add(num1 * num2); // 否则，若 token.equals(「 乘 」)) 栈 追加 num1 乘 num2);
        else stack.add((int) (num1 / num2)); // 否则
      }
    }
    return stack.pollLast(); // 返回 栈.pollLast()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][][] cases = { // 把 { 写入 String[][][] cases
      {{"2", "1", "+", "3", "*"}},
      {{"4", "13", "5", "/", "+"}},
      {{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}},
      {{"2", "1", "+", "3", "*"}},
      {{"3", "11", "5", "+", "-"}},
    };
    int[] wants = {9, 6, 22, 9, -13}; // 把 {9, 6, 22, 9, 减 13}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      int got = evalRPN(cases[ci][0]); // 把 evalRPN(cases[ci][0]) 存入 got
      if (got != wants[ci]) { // 若 got 不等于 wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL case " + ci + " got " + got + " want " + wants[ci]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
