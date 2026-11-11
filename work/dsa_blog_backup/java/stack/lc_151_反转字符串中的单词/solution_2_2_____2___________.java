// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static char[] trimSpaces(String s) { // 定义函数/方法 trimSpaces
    int left = 0, right = s.length() - 1; // 把 0, 右边界 赋值为 字符串.长度() 减 1 存入 左边界
    while (left <= right && s.charAt(left) == ' ')
      left++; // 循环，直到不满足「左边界 不超过 右边界 且 字符串 取字符 左边界) 等于 ' ') 左边界 加一 ;」
    while (left <= right && s.charAt(right) == ' ')
      right--; // 循环，直到不满足「左边界 不超过 右边界 且 字符串 取字符 右边界) 等于 ' ') 右边界 减一 ;」
    StringBuilder out = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder out
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      if (s.charAt(left) != ' ')
        out.append(s.charAt(left)); // 若 字符串 取字符 左边界) 不等于 ' ') out 追加 字符串 取字符 左边界));
      else if (out.length() > 0 && out.charAt(out.length() - 1) != ' ') out.append(s.charAt(left));
      left++; // 左边界 加一
    }
    return out.toString().toCharArray(); // 返回 out.toString().toCharArray()
  }

  static void reverse(char[] l, int left, int right) { // 定义函数/方法 reverse
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
      char t = l[left];
      l[left] = l[right];
      l[right] = t;
      left++;
      right--; // 左边界 加一 ; 右边界 减一 ;
    }
  }

  static void reverseEachWord(char[] l) { // 定义函数/方法 reverseEachWord
    int n = l.length, start = 0, end = 0; // 把 左指针.长度, 起点 赋值为 0, 终点 赋值为 0 存入 元素个数
    while (start < n) { // 循环，直到不满足「起点 小于 元素个数」
      while (end < n && l[end] != ' ') end++; // 循环，直到不满足「终点 小于 元素个数 且 左指针[终点] 不等于 ' ') 终点 加一 ;」
      reverse(l, start, end - 1); // reverse(左指针, 起点, 终点 减 1);
      start = end + 1; // 把 终点 加 1; 写入 起点
      end = start; // 把 起点; 写入 终点
    }
  }

  static String reverseWords(String s) { // 定义函数/方法 reverseWords
    char[] l = trimSpaces(s); // 把 trimSpaces(字符串); 写入 char[] l
    reverse(l, 0, l.length - 1); // reverse(左指针, 0, 左指针.长度 减 1);
    reverseEachWord(l); // reverseEachWord(左指针);
    return new String(l); // 返回 new String(左指针)
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
