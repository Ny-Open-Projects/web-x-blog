// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  List<String> hanoi(int n, char src, char aux, char dst) { // 定义函数/方法 hanoi
    List<String> moves = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> moves
    h(n, src, aux, dst, moves); // h(元素个数, src, aux, dst, moves);
    return moves; // 返回 moves
  }

  void h(int n, char src, char aux, char dst, List<String> moves) { // 定义函数/方法 h
    if (n == 1) {
      moves.add("" + src + dst);
      return;
    } // 若 元素个数 等于 1) { moves 追加 「」 加 src 加 dst); return; }
    h(n - 1, src, dst, aux, moves); // h(元素个数 减 1, src, dst, aux, moves);
    moves.add("" + src + dst); // moves 追加 「」 加 src 加 dst);
    h(n - 1, aux, src, dst, moves); // h(元素个数 减 1, aux, src, dst, moves);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    List<String> got =
        s.hanoi(3, 'A', 'B', 'C'); // 把 字符串.hanoi(3, 'A', 'B', 'C'); 写入 List<String> got
    List<String> want = Arrays.asList("AC", "AB", "CB", "AC", "BA", "BC", "AC");
    List<String> got1 =
        s.hanoi(1, 'A', 'B', 'C'); // 把 字符串.hanoi(1, 'A', 'B', 'C'); 写入 List<String> got1
    List<String> want1 = Arrays.asList("AC"); // 把 Arrays.asList(「AC」); 写入 List<String> want1
    boolean ok =
        got.equals(want)
            && got1.equals(want1); // 把 got.equals(want) 且 got1.equals(want1); 写入 boolean ok
    if (!ok) {
      System.out.println("FAIL got=" + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
