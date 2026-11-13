// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094527
package com.webfault.dsa; // 引入依赖

import java.util.LinkedHashMap; // 引入依赖
// 引入依赖

class LRUCacheSol1 { // 定义类型
  static class LRUCache { // static class LRUCache {
    int cap; // int cap;
    LinkedHashMap<Integer, Integer> m; // LinkedHashMap 小于 Integer, Integer 超过 映射表;

    LRUCache(int c) { // LRUCache(int 字符) {
      cap = c; // 把 字符; 写入 cap
      m = new LinkedHashMap<Integer, Integer>(c, 0.75f, false);
    }

    int get(int k) { // 定义函数/方法 get
      if (!m.containsKey(k)) return -1; // 若 取反 映射表.containsKey(下标 k)，直接返回 减 1
      int v = m.remove(k); // 把 映射表 弹出 下标 k) 存入 值
      m.put(k, v); // 映射表.put(下标 k, 值);
      return v; // 返回 值
    }

    void put(int k, int v) { // 定义函数/方法 put
      if (m.containsKey(k)) { // 若 映射表.containsKey(下标 k
        m.remove(k); // 映射表 弹出 下标 k);
      } else if (m.size() >= cap) { // 否则，若 映射表.大小() 不低于 cap
        int oldest = m.keySet().iterator().next(); // 把 映射表.keySet().iterator().下一个() 存入 oldest
        m.remove(oldest); // 映射表 弹出 oldest);
      }
      m.put(k, v); // 映射表.put(下标 k, 值);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    LRUCache c = new LRUCache(2); // 把 new LRUCache(2); 写入 LRUCache c
    c.put(1, 1); // 字符.put(1, 1);
    c.put(2, 2); // 字符.put(2, 2);
    int g1 = c.get(1); // 把 字符 查找 1) 存入 g1
    c.put(3, 3); // 字符.put(3, 3);
    int g2 = c.get(2); // 把 字符 查找 2) 存入 g2
    c.put(4, 4); // 字符.put(4, 4);
    int g3 = c.get(1); // 把 字符 查找 1) 存入 g3
    int g4 = c.get(3); // 把 字符 查找 3) 存入 g4
    int g5 = c.get(4); // 把 字符 查找 4) 存入 g5
    int[] got = {g1, g2, g3, g4, g5}; // 把 {g1, g2, g3, g4, g5}; 写入 int[] got
    int[] want = {1, -1, -1, 3, 4}; // 把 {1, 减 1, 减 1, 3, 4}; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
