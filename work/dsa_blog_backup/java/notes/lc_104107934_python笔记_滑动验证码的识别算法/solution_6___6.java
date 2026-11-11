// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static int[][] buildSynthetic() { // 定义函数/方法 buildSynthetic
    int bgLen = 8, gapStart = 3, puzzleLen = 4; // 把 8, gapStart 赋值为 3, puzzleLen 赋值为 4 存入 bgLen
    int[] bg = new int[bgLen]; // 把 new int[bgLen]; 写入 int[] bg
    for (int i = 0; i < bgLen; i++) bg[i] = 10; // 让 下标 i 从 0 开始计数，下标 i 小于 bgLen 就继续
    for (int i = gapStart; i < Math.min(gapStart + puzzleLen, bgLen); i++) bg[i] = 200;
    int[] puzzle = Arrays.copyOfRange(bg, gapStart, gapStart + puzzleLen);
    return new int[][] {bg, puzzle}; // 返回 new int[][]{bg, puzzle}
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] got = buildSynthetic(); // 把 buildSynthetic(); 写入 int[][] got
    int[] wantBg = {
      10, 10, 10, 200, 200, 200, 200, 10
    }; // 把 {10,10,10,200,200,200,200,10}; 写入 int[] wantBg
    int[] wantPuzzle = {200, 200, 200, 200}; // 把 {200,200,200,200}; 写入 int[] wantPuzzle
    if (!Arrays.equals(got[0], wantBg) || !Arrays.equals(got[1], wantPuzzle)) {
      System.out.println(
          "FAIL bg=" + Arrays.toString(got[0]) + " puzzle=" + Arrays.toString(got[1])); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
