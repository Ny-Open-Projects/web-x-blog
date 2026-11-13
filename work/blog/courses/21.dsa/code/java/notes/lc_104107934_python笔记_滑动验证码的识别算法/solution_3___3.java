// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static int nccMatch(int[] bg, int[] puzzle) { // 定义函数/方法 nccMatch
    int bestX = 0; // 把 0 存入 bestX
    double bestScore = Double.NEGATIVE_INFINITY; // 把 Double.NEGATIVE_INFINITY 存入 bestScore
    int n = puzzle.length; // 把 puzzle.长度 存入 元素个数
    for (int x = 0; x <= bg.length - n; x++) { // 让 x 从 0 开始计数，x 不超过 bg.长度 减 元素个数 就继续
      int[] window =
          Arrays.copyOfRange(
              bg, x, x + n); // 把 Arrays.copyOfRange(bg, x, x 加 元素个数); 写入 int[] window
      double bw = 0;
      for (int v : window) bw += v;
      bw /= n; // 把 0; for (int 值 : window) bw 累加 值; bw 除以 元素个数 存入 bw
      double pw = 0;
      for (int v : puzzle) pw += v;
      pw /= n; // 把 0; for (int 值 : puzzle) pw 累加 值; pw 除以 元素个数 存入 pw
      double num = 0;
      for (int i = 0; i < n; i++) num += (window[i] - bw) * (puzzle[i] - pw);
      double db = 0;
      for (int v : window) db += (v - bw) * (v - bw);
      db = Math.sqrt(db);
      double dp = 0;
      for (int v : puzzle) dp += (v - pw) * (v - pw);
      dp = Math.sqrt(dp);
      double denom = db * dp; // 把 db 乘 DP 表 存入 denom
      double score = denom != 0 ? num / denom : 0; // 把 denom 不等于 0 ? num 除以 denom : 0 存入 score
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
    int got = nccMatch(bg, puzzle); // 把 nccMatch(bg, puzzle) 存入 got
    if (got != 3) {
      System.out.println("FAIL got " + got + " want 3");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
