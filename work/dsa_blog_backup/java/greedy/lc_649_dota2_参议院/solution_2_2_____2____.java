// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145244562
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc649_solution222 { // 定义类型
  static String predictPartyVictory(String senate) { // 定义函数/方法 predictPartyVictory
    Queue<Character> queue =
        new LinkedList<>(); // 把 new LinkedList 小于 超过 (); 写入 Queue<Character> queue
    for (char c : senate.toCharArray())
      queue.offer(c); // for (char 字符 : senate.toCharArray()) 队列.offer(字符);
    Deque<Character> stack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Character> stack
    while (!queue.isEmpty()) { // 循环，直到不满足「取反 队列.isEmpty(」
      char s = queue.poll(); // 把 队列.poll(); 写入 char s
      if (stack.isEmpty() || stack.peekLast() == s) { // 若 栈.isEmpty() 或 栈.peekLast() 等于 字符串
        stack.addLast(s); // 栈.addLast(字符串);
      } else { // 否则
        queue.offer(stack.pollLast()); // 队列.offer(栈.pollLast());
      }
    }
    char top = stack.peekLast(); // 把 栈.peekLast(); 写入 char top
    return top == 'R' ? "Radiant" : "Dire"; // 返回 top 等于 'R' ? 「Radiant」 : 「Radiant」
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
