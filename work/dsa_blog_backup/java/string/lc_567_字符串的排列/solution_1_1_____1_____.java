// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static boolean checkInclusion(String s1, String s2) { // 定义判定函数 checkInclusion
    if (s1.length() > s2.length()) return false; // 若 s1.长度() 超过 s2.长度()，直接返回 false
    int[] s1Count = new int[26]; // 把 new int[26]; 写入 int[] s1Count
    int[] s2Count = new int[26]; // 把 new int[26]; 写入 int[] s2Count
    for (int i = 0; i < s1.length(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 s1.长度() 就继续
      s1Count[s1.charAt(i) - 'a']++; // 逐字符处理
      s2Count[s2.charAt(i) - 'a']++; // 逐字符处理
    }
    if (Arrays.equals(s1Count, s2Count)) return true; // 若 Arrays.equals(s1Count, s2Count)，直接返回 true
    for (int i = s1.length(); i < s2.length(); i++) { // 让 下标 i 从 s1.长度() 开始计数，下标 i 小于 s2.长度() 就继续
      s2Count[s2.charAt(i) - 'a']++; // 逐字符处理
      s2Count[s2.charAt(i - s1.length()) - 'a']--; // 逐字符处理
      if (Arrays.equals(s1Count, s2Count))
        return true; // 若 Arrays.equals(s1Count, s2Count)，直接返回 true
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][] a = { // 把 { 写入 String[][] a
      {"ab", "eidbaooo"},
      {"ab", "eidboaoo"},
      {"hello", "ooolleoooleh"},
      {"a", "a"},
      {"abc", "cccccbabbbaaaa"},
      {"ab", "xyz"},
    };
    boolean[] wants = {true, false, false, true, true, false};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < a.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 数组.长度 就继续
      boolean got =
          checkInclusion(
              a[ci][0], a[ci][1]); // 把 checkInclusion(数组[ci][0], 数组[ci][1]); 写入 boolean got
      if (got != wants[ci]) { // 若 got 不等于 wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL case " + ci + " got " + got + " want " + wants[ci]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
