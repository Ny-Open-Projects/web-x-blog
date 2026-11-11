// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型
  public String customSortString(String order, String s) { // 定义函数/方法 customSortString
    Map<Character, Integer> count =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> count
    for (char c : s.toCharArray()) count.put(c, count.getOrDefault(c, 0) + 1);
    StringBuilder result = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder result
    for (char c : order.toCharArray()) { // for (char 字符 : order.toCharArray()) {
      if (count.containsKey(c)) { // 若 计数.containsKey(字符
        for (int t = 0; t < count.get(c); t++)
          result.append(c); // 让 另一字符串 从 0 开始计数，另一字符串 小于 计数 查找 字符) 就继续
        count.remove(c); // 计数 弹出 字符);
      }
    }
    for (Map.Entry<Character, Integer> e :
        count.entrySet()) { // for (Map.Entry 小于 Character, Integer 超过 e : 计数.entrySet()) {
      for (int t = 0; t < e.getValue(); t++)
        result.append(e.getKey()); // 让 另一字符串 从 0 开始计数，另一字符串 小于 e.getValue() 就继续
    }
    return result.toString(); // 返回 结果.toString()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[][] ins = {
      {"cba", "abcd"}, {"cbafg", "abcd"}
    }; // 把 {{「cba」,「cba」},{「cba」,「cba」}}; 写入 String[][] ins
    String[] wants = {"cbad", "cbad"}; // 把 {「cbad」,「cbad」}; 写入 String[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      String got =
          s.customSortString(
              ins[i][0], ins[i][1]); // 把 字符串.customSortString(ins[下标 i][0], ins[下标 i][1]) 存入 got
      if (!got.equals(wants[i])) {
        ok = false;
        System.out.println("FAIL " + ins[i][0] + "," + ins[i][1] + "=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
