// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130470370
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Q933S2 { // 定义类型
  static class RecentCounter { // static class RecentCounter {
    List<Integer> queue = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> queue
    int front = 0; // 把 0 存入 front

    int ping(int t) { // 定义函数/方法 ping
      queue.add(t); // 队列 追加 另一字符串);
      while (queue.get(front) < t - 3000)
        front++; // 循环，直到不满足「队列 查找 front) 小于 另一字符串 减 3000) front 加一 ;」
      return queue.size() - front; // 返回 队列.大小() 减 front
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
