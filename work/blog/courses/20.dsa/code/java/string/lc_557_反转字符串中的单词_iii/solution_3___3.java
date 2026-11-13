// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖
import java.util.regex.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_3___3.py (regex \S+ tokens)
  static String reverseWords(String s) { // 定义函数/方法 reverseWords
    if (s == null || s.isEmpty()) return ""; // 若 字符串 等于 null 或 字符串.isEmpty()，直接返回 「」
    Matcher m =
        Pattern.compile("\\S+").matcher(s); // 把 Pattern.compile(「\S 加 」).matcher(字符串); 写入 Matcher m
    List<String> rev = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> rev
    while (m.find()) { // 循环，直到不满足「映射表 查找」
      rev.add(new StringBuilder(m.group()).reverse().toString()); // 反转
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
