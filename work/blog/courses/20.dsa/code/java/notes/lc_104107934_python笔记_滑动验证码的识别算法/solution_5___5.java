// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static boolean[] detectEdges(int[] image) { // 定义函数/方法 detectEdges
    boolean[] edges = new boolean[image.length]; // 把 new boolean[image.长度]; 写入 boolean[] edges
    for (int i = 1; i < image.length; i++)
      edges[i] = Math.abs(image[i] - image[i - 1]) > 50; // 让 下标 i 从 1 开始计数，下标 i 小于 image.长度 就继续
    return edges; // 返回 边集
  }

  static int findGap(
      int[] bg, int[] puzzle, java.util.ArrayList<Integer> responses) { // 定义函数/方法 findGap
    boolean[] bgEdges = detectEdges(bg); // 把 detectEdges(bg); 写入 boolean[] bgEdges
    boolean[] puzzleEdges = detectEdges(puzzle); // 把 detectEdges(puzzle); 写入 boolean[] puzzleEdges
    int bestX = 0, bestScore = -1; // 把 0, bestScore 赋值为 减 1 存入 bestX
    for (int x = 0;
        x <= bg.length - puzzle.length;
        x++) { // 让 x 从 0 开始计数，x 不超过 bg.长度 减 puzzle.长度 就继续
      int score = 0; // 把 0 存入 score
      for (int y = 0; y < puzzle.length; y++)
        if (bgEdges[x + y] && puzzleEdges[y]) score++; // 让 y 从 0 开始计数，y 小于 puzzle.长度 就继续
      responses.add(score); // responses 追加 score);
      if (score > bestScore) {
        bestScore = score;
        bestX = x;
      } // 若 score 超过 bestScore) { bestScore 赋值为 score; bestX 赋值为 x; }
    }
    return bestX; // 返回 bestX
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] bg = {10, 10, 10, 10, 200, 200, 200, 200}; // 把 {10,10,10,10,200,200,200,200}; 写入 int[] bg
    int[] puzzle = {10, 200, 200, 200}; // 把 {10,200,200,200}; 写入 int[] puzzle
    java.util.ArrayList<Integer> responses = new java.util.ArrayList<>();
    int bestX = findGap(bg, puzzle, responses); // 把 findGap(bg, puzzle, responses) 存入 bestX
    int[] wantResp = {0, 0, 0, 1, 0}; // 把 {0,0,0,1,0}; 写入 int[] wantResp
    boolean ok = (bestX == 3); // 把 (bestX 等于 3); 写入 boolean ok
    if (responses.size() != wantResp.length)
      ok = false; // 若 responses.大小() 不等于 wantResp.长度) ok 赋值为 false;
    else
      for (int i = 0; i < wantResp.length; i++)
        if (responses.get(i) != wantResp[i]) ok = false; // 否则
    if (!ok) { // 若 取反 ok
      System.out.println("FAIL bestX=" + bestX + " responses=" + responses); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
