// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355797
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  static boolean canConstruct(String ransomNote, String magazine) { // 定义函数/方法 canConstruct
    if (ransomNote.length() > magazine.length())
      return false; // 若 ransomNote.长度() 超过 magazine.长度()，直接返回 false
    int[] cnt = new int[26]; // 把 new int[26]; 写入 int[] cnt
    for (char c : magazine.toCharArray())
      cnt[c - 'a']++; // for (char 字符 : magazine.toCharArray()) 计数[字符 减 '数组'] 加一 ;
    for (char c : ransomNote.toCharArray()) { // for (char 字符 : ransomNote.toCharArray()) {
      cnt[c - 'a']--; // 计数[字符 减 '数组'] 减一 ;
      if (cnt[c - 'a'] < 0) return false; // 若 计数[字符 减 '数组'] 小于 0，直接返回 false
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[] r = {"a", "aa", "aa"}; // 把 {「数组」, 「数组」, 「数组」}; 写入 String[] r
    String[] m = {"b", "ab", "aab"}; // 把 {「b」, 「b」, 「b」}; 写入 String[] m
    boolean[] want = {false, false, true}; // 把 {false, false, true}; 写入 boolean[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < r.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 右指针.长度 就继续
      boolean got =
          canConstruct(r[i], m[i]); // 把 canConstruct(右指针[下标 i], 映射表[下标 i]); 写入 boolean got
      if (got != want[i]) { // 若 got 不等于 want[下标 i]
        System.out.println(
            "FAIL ransom=" + r[i] + " mag=" + m[i] + " want=" + want[i] + " got=" + got); // 打印输出
        ok = false; // 把 false; 写入 ok
      }
    }
    if (!ok) {
      System.out.println("RESULT: FAIL");
      System.exit(1);
    } // 若 取反 ok) { System.out.输出(「RESULT: FAIL」); System.exit(1); }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
