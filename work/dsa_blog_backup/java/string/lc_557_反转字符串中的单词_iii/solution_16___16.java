// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  // faithful translation of python solution_16___16.py (in-place char array scan)
  static String reverseWords(String s) { // 定义函数/方法 reverseWords
    char[] chars = s.toCharArray(); // 把 字符串.toCharArray(); 写入 char[] chars
    int n = chars.length, i = 0; // 把 chars.长度, 下标 i 赋值为 0 存入 元素个数
    while (i < n) { // 循环，直到不满足「下标 i 小于 元素个数」
      if (chars[i] == ' ') {
        i++;
        continue;
      } // 若 chars[下标 i] 等于 ' ') { 下标 i 加一 ; continue; }
      int j = i; // 把 下标 i 存入 下标 j
      while (j < n && chars[j] != ' ')
        j++; // 循环，直到不满足「下标 j 小于 元素个数 且 chars[下标 j] 不等于 ' ') 下标 j 加一 ;」
      int left = i, right = j - 1; // 把 下标 i, 右边界 赋值为 下标 j 减 1 存入 左边界
      while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
        char t = chars[left];
        chars[left] = chars[right];
        chars[right] = t;
        left++;
        right--; // 左边界 加一 ; 右边界 减一 ;
      }
      i = j; // 把 下标 j; 写入 下标 i
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
