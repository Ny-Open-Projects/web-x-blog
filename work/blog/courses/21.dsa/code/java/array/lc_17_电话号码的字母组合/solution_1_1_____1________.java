// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc17_solution111 { // 定义类型
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

  public static List<String> letterCombinations(String digits) {
    if (digits == null || digits.length() < 1) return new ArrayList<>();
    List<String> code = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> code
    for (char item : digits.toCharArray()) if (map.containsKey(item)) code.add(map.get(item));
    return comb(code); // 返回 comb(code)
  }

  static List<String> comb(List<String> arr) { // 定义函数/方法 comb
    if (arr.size() == 1) { // 若 数组.大小() 等于 1
      List<String> out = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> out
      for (char c : arr.get(0).toCharArray()) out.add(String.valueOf(c));
      return out; // 返回 out
    }
    List<String> tmp = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> tmp
    for (char a : arr.get(0).toCharArray()) // for (char 数组 : 数组 查找 0).toCharArray())
    for (String b :
          comb(arr.subList(1, arr.size()))) // for (String b : comb(数组.subList(1, 数组.大小())))
      tmp.add(a + b); // 临时变量 追加 数组 加 b);
    return tmp; // 返回 临时变量
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
