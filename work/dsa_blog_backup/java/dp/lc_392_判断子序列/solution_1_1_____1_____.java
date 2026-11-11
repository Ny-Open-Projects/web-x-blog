// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852792
package com.webfault.dsa; // 引入依赖

class Lc392 { // 定义类型
  boolean isSubsequence(String s, String t) { // 定义判定函数 isSubsequence
    int i = 0; // 把 0 存入 下标 i
    for (int j = 0; j < t.length(); j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 另一字符串.长度() 就继续
      if (i < s.length() && s.charAt(i) == t.charAt(j)) i++;
    }
    return i == s.length(); // 返回 下标 i 等于 字符串.长度()
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc392 s = new Lc392(); // 把 new Lc392(); 写入 Lc392 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!s.isSubsequence("abc", "ahbgdc")) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.isSubsequence("axc", "ahbgdc")) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
