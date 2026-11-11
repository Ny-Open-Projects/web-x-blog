// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static String reverseWords(String s) { // 定义函数/方法 reverseWords
    int left = 0, right = s.length() - 1; // 把 0, 右边界 赋值为 字符串.长度() 减 1 存入 左边界
    java.util.ArrayList<String> words = new java.util.ArrayList<>();
    StringBuilder word = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder word
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      if (s.charAt(left) == ' ' && word.length() > 0) { // 若 字符串 取字符 左边界) 等于 ' ' 且 单词.长度() 超过 0
        words.add(0, word.toString()); // 单词列表 追加 0, 单词.toString());
        word = new StringBuilder(); // 把 new StringBuilder(); 写入 单词
      } else if (s.charAt(left) != ' ') { // 否则，若 字符串 取字符 左边界) 不等于 ' '
        word.append(s.charAt(left)); // 把 字符串 取字符 左边界 追加到列表尾部
      }
      left++; // 左边界 加一
    }
    if (word.length() > 0)
      words.add(0, word.toString()); // 若 单词.长度() 超过 0) 单词列表 追加 0, 单词.toString());
    return String.join(" ", words); // 返回 String.join(「 」, 单词列表)
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
