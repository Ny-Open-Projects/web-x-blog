// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  boolean valid(int x, List<Integer> a) { // 定义函数/方法 valid
    int y = a.size() + 1; // 把 数组.大小() 加 1 存入 y
    for (int i = 1; i < y; i++) // 让 下标 i 从 1 开始计数，下标 i 小于 y 就继续
    if (x == a.get(i - 1) || Math.abs(y - i) == Math.abs(x - a.get(i - 1))) return false;
    return true; // 返回 true
  }

  List<List<Integer>> nQueens() { // 定义函数/方法 nQueens
    List<List<Integer>> solutions =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> solutions
    Deque<List<Integer>> stack =
        new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<List<Integer>> stack
    stack.push(new ArrayList<>()); // 把 new ArrayList 小于 超过 ( 压入栈/数组尾部
    while (!stack.isEmpty()) { // 循环，直到不满足「取反 栈.isEmpty(」
      List<Integer> a = stack.pop(); // 弹出栈顶元素
      if (a.size() == 8) solutions.add(a); // 若 数组.大小() 等于 8) solutions 追加 数组);
      else { // 否则
        for (int i = 1; i <= 8; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 8 就继续
          if (valid(i, a)) { // 若 valid(下标 i, 数组
            List<Integer> na =
                new ArrayList<>(a); // 把 new ArrayList 小于 超过 (数组); 写入 List<Integer> na
            na.add(i); // na 追加 下标 i);
            stack.push(na); // 把 na 压入栈/数组尾部
          }
        }
      }
    }
    return solutions; // 返回 solutions
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    List<List<Integer>> sols = s.nQueens(); // 把 字符串.nQueens(); 写入 List<List<Integer>> sols
    boolean ok = true; // 把 true; 写入 boolean ok
    if (sols.size() != 92) {
      ok = false;
      System.out.println("FAIL count=" + sols.size());
    }
    List<Integer> first = sols.get(0); // 把 sols 查找 0); 写入 List<Integer> first
    List<Integer> want =
        Arrays.asList(
            8, 4, 1, 3, 6, 2, 7, 5); // 把 Arrays.asList(8,4,1,3,6,2,7,5); 写入 List<Integer> want
    if (!first.equals(want)) {
      ok = false;
      System.out.println("FAIL first=" + first);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
