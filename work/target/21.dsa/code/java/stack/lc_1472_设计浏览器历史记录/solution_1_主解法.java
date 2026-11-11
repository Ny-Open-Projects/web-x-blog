// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354313
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1472_solution1 { // 定义类型
  static class BrowserHistory { // static class BrowserHistory {
    List<String> history = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> history
    int current = 0; // 把 0 存入 current

    BrowserHistory(String homepage) {
      history.add(homepage);
      current = 0;
    }

    void visit(String url) { // 定义函数/方法 visit
      history = new ArrayList<>(history.subList(0, current + 1));
      history.add(url); // history 追加 url);
      current = history.size() - 1; // 把 history.大小() 减 1; 写入 current
    }

    String back(int steps) {
      current = Math.max(0, current - steps);
      return history.get(current);
    }

    String forward(int steps) {
      current = Math.min(history.size() - 1, current + steps);
      return history.get(current);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    BrowserHistory b =
        new BrowserHistory(
            "leetcode.com"); // 把 new BrowserHistory(「leetcode.com」); 写入 BrowserHistory b
    b.visit("google.com"); // b.visit(「google.com」);
    b.visit("facebook.com"); // b.visit(「facebook.com」);
    b.visit("youtube.com"); // b.visit(「youtube.com」);
    List<String> out = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> out
    out.add(b.back(1)); // out 追加 b.back(1));
    out.add(b.forward(2)); // out 追加 b.forward(2));
    List<String> want = Arrays.asList("facebook.com", "youtube.com");
    if (!out.equals(want)) throw new RuntimeException("FAILED " + out);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
