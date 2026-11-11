// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_5___5.py
  static String reverseWords3(String s) { // 定义函数/方法 reverseWords3
    if (s == null || s.isEmpty()) return ""; // 若 字符串 等于 null 或 字符串.isEmpty()，直接返回 「」
    String[] words = s.split(" ", -1); // 把 字符串.split(「 」, 减 1); 写入 String[] words
    List<String> rev = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> rev
    for (String word : words) { // for (String 单词 : 单词列表) {
      rev.add(new StringBuilder(word).reverse().toString()); // 反转
    }
    return String.join(" ", rev); // 返回 String.join(「 」, rev)
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
      String got = reverseWords3(c[0]); // 把 reverseWords3(字符[0]) 存入 got
      if (!got.equals(c[1])) { // 若 取反 got.equals(字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL reverseWords3(\"" + c[0] + "\")=\"" + got + "\" want \"" + c[1] + "\""); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
