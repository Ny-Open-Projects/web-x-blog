// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355461
package com.webfault.dsa; // 引入依赖

import java.util.HashMap; // 引入依赖
import java.util.Map; // 引入依赖

// LeetCode 242. 有效的字母异位词（哈希计数法）
// 忠实翻译 Python 参考实现：Counter(s) == Counter(t)
class lc242_solution222 { // 定义类型
  boolean isAnagram(String s, String t) { // 定义判定函数 isAnagram
    if (s.length() != t.length()) return false; // 若 字符串.长度() 不等于 另一字符串.长度()，直接返回 false
    Map<Character, Integer> cnt =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> cnt
    for (int i = 0; i < s.length(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.长度() 就继续
      char c = s.charAt(i); // 逐字符处理
      cnt.put(c, cnt.getOrDefault(c, 0) + 1); // 计数.put(字符, 计数.getOrDefault(字符, 0) 加 1);
    }
    for (int i = 0; i < t.length(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 另一字符串.长度() 就继续
      char c = t.charAt(i); // 逐字符处理
      cnt.put(c, cnt.getOrDefault(c, 0) - 1); // 计数.put(字符, 计数.getOrDefault(字符, 0) 减 1);
      if (cnt.get(c) < 0) return false; // 若 计数 查找 字符) 小于 0，直接返回 false
    }
    for (int v : cnt.values()) { // for (int 值 : 计数.values()) {
      if (v != 0) return false; // 若 值 不等于 0，直接返回 false
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 用例来自 _tools/correctness_check.py PROBLEMS["lc_242_有效的字母异位词"]
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {"anagram", "nagaram", true},
      {"rat", "car", false},
      {"aacc", "ccac", false},
    };
    lc242_solution222 s =
        new lc242_solution222(); // 把 new lc242_solution222(); 写入 lc242_solution222 s
    boolean allOK = true; // 把 true; 写入 boolean allOK
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      boolean got = s.isAnagram((String) c[0], (String) c[1]);
      boolean want = (Boolean) c[2]; // 把 (Boolean) 字符[2]; 写入 boolean want
      if (got != want) { // 若 got 不等于 want
        allOK = false; // 把 false; 写入 allOK
        System.out.println(
            "FAIL isAnagram(" + c[0] + "," + c[1] + ") = " + got + ", want " + want); // 打印输出
      }
    }
    if (!allOK) { // 若 取反 allOK
      throw new RuntimeException(
          "some cases FAILED"); // throw new RuntimeException(「some cases FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
