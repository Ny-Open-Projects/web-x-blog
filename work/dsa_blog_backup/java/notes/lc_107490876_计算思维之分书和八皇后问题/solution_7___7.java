// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  List<int[]> positions; // List 小于 int[] 超过 positions;
  List<int[]> solutions; // List 小于 int[] 超过 solutions;

  boolean safe(int r, int c) { // 定义函数/方法 safe
    for (int[] p : positions) // for (int[] 节点 : positions)
    if (p[0] == r || Math.abs(p[0] - r) == Math.abs(p[1] - c)) return false;
    return true; // 返回 true
  }

  void solve(int col) { // 定义函数/方法 solve
    if (col == 8) { // 若 col 等于 8
      int[] rows = new int[8]; // 把 new int[8]; 写入 int[] rows
      for (int i = 0; i < 8; i++) rows[i] = positions.get(i)[0]; // 让 下标 i 从 0 开始计数，下标 i 小于 8 就继续
      solutions.add(rows); // solutions 追加 行数);
      return; // return;
    }
    for (int r = 0; r < 8; r++) { // 让 右指针 从 0 开始计数，右指针 小于 8 就继续
      if (safe(r, col)) { // 若 safe(右指针, col
        positions.add(new int[] {r, col}); // positions 追加 new int[]{右指针, col});
        solve(col + 1); // solve(col 加 1);
        positions.remove(positions.size() - 1); // positions 弹出 positions.大小() 减 1);
      }
    }
  }

  List<int[]> nQueens() { // 定义函数/方法 nQueens
    positions = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 positions
    solutions = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 solutions
    solve(0); // solve(0);
    return solutions; // 返回 solutions
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    List<int[]> sols = s.nQueens(); // 把 字符串.nQueens(); 写入 List<int[]> sols
    boolean ok = true; // 把 true; 写入 boolean ok
    if (sols.size() != 92) {
      ok = false;
      System.out.println("FAIL count=" + sols.size());
    }
    if (!Arrays.equals(sols.get(0), new int[] {0, 4, 7, 5, 2, 6, 1, 3})) {
      ok = false;
      System.out.println("FAIL first=" + Arrays.toString(sols.get(0)));
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
