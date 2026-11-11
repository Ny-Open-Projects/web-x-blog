// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133465616
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc76_solution22 { // 定义类型
  static String minWindow(String s, String t) { // 定义函数/方法 minWindow
    if (s == null || t == null || s.isEmpty() || t.isEmpty()) return "";
    Map<Character, Integer> target =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> target
    for (char c : t.toCharArray()) target.put(c, target.getOrDefault(c, 0) + 1);
    int required = target.size(); // 把 目标值.大小() 存入 required
    Map<Character, Integer> window =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> window
    int left = 0, formed = 0, minLen = Integer.MAX_VALUE, minLeft = 0;
    for (int right = 0; right < s.length(); right++) { // 让 右边界 从 0 开始计数，右边界 小于 字符串.长度() 就继续
      char c = s.charAt(right); // 逐字符处理
      window.put(
          c, window.getOrDefault(c, 0) + 1); // window.put(字符, window.getOrDefault(字符, 0) 加 1);
      if (target.containsKey(c) && window.get(c).intValue() == target.get(c).intValue()) formed++;
      while (left <= right && formed == required) { // 循环，直到不满足「左边界 不超过 右边界 且 formed 等于 required」
        char lc = s.charAt(left); // 逐字符处理
        if (right - left + 1 < minLen) {
          minLen = right - left + 1;
          minLeft = left;
        }
        window.put(lc, window.get(lc) - 1); // window.put(lc, window 查找 lc) 减 1);
        if (target.containsKey(lc) && window.get(lc) < target.get(lc)) formed--;
        left++; // 左边界 加一
      }
    }
    return (minLen == Integer.MAX_VALUE) ? "" : s.substring(minLeft, minLeft + minLen);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (!minWindow("ADOBECODEBANC", "ABC").equals("BANC"))
      throw new RuntimeException("FAILED BANC"); // throw new RuntimeException(「FAILED BANC」);
    if (!minWindow("a", "a").equals("a")) // 若 取反 minWindow(「数组」, 「数组」).equals(「数组」
    throw new RuntimeException("FAILED a"); // throw new RuntimeException(「FAILED 数组」);
    if (!minWindow("a", "aa").equals("")) // 若 取反 minWindow(「数组」, 「数组」).equals(「数组」
    throw new RuntimeException("FAILED aa"); // throw new RuntimeException(「FAILED aa」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
