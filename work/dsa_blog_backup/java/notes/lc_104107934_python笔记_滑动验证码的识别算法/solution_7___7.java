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

  static int[][] buildSynthetic() { // 定义函数/方法 buildSynthetic
    int bgLen = 8, gapStart = 3, puzzleLen = 4; // 把 8, gapStart 赋值为 3, puzzleLen 赋值为 4 存入 bgLen
    int[] bg = new int[bgLen]; // 把 new int[bgLen]; 写入 int[] bg
    for (int i = 0; i < bgLen; i++) bg[i] = 10; // 让 下标 i 从 0 开始计数，下标 i 小于 bgLen 就继续
    for (int i = gapStart; i < Math.min(gapStart + puzzleLen, bgLen); i++) bg[i] = 200;
    int[] puzzle = Arrays.copyOfRange(bg, gapStart, gapStart + puzzleLen);
    return new int[][] {bg, puzzle}; // 返回 new int[][]{bg, puzzle}
  }

  static int recognizeCaptcha(int[] bg, int[] puzzle) { // 定义函数/方法 recognizeCaptcha
    boolean[] bgEdges = detectEdges(bg); // 把 detectEdges(bg); 写入 boolean[] bgEdges
    boolean[] puzzleEdges = detectEdges(puzzle); // 把 detectEdges(puzzle); 写入 boolean[] puzzleEdges
    int bestX = 0, bestScore = -1; // 把 0, bestScore 赋值为 减 1 存入 bestX
    for (int x = 0;
        x <= bg.length - puzzle.length;
        x++) { // 让 x 从 0 开始计数，x 不超过 bg.长度 减 puzzle.长度 就继续
      int score = 0; // 把 0 存入 score
      for (int y = 0; y < puzzle.length; y++)
        if (bgEdges[x + y] && puzzleEdges[y]) score++; // 让 y 从 0 开始计数，y 小于 puzzle.长度 就继续
      if (score > bestScore) {
        bestScore = score;
        bestX = x;
      } // 若 score 超过 bestScore) { bestScore 赋值为 score; bestX 赋值为 x; }
    }
    return bestX; // 返回 bestX
  }

  static int fullPipeline() { // 定义函数/方法 fullPipeline
    int[][] sp = buildSynthetic(); // 把 buildSynthetic(); 写入 int[][] sp
    return recognizeCaptcha(sp[0], sp[1]); // 返回 recognizeCaptcha(sp[0], sp[1])
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int got = fullPipeline(); // 把 fullPipeline() 存入 got
    if (got != 0) {
      System.out.println("FAIL got " + got + " want 0");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
