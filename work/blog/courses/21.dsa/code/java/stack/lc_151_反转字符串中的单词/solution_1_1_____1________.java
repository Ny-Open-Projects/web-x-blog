// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static String reverseWords(String s) { // 定义函数/方法 reverseWords
    String[] parts = s.split("\\s+"); // 把 字符串.split(「\字符串 加 」); 写入 String[] parts
    java.util.ArrayList<String> list = new java.util.ArrayList<>();
    for (String p : parts)
      if (!p.isEmpty()) list.add(p); // for (String 节点 : parts) if (取反 节点.isEmpty()) 列表 追加 节点);
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    for (int k = list.size() - 1; k >= 0; k--) { // 让 下标 k 从 列表.大小() 减 1 开始计数，下标 k 不低于 0 就继续
      if (k < list.size() - 1) sb.append(' '); // 若 下标 k 小于 列表.大小() 减 1) sb 追加 ' ');
      sb.append(list.get(k)); // 把 列表 查找 下标 k 追加到列表尾部
    }
    return sb.toString(); // 返回 sb.toString()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[] cases = { // 把 { 写入 String[] cases
      "the sky is blue",
      "  hello   world  ",
      "a good   example",
      "abc",
      "",
      "  fly me   to   the moon  ",
    };
    String[] wants = { // 把 { 写入 String[] wants
      "blue is sky the", "world hello", "example good a", "abc", "", "moon the to me fly",
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      String got = reverseWords(cases[ci]); // 把 reverseWords(cases[ci]) 存入 got
      if (!got.equals(wants[ci])) { // 若 取反 got.equals(wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL case " + ci + " got [" + got + "] want [" + wants[ci] + "]"); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
