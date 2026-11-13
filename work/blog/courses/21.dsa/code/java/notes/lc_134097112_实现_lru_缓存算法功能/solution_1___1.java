// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class LruS1 { // 定义类型
  static class LRUCache { // static class LRUCache {
    int capacity; // int capacity;
    LinkedHashMap<Integer, Integer> data = new LinkedHashMap<>();

    LRUCache(int c) {
      capacity = c;
    } // 把 字符; } 写入 LRUCache(int c) { capacity

    void set(int key, int value) { // 定义函数/方法 set
      if (data.containsKey(key)) data.remove(key); // 若 data.containsKey(key)) data 弹出 key);
      data.put(key, value); // data.put(key, value);
      if (data.size() > capacity) data.remove(data.keySet().iterator().next());
    }

    Integer get(int key) { // 定义函数/方法 get
      if (!data.containsKey(key)) return null; // 若 取反 data.containsKey(key)，直接返回 null
      int value = data.get(key); // 把 data 查找 key) 存入 value
      data.remove(key); // data 弹出 key);
      data.put(key, value); // data.put(key, value);
      return value; // 返回 value
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    LRUCache c = new LRUCache(2); // 把 new LRUCache(2); 写入 LRUCache c
    c.set(1, 1);
    c.set(2, 2); // 字符.set(1, 1); 字符.set(2, 2);
    Integer[] got = new Integer[5]; // 把 new Integer[5]; 写入 Integer[] got
    got[0] = c.get(1); // 把 字符 查找 1); 写入 got[0]
    c.set(3, 3); // 字符.set(3, 3);
    got[1] = c.get(2); // 把 字符 查找 2); 写入 got[1]
    c.set(4, 4); // 字符.set(4, 4);
    got[2] = c.get(1); // 把 字符 查找 1); 写入 got[2]
    got[3] = c.get(3); // 把 字符 查找 3); 写入 got[3]
    got[4] = c.get(4); // 把 字符 查找 4); 写入 got[4]
    Integer[] want = {1, null, null, 3, 4}; // 把 { 1, null, null, 3, 4 }; 写入 Integer[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    if (got.length != want.length) ok = false; // 若 got.长度 不等于 want.长度) ok 赋值为 false;
    else
      for (int i = 0; i < got.length; i++) { // 否则
        if (got[i] == null ? want[i] != null : !got[i].equals(want[i])) {
          ok = false; // 把 false; 写入 ok
          System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
        }
      }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
