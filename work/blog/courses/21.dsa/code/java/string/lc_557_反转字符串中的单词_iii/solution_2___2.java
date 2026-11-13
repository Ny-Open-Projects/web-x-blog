// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_2___2.py
  static String reverseWords(String s) { // 定义函数/方法 reverseWords
    String[] words = s.split(" ", -1); // 把 字符串.split(「 」, 减 1); 写入 String[] words
    for (int i = 0; i < words.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 单词列表.长度 就继续
      words[i] = new StringBuilder(words[i]).reverse().toString(); // 反转
    }
    return String.join(" ", words); // 返回 String.join(「 」, 单词列表)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][] cases = { // 把 { 写入 String[][] cases
      {"Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"},
      {"God Ding", "doG gniD"},
      {"hello", "olleh"},
      {"", ""},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (String[] c : cases) { // for (String[] 字符 : cases) {
      String got = reverseWords(c[0]); // 把 reverseWords(字符[0]) 存入 got
      if (!got.equals(c[1])) { // 若 取反 got.equals(字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL reverseWords(\"" + c[0] + "\")=\"" + got + "\" want \"" + c[1] + "\""); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
