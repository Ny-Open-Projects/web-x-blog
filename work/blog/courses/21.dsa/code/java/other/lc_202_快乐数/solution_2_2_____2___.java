// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355335
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class HappyS2 { // 定义类型
  static boolean getNum(int n) { // 定义函数/方法 getNum
    Set<Integer> seen = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> seen
    while (n != 1) { // 循环，直到不满足「元素个数 不等于 1」
      if (seen.contains(n)) return false; // 若 已见集合 是否包含 元素个数)，直接返回 false
      seen.add(n); // 已见集合 追加 元素个数);
      int sum = 0; // 把 0 存入 累计和
      for (char c :
          String.valueOf(n).toCharArray()) { // for (char 字符 : String.valueOf(元素个数).toCharArray()) {
        int d = c - '0'; // 把 字符 减 '0' 存入 d
        sum += d * d; // 累计和累加 d 乘 d
      }
      n = sum; // 把 累计和; 写入 元素个数
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean[] got = { // 把 { 写入 boolean[] got
      HappyS2.getNum(1), HappyS2.getNum(19), HappyS2.getNum(2),
    };
    boolean[] want = {true, true, false}; // 把 { true, true, false }; 写入 boolean[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL getNum idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
