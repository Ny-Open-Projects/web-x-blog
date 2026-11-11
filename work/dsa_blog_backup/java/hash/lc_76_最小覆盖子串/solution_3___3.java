// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133465616
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc76_solution33 { // 定义类型
  static String minWindow(String s, String t) { // 定义函数/方法 minWindow
    if (s == null || t == null || s.length() == 0 || t.length() == 0) return "";
    Map<Character, Integer> need =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> need
    for (char c : t.toCharArray()) need.put(c, need.getOrDefault(c, 0) + 1);
    int mSize = need.size(); // 把 need.大小() 存入 mSize
    int l = 0; // 把 0 存入 左指针
    String res = ""; // 把 「」 存入 结果
    for (int r = 0; r < s.length(); r++) { // 让 右指针 从 0 开始计数，右指针 小于 字符串.长度() 就继续
      char c = s.charAt(r); // 逐字符处理
      if (need.containsKey(c)) { // 若 need.containsKey(字符
        need.put(c, need.get(c) - 1); // need.put(字符, need 查找 字符) 减 1);
        if (need.get(c) == 0) mSize--; // 若 need 查找 字符) 等于 0) mSize 减一 ;
      }
      while (mSize == 0) { // 循环，直到不满足「mSize 等于 0」
        String newRes = s.substring(l, r + 1); // 把 字符串 截取 左指针, 右指针 加 1) 存入 newRes
        if (res.isEmpty() || newRes.length() < res.length())
          res = newRes; // 若 结果.isEmpty() 或 newRes.长度() 小于 结果.长度()) 结果 赋值为 newRes;
        char c2 = s.charAt(l); // 逐字符处理
        if (need.containsKey(c2)) { // 若 need.containsKey(c2
          need.put(c2, need.get(c2) + 1); // need.put(c2, need 查找 c2) 加 1);
          if (need.get(c2) == 1) mSize++; // 若 need 查找 c2) 等于 1) mSize 加一 ;
        }
        l++; // 左指针 加一
      }
    }
    return res; // 返回 结果
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
