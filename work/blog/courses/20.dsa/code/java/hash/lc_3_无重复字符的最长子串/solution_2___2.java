// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133461048
package com.webfault.dsa; // 引入依赖

import java.util.HashSet; // 引入依赖
import java.util.Set; // 引入依赖

class lc3_solution22 { // 定义类型
  // lengthOfLongestSubstring 忠实翻译 python ref solution_2___2.py（set 滑窗）
  public int lengthOfLongestSubstring(String s) { // 定义函数/方法 lengthOfLongestSubstring
    Set<Character> charSet = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Character> charSet
    int left = 0; // 把 0 存入 左边界
    int maxLen = 0; // 把 0 存入 maxLen
    for (int right = 0; right < s.length(); right++) { // 让 右边界 从 0 开始计数，右边界 小于 字符串.长度() 就继续
      char c = s.charAt(right); // 逐字符处理
      while (charSet.contains(c)) { // 循环，直到不满足「charSet 是否包含 字符」
        charSet.remove(s.charAt(left)); // 逐字符处理
        left++; // 左边界 加一
      }
      charSet.add(c); // charSet 追加 字符);
      maxLen = Math.max(maxLen, right - left + 1); // 把 Math.取较大值 maxLen, 右边界 减 左边界 加 1); 写入 maxLen
    }
    return maxLen; // 返回 maxLen
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc3_solution22 s = new lc3_solution22(); // 把 new lc3_solution22(); 写入 lc3_solution22 s
    String[][] cases = { // 把 { 写入 String[][] cases
      {"abcabcbb", "3"},
      {"pwwkew", "3"},
      {"", "0"},
      {" ", "1"},
      {"dvdf", "3"},
      {"abba", "2"},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (String[] c : cases) { // for (String[] 字符 : cases) {
      int got = s.lengthOfLongestSubstring(c[0]); // 把 字符串.lengthOfLongestSubstring(字符[0]) 存入 got
      int want = Integer.parseInt(c[1]); // 把 Integer.转整数(字符[1]) 存入 want
      if (got != want) { // 若 got 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL solve(\"" + c[0] + "\")=" + got + " want " + want); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
