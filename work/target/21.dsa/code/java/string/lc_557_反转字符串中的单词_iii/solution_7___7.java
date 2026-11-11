// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_7___7.py (nested reverse_word two-pointer helper)
  static String reverseWords(String s) { // 定义函数/方法 reverseWords
    return String.join(
        " ",
        reverseEach(s.split(" ", -1))); // 返回 String.join(「 」, reverseEach(字符串.split(「 」, 减 1)))
  }

  static String[] reverseEach(String[] words) { // 定义函数/方法 reverseEach
    String[] out = new String[words.length]; // 把 new String[单词列表.长度]; 写入 String[] out
    for (int i = 0; i < words.length; i++)
      out[i] = reverseWord(words[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 单词列表.长度 就继续
    return out; // 返回 out
  }

  static String reverseWord(String word) { // 定义函数/方法 reverseWord
    char[] chars = word.toCharArray(); // 把 单词.toCharArray(); 写入 char[] chars
    int left = 0, right = chars.length - 1; // 把 0, 右边界 赋值为 chars.长度 减 1 存入 左边界
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
      char t = chars[left];
      chars[left] = chars[right];
      chars[right] = t;
      left++;
      right--; // 左边界 加一 ; 右边界 减一 ;
    }
    return new String(chars); // 返回 new String(chars)
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
