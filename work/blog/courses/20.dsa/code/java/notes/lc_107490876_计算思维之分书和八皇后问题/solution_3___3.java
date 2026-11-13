// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  int[] board = new int[8]; // 把 new int[8]; 写入 int[] board
  List<int[]> results; // List 小于 int[] 超过 results;

  boolean isSafe(int col, int row) { // 定义判定函数 isSafe
    for (int c = 0; c < col; c++) // 让 字符 从 0 开始计数，字符 小于 col 就继续
    if (board[c] == row || Math.abs(board[c] - row) == Math.abs(c - col)) return false;
    return true; // 返回 true
  }

  void place(int col) { // 定义函数/方法 place
    if (col == 8) {
      results.add(board.clone());
      return;
    } // 若 col 等于 8) { results 追加 棋盘.clone()); return; }
    for (int row = 1; row <= 8; row++) { // 让 row 从 1 开始计数，row 不超过 8 就继续
      if (isSafe(col, row)) {
        board[col] = row;
        place(col + 1);
      } // 若 isSafe(col, row)) { 棋盘[col] 赋值为 row; place(col 加 1); }
    }
  }

  List<int[]> nQueens() { // 定义函数/方法 nQueens
    results = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 results
    board = new int[8]; // 把 new int[8]; 写入 棋盘
    place(0); // place(0);
    return results; // 返回 results
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    List<int[]> sols = s.nQueens(); // 把 字符串.nQueens(); 写入 List<int[]> sols
    boolean ok = true; // 把 true; 写入 boolean ok
    if (sols.size() != 92) {
      ok = false;
      System.out.println("FAIL count=" + sols.size());
    }
    if (!Arrays.equals(sols.get(0), new int[] {1, 5, 8, 6, 3, 7, 2, 4})) {
      ok = false;
      System.out.println("FAIL first=" + Arrays.toString(sols.get(0)));
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
