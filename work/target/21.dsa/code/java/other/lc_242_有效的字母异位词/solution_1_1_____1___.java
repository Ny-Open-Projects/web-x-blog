// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355461
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

// LeetCode 242. 有效的字母异位词（排序法）
// 忠实翻译 Python 参考实现：Counter(s) == Counter(t)
class lc242_solution111 { // 定义类型
  boolean isAnagram(String s, String t) { // 定义判定函数 isAnagram
    if (s.length() != t.length()) return false; // 若 字符串.长度() 不等于 另一字符串.长度()，直接返回 false
    char[] a = s.toCharArray(); // 把 字符串.toCharArray(); 写入 char[] a
    char[] b = t.toCharArray(); // 把 另一字符串.toCharArray(); 写入 char[] b
    Arrays.sort(a); // 排序
    Arrays.sort(b); // 排序
    return Arrays.equals(a, b); // 返回 Arrays.equals(数组, b)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 用例来自 _tools/correctness_check.py PROBLEMS["lc_242_有效的字母异位词"]
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {"anagram", "nagaram", true},
      {"rat", "car", false},
      {"aacc", "ccac", false},
    };
    lc242_solution111 s =
        new lc242_solution111(); // 把 new lc242_solution111(); 写入 lc242_solution111 s
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
