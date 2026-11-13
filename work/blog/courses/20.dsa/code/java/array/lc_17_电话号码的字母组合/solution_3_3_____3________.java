// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc17_solution333 { // 定义类型
  static List<String> letterCombinations(String digits) { // 定义函数/方法 letterCombinations
    if (digits == null || digits.length() == 0) return new ArrayList<>();
    Map<Character, String> d =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, String> d
    d.put('2', "abc");
    d.put('3', "def");
    d.put('4', "ghi");
    d.put('5', "jkl");
    d.put('6', "mno");
    d.put('7', "pqrs");
    d.put('8', "tuv");
    d.put('9', "wxyz");
    List<String> res = new ArrayList<>();
    res.add(""); // 把 new ArrayList 小于 超过 (); 结果 追加 「」); 写入 List<String> res
    for (char ch : digits.toCharArray()) { // for (char 字符 : digits.toCharArray()) {
      List<String> nw = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> nw
      for (String p : res) for (char c : d.get(ch).toCharArray()) nw.add(p + c);
      res = nw; // 把 nw; 写入 结果
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<String> a = letterCombinations("23"); // 把 letterCombinations(「23」); 写入 List<String> a
    Collections.sort(a); // 排序
    List<String> exp = Arrays.asList("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf");
    if (!a.equals(exp)) throw new RuntimeException("FAILED a");
    if (!letterCombinations("").isEmpty()) throw new RuntimeException("FAILED b");
    List<String> c = letterCombinations("2"); // 把 letterCombinations(「2」); 写入 List<String> c
    Collections.sort(c); // 排序
    if (!c.equals(Arrays.asList("a", "b", "c"))) throw new RuntimeException("FAILED c");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
