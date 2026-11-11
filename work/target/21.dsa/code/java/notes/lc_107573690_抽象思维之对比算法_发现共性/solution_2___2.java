// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static final int[][] MOVES = {{1, 2}, {2, 1}, {2, -1}, {1, -2}};

  static int horseJumpRefactored() { // 定义函数/方法 horseJumpRefactored
    int[] count = {0}; // 把 {0}; 写入 int[] count
    dfs(0, 0, count); // dfs(0, 0, 计数);
    return count[0]; // 返回 计数[0]
  }

  static void dfs(int x, int y, int[] count) { // 定义函数/方法 dfs
    if (x == 8 && y == 4) {
      count[0]++;
      return;
    } // 若 x 等于 8 且 y 等于 4) { 计数[0] 加一 ; return; }
    if (!(0 <= x && x <= 8 && 0 <= y && y <= 4))
      return; // 若 取反 (0 不超过 x 且 x 不超过 8 且 0 不超过 y 且 y 不超过 4)) return;
    for (int k = 0; k < 4; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
      int nx = x + MOVES[k][0]; // 把 x 加 MOVES[下标 k][0] 存入 nx
      int ny = y + MOVES[k][1]; // 把 y 加 MOVES[下标 k][1] 存入 ny
      dfs(nx, ny, count); // dfs(nx, ny, 计数);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int got = horseJumpRefactored(); // 把 horseJumpRefactored() 存入 got
    if (got != 37) {
      System.out.println("FAIL got " + got + " want 37");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
