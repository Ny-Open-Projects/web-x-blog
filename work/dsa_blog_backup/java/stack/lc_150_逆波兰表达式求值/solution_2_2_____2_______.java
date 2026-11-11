// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113233
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static int evalRPN(String[] tokens) { // 定义函数/方法 evalRPN
    int n = tokens.length; // 把 tokens.长度 存入 元素个数
    int[] stack = new int[(n + 1) / 2]; // 把 new int[(元素个数 加 1) 除以 2]; 写入 int[] stack
    int index = -1; // 把 减 1 存入 index
    for (String token : tokens) { // for (String token : tokens) {
      if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
        int num2 = stack[index]; // 把 栈[index] 存入 num2
        int num1 = stack[index - 1]; // 把 栈[index 减 1] 存入 num1
        index--; // index 减一
        if (token.equals("+"))
          stack[index] = num1 + num2; // 若 token.equals(「 加 」)) 栈[index] 赋值为 num1 加 num2;
        else if (token.equals("-"))
          stack[index] = num1 - num2; // 否则，若 token.equals(「 减 」)) 栈[index] 赋值为 num1 减 num2;
        else if (token.equals("*"))
          stack[index] = num1 * num2; // 否则，若 token.equals(「 乘 」)) 栈[index] 赋值为 num1 乘 num2;
        else stack[index] = (int) (num1 / num2); // 否则
      } else { // 否则
        index++; // index 加一
        stack[index] = Integer.parseInt(token); // 把 Integer.转整数(token); 写入 stack[index]
      }
    }
    return stack[index]; // 返回 栈[index]
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
