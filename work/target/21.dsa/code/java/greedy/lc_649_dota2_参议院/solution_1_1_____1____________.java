// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244562
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc649_solution111 { // 定义类型
  static String predictPartyVictory(String senate) { // 定义函数/方法 predictPartyVictory
    int n = senate.length(); // 把 senate.长度() 存入 元素个数
    Queue<Integer> radiant =
        new LinkedList<>(); // 把 new LinkedList 小于 超过 (); 写入 Queue<Integer> radiant
    Queue<Integer> dire = new LinkedList<>(); // 把 new LinkedList 小于 超过 (); 写入 Queue<Integer> dire
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if (senate.charAt(i) == 'R')
        radiant.offer(i); // 若 senate 取字符 下标 i) 等于 'R') radiant.offer(下标 i);
      else dire.offer(i); // 否则
    }
    while (!radiant.isEmpty()
        && !dire.isEmpty()) { // 循环，直到不满足「取反 radiant.isEmpty() 且 取反 dire.isEmpty(」
      int r = radiant.poll(); // 把 radiant.poll() 存入 右指针
      int d = dire.poll(); // 把 dire.poll() 存入 d
      if (r < d) radiant.offer(r + n); // 若 右指针 小于 d) radiant.offer(右指针 加 元素个数);
      else dire.offer(d + n); // 否则
    }
    return !radiant.isEmpty()
        ? "Radiant"
        : "Dire"; // 返回 取反 radiant.isEmpty() ? 「Radiant」 : 「Radiant」
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (!predictPartyVictory("RD").equals("Radiant")) // 若 取反 predictPartyVictory(「RD」).equals(「RD」
    throw new RuntimeException("FAILED RD"); // throw new RuntimeException(「FAILED RD」);
    if (!predictPartyVictory("RRRDDD")
        .equals("Radiant")) // 若 取反 predictPartyVictory(「RRRDDD」).equals(「RRRDDD」
    throw new RuntimeException("FAILED RRRDDD"); // throw new RuntimeException(「FAILED RRRDDD」);
    if (!predictPartyVictory("DDR").equals("Dire")) // 若 取反 predictPartyVictory(「DDR」).equals(「DDR」
    throw new RuntimeException("FAILED DDR"); // throw new RuntimeException(「FAILED DDR」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
