// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354494
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class AuthS1 { // 定义类型
  static class AuthenticationManager { // static class AuthenticationManager {
    Map<String, Integer> expiresAt =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<String, Integer> expiresAt
    int ttl; // int ttl;

    AuthenticationManager(int timeToLive) {
      ttl = timeToLive;
    }

    void generate(String token, int currentTime) {
      expiresAt.put(token, currentTime + ttl);
    }

    int renew(String token, int currentTime) { // 定义函数/方法 renew
      if (expiresAt.containsKey(token) && expiresAt.get(token) > currentTime) {
        expiresAt.put(token, currentTime + ttl); // expiresAt.put(token, currentTime 加 ttl);
        return 1; // 返回 1
      }
      return 0; // 返回 0
    }

    int countValidTokens(int currentTime) { // 定义函数/方法 countValidTokens
      int count = 0; // 把 0 存入 计数
      for (int expire : expiresAt.values()) if (expire > currentTime) count++;
      return count; // 返回 计数
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    AuthenticationManager auth = new AuthenticationManager(5);
    auth.generate("aaa", 1); // auth.generate(「aaa」, 1);
    Integer[] got = { // 把 { 写入 Integer[] got
      auth.countValidTokens(3), auth.renew("aaa", 4), auth.countValidTokens(6),
    };
    Integer[] want = {1, 1, 1}; // 把 { 1, 1, 1 }; 写入 Integer[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (!got[i].equals(want[i])) { // 若 取反 got[下标 i].equals(want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
