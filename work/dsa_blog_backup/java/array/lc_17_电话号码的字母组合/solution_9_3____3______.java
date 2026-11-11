// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130444168
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc17_solution933 { // 定义类型
  public List<String> letterCombinations(String digits) { // 定义函数/方法 letterCombinations
    List<String> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> res
    if (digits == null || digits.length() == 0)
      return res; // 若 digits 等于 null 或 digits.长度() 等于 0，直接返回 结果
    String[] phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    res.add(""); // 结果 追加 「」);
    for (char d : digits.toCharArray()) { // for (char d : digits.toCharArray()) {
      String letters = phone[d - '0']; // 把 phone[d 减 '0'] 存入 letters
      List<String> next = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> next
      for (String comb : res) { // for (String comb : 结果) {
        for (char c : letters.toCharArray())
          next.add(comb + c); // for (char 字符 : letters.toCharArray()) 下一个 追加 comb 加 字符);
      }
      res = next; // 把 下一个; 写入 结果
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc17_solution933 s = new lc17_solution933(); // 把 new lc17_solution933(); 写入 lc17_solution933 s
    if (!s.letterCombinations("").isEmpty()) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
