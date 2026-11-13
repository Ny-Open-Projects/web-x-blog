// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc17_solution633 { // 定义类型
  static List<String> letterCombinations(String digits) { // 定义函数/方法 letterCombinations
    List<String> combos = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> combos
    if (digits == null || digits.isEmpty())
      return combos; // 若 digits 等于 null 或 digits.isEmpty()，直接返回 combos
    Map<Character, String> mapping =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, String> mapping
    mapping.put('2', "abc");
    mapping.put('3', "def");
    mapping.put('4', "ghi");
    mapping.put('5', "jkl");
    mapping.put('6', "mno");
    mapping.put('7', "pqrs");
    mapping.put('8', "tuv");
    mapping.put('9', "wxyz"); // mapping.put('8', 「tuv」); mapping.put('9', 「tuv」);
    combos.add(""); // combos 追加 「」);
    for (char d : digits.toCharArray()) { // for (char d : digits.toCharArray()) {
      List<String> newCombos =
          new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> newCombos
      for (String p : combos) // for (String 节点 : combos)
      for (char c : mapping.get(d).toCharArray()) newCombos.add(p + c);
      combos = newCombos; // 把 newCombos; 写入 combos
    }
    return combos; // 返回 combos
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<String> r = letterCombinations("23"); // 把 letterCombinations(「23」); 写入 List<String> r
    Collections.sort(r); // 排序
    List<String> exp = Arrays.asList("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf");
    if (!r.equals(exp))
      throw new RuntimeException(
          "FAILED"); // 若 取反 右指针.equals(exp)) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
