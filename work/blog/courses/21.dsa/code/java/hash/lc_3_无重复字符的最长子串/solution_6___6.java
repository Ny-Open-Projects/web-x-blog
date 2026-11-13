// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133461048
package com.webfault.dsa; // 引入依赖

import java.util.HashMap; // 引入依赖
import java.util.Map; // 引入依赖

class lc3_solution66 { // 定义类型
  // lengthOfLongestSubstring 忠实翻译 python ref solution_6___6.py（last 出现位置字典）
  public int lengthOfLongestSubstring(String s) { // 定义函数/方法 lengthOfLongestSubstring
    Map<Character, Integer> last =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> last
    int l = 0; // 把 0 存入 左指针
    int res = 0; // 把 0 存入 结果
    for (int r = 0; r < s.length(); r++) { // 让 右指针 从 0 开始计数，右指针 小于 字符串.长度() 就继续
      char ch = s.charAt(r); // 逐字符处理
      Integer li = last.get(ch); // 把 last 查找 字符) 存入 li
      if (li != null && li >= l) { // 若 li 不等于 null 且 li 不低于 左指针
        l = li + 1; // 把 li 加 1; 写入 左指针
      }
      res = Math.max(res, r - l + 1); // 把 Math.取较大值 结果, 右指针 减 左指针 加 1); 写入 结果
      last.put(ch, r); // last.put(字符, 右指针);
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc3_solution66 s = new lc3_solution66(); // 把 new lc3_solution66(); 写入 lc3_solution66 s
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
