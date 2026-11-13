// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class solution111sortMap { // 定义类型
  public String frequencySort(String s) { // 定义函数/方法 frequencySort
    Map<Character, Integer> map =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> map
    for (char c : s.toCharArray()) { // for (char 字符 : 字符串.toCharArray()) {
      map.put(c, map.getOrDefault(c, 0) + 1); // 映射表.put(字符, 映射表.getOrDefault(字符, 0) 加 1);
    }
    List<Map.Entry<Character, Integer>> arr = new ArrayList<>(map.entrySet());
    arr.sort((a, b) -> b.getValue() - a.getValue()); // 排序
    StringBuilder result = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder result
    for (Map.Entry<Character, Integer> item :
        arr) { // for (Map.Entry 小于 Character, Integer 超过 item : 数组) {
      for (int i = 0; i < item.getValue(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 item.getValue() 就继续
        result.append(item.getKey()); // 把 item.getKey( 追加到列表尾部
      }
    }
    return result.toString(); // 返回 结果.toString()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    solution111sortMap s =
        new solution111sortMap(); // 把 new solution111sortMap(); 写入 solution111sortMap s
    String[] inputs = {"tree", "cccaaa", "Aabb", "", "raaeaedere"};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (String in : inputs) { // for (String in : inputs) {
      String got = s.frequencySort(in); // 把 字符串.frequencySort(in) 存入 got
      if (!isFreqSorted(got, in)) { // 若 取反 isFreqSorted(got, in
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL frequencySort(" + in + ")=" + got); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean isFreqSorted(String r, String input) { // 定义判定函数 isFreqSorted
    if (r == null) return false; // 若 右指针 等于 null，直接返回 false
    Map<Character, Integer> in =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> in
    for (char c : input.toCharArray()) in.put(c, in.getOrDefault(c, 0) + 1);
    Map<Character, Integer> out =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Character, Integer> out
    for (char c : r.toCharArray()) out.put(c, out.getOrDefault(c, 0) + 1);
    if (!in.equals(out)) return false; // 若 取反 in.equals(out)，直接返回 false
    int i = 0; // 把 0 存入 下标 i
    int prev = Integer.MAX_VALUE; // 把 Integer.MAX_VALUE 存入 前一个
    while (i < r.length()) { // 循环，直到不满足「下标 i 小于 右指针.长度(」
      char c = r.charAt(i); // 逐字符处理
      int j = i; // 把 下标 i 存入 下标 j
      while (j < r.length() && r.charAt(j) == c)
        j++; // 循环，直到不满足「下标 j 小于 右指针.长度() 且 右指针 取字符 下标 j) 等于 字符) 下标 j 加一 ;」
      int freq = j - i; // 把 下标 j 减 下标 i 存入 频次表
      if (freq != out.get(c)) return false; // 若 频次表 不等于 out 查找 字符)，直接返回 false
      if (freq > prev) return false; // 若 频次表 超过 前一个，直接返回 false
      prev = freq; // 把 频次表; 写入 前一个
      i = j; // 把 下标 j; 写入 下标 i
    }
    return true; // 返回 true
  }
}
