// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240399
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc131_solution222 { // 定义类型
  public static List<List<String>> partition(String s) {
    List<List<String>> result =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> result
    backtrack(s, 0, new ArrayList<>(), result); // backtrack(字符串, 0, new ArrayList 小于 超过 (), 结果);
    return result; // 返回 结果
  }

  private static void backtrack(String s, int start, List<String> path, List<List<String>> result) {
    if (start == s.length()) { // 若 起点 等于 字符串.长度(
      result.add(new ArrayList<>(path)); // 结果 追加 new ArrayList 小于 超过 (当前路径));
      return; // return;
    }
    for (int end = start + 1; end <= s.length(); end++) { // 让 终点 从 起点 加 1 开始计数，终点 不超过 字符串.长度() 就继续
      String sub = s.substring(start, end); // 把 字符串 截取 起点, 终点) 存入 sub
      if (isPalindrome(sub)) { // 若 isPalindrome(sub
        path.add(sub); // 当前路径 追加 sub);
        backtrack(s, end, path, result); // backtrack(字符串, 终点, 当前路径, 结果);
        path.remove(path.size() - 1); // 当前路径 弹出 当前路径.大小() 减 1);
      }
    }
  }

  private static boolean isPalindrome(
      String s) { // private static boolean isPalindrome(String 字符串) {
    int i = 0, j = s.length() - 1; // 把 0, 下标 j 赋值为 字符串.长度() 减 1 存入 下标 i
    while (i < j) { // 循环，直到不满足「下标 i 小于 下标 j」
      if (s.charAt(i) != s.charAt(j)) return false; // 若 字符串 取字符 下标 i) 不等于 字符串 取字符 下标 j)，直接返回 false
      i++; // 下标 i 加一
      j--; // 下标 j 减一
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<List<String>> r1 = partition("abc"); // 把 partition(「abc」); 写入 List<List<String>> r1
    List<List<String>> w1 = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> w1
    w1.add(Arrays.asList("a", "b", "c")); // w1 追加 Arrays.asList(「数组」, 「数组」, 「数组」));
    List<List<String>> r2 = partition("aab"); // 把 partition(「aab」); 写入 List<List<String>> r2
    List<List<String>> w2 = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> w2
    w2.add(Arrays.asList("a", "a", "b")); // w2 追加 Arrays.asList(「数组」, 「数组」, 「数组」));
    w2.add(Arrays.asList("aa", "b")); // w2 追加 Arrays.asList(「aa」, 「aa」));
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!eq(r1, w1)) {
      ok = false;
      System.out.println("FAIL abc got " + r1);
    }
    if (!eq(r2, w2)) {
      ok = false;
      System.out.println("FAIL aab got " + r2);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  private static boolean eq(List<List<String>> a, List<List<String>> b) {
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (int i = 0; i < a.size(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
      if (!a.get(i).equals(b.get(i)))
        return false; // 若 取反 数组 查找 下标 i).equals(b 查找 下标 i))，直接返回 false
    }
    return true; // 返回 true
  }
}
