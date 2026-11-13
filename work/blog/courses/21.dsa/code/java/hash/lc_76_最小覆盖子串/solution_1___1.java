// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133465616
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc76_solution11 { // 定义类型
  static String minWindow(String s, String t) { // 定义函数/方法 minWindow
    if (s == null || t == null || s.length() == 0 || t.length() == 0) return "";
    int[] need = new int[128]; // 把 new int[128]; 写入 int[] need
    int required = 0; // 把 0 存入 required
    for (char c : t.toCharArray()) { // for (char 字符 : 另一字符串.toCharArray()) {
      if (need[c]++ == 0) required++; // 若 need[字符] 加一 等于 0) required 加一 ;
    }
    int left = 0, formed = 0; // 把 0, formed 赋值为 0 存入 左边界
    int[] window = new int[128]; // 把 new int[128]; 写入 int[] window
    int minLen = Integer.MAX_VALUE, start = 0; // 把 Integer.MAX_VALUE, 起点 赋值为 0 存入 minLen
    for (int right = 0; right < s.length(); right++) { // 让 右边界 从 0 开始计数，右边界 小于 字符串.长度() 就继续
      char c = s.charAt(right); // 逐字符处理
      window[c]++; // window[字符] 加一 ;
      if (need[c] > 0 && window[c] == need[c])
        formed++; // 若 need[字符] 超过 0 且 window[字符] 等于 need[字符]) formed 加一 ;
      while (formed == required) { // 循环，直到不满足「formed 等于 required」
        if (right - left + 1 < minLen) { // 若 右边界 减 左边界 加 1 小于 minLen
          minLen = right - left + 1; // 把 右边界 减 左边界 加 1; 写入 minLen
          start = left; // 把 左边界; 写入 起点
        }
        char lc = s.charAt(left); // 逐字符处理
        window[lc]--; // window[lc] 减一 ;
        if (need[lc] > 0 && window[lc] < need[lc])
          formed--; // 若 need[lc] 超过 0 且 window[lc] 小于 need[lc]) formed 减一 ;
        left++; // 左边界 加一
      }
    }
    return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (!minWindow("abc", null).equals("")) // 若 取反 minWindow(「abc」, null).equals(「abc」
    throw new RuntimeException("FAILED null"); // throw new RuntimeException(「FAILED null」);
    if (!minWindow("ADOBECODEBANC", "ABC").equals("BANC"))
      throw new RuntimeException("FAILED BANC"); // throw new RuntimeException(「FAILED BANC」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
