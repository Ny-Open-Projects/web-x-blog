// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static int[] bestMatchWindow(int[] bg, int[] puzzle) { // 定义函数/方法 bestMatchWindow
    int bestX = 0; // 把 0 存入 bestX
    int bestScore = Integer.MAX_VALUE; // 把 Integer.MAX_VALUE 存入 bestScore
    int n = puzzle.length; // 把 puzzle.长度 存入 元素个数
    for (int x = 0; x <= bg.length - n; x++) { // 让 x 从 0 开始计数，x 不超过 bg.长度 减 元素个数 就继续
      int score = 0; // 把 0 存入 score
      for (int y = 0; y < n; y++)
        score += Math.abs(bg[x + y] - puzzle[y]); // 让 y 从 0 开始计数，y 小于 元素个数 就继续
      if (score < bestScore) {
        bestScore = score;
        bestX = x;
      } // 若 score 小于 bestScore) { bestScore 赋值为 score; bestX 赋值为 x; }
    }
    return new int[] {bestX, bestScore}; // 返回 new int[]{bestX, bestScore}
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] bg = {10, 10, 10, 10, 200, 200, 200, 200}; // 把 {10,10,10,10,200,200,200,200}; 写入 int[] bg
    int[] puzzle = {10, 200, 200, 200}; // 把 {10,200,200,200}; 写入 int[] puzzle
    int[] got = bestMatchWindow(bg, puzzle); // 把 bestMatchWindow(bg, puzzle); 写入 int[] got
    int[] want = {3, 0}; // 把 {3, 0}; 写入 int[] want
    if (got[0] != want[0] || got[1] != want[1]) { // 若 got[0] 不等于 want[0] 或 got[1] 不等于 want[1]
      System.out.println(
          "FAIL got " + Arrays.toString(got) + " want " + Arrays.toString(want)); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
