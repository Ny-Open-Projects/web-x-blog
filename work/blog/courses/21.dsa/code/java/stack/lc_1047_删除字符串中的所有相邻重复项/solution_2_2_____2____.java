// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114201
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1047_solution222 { // 定义类型
  static String removeDuplicates(String s) { // 定义函数/方法 removeDuplicates
    StringBuilder stack = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder stack
    for (char x : s.toCharArray()) { // for (char x : 字符串.toCharArray()) {
      if (stack.length() > 0
          && stack.charAt(stack.length() - 1) == x) { // 若 栈.长度() 超过 0 且 栈 取字符 栈.长度() 减 1) 等于 x
        stack.deleteCharAt(stack.length() - 1); // 栈.deleteCharAt(栈.长度() 减 1);
        continue; // 跳过本轮，进入下一次
      }
      stack.append(x); // 把 x 追加到列表尾部
    }
    return stack.toString(); // 返回 栈.toString()
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
