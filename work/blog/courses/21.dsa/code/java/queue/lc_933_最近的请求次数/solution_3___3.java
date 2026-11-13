// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Q933S3 { // 定义类型
  static class RecentCounter { // static class RecentCounter {
    Deque<Integer> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> q

    int ping(int t) { // 定义函数/方法 ping
      q.addLast(t); // 节点.addLast(另一字符串);
      while (q.peekFirst() < t - 3000)
        q.pollFirst(); // 循环，直到不满足「节点.peekFirst() 小于 另一字符串 减 3000) 节点.pollFirst();」
      return q.size(); // 返回 节点.大小()
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    RecentCounter counter = new RecentCounter(); // 把 new RecentCounter(); 写入 RecentCounter counter
    List<Integer> got = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> got
    got.add(counter.ping(1)); // got 追加 counter.ping(1));
    got.add(counter.ping(100)); // got 追加 counter.ping(100));
    got.add(counter.ping(3001)); // got 追加 counter.ping(3001));
    List<Integer> want = Arrays.asList(1, 2, 3); // 把 Arrays.asList(1, 2, 3); 写入 List<Integer> want
    boolean ok = got.equals(want); // 把 got.equals(want); 写入 boolean ok
    if (!ok) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
