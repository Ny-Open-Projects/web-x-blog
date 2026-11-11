// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc17_solution711 { // 定义类型
  static List<String> res =
      new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 static List<String> res
  static Map<Character, String> map =
      new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 static Map<Character, String> map

  static { // static {
    map.put('2', "abc");
    map.put('3', "def");
    map.put('4', "ghi");
    map.put('5', "jkl");
    map.put('6', "mno");
    map.put('7', "pqrs");
    map.put('8', "tuv");
    map.put('9', "wxyz"); // 映射表.put('8', 「tuv」); 映射表.put('9', 「tuv」);
  }

  static void backtrack(StringBuilder path, int index, String digits) { // 定义函数/方法 backtrack
    if (index == digits.length()) {
      res.add(path.toString());
      return;
    } // 若 index 等于 digits.长度()) { 结果 追加 当前路径.toString()); return; }
    for (char c : map.get(digits.charAt(index)).toCharArray()) { // 逐字符处理
      path.append(c); // 把 字符 追加到列表尾部
      backtrack(path, index + 1, digits); // backtrack(当前路径, index 加 1, digits);
      path.deleteCharAt(path.length() - 1); // 当前路径.deleteCharAt(当前路径.长度() 减 1);
    }
  }

  static List<String> letterCombinations(String digits) { // 定义函数/方法 letterCombinations
    res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 结果
    if (digits == null || digits.length() == 0)
      return res; // 若 digits 等于 null 或 digits.长度() 等于 0，直接返回 结果
    backtrack(new StringBuilder(), 0, digits); // backtrack(new StringBuilder(), 0, digits);
    return res; // 返回 结果
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
