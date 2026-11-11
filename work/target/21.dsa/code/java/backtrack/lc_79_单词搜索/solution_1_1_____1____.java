// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240191
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc79_solution111 { // 定义类型
  private char[][] board; // private char[][] 棋盘;
  private int h, w; // private int h, 权重;
  private char[][] visited; // private char[][] 已访问集合;

  public boolean exist(String[] boardArr, String word) { // 定义函数/方法 exist
    if (boardArr == null || boardArr.length == 0 || boardArr[0].length() == 0) return false;
    h = boardArr.length; // 把 boardArr.长度; 写入 h
    w = boardArr[0].length(); // 把 boardArr[0].长度(); 写入 权重
    board = new char[h][w]; // 把 new char[h][权重]; 写入 棋盘
    for (int i = 0; i < h; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 h 就继续
      board[i] = boardArr[i].toCharArray(); // 把 boardArr[下标 i].toCharArray(); 写入 board[i]
    }
    visited = new char[h][w]; // 把 new char[h][权重]; 写入 已访问集合
    for (int i = 0; i < h; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 h 就继续
      for (int j = 0; j < w; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 权重 就继续
        if (check(i, j, word, 0)) { // 若 check(下标 i, 下标 j, 单词, 0
          return true; // 返回 true
        }
      }
    }
    return false; // 返回 false
  }

  private boolean check(int i, int j, String s, int k) { // 定义判定函数 check
    if (board[i][j] != s.charAt(k)) { // 若 棋盘[下标 i][下标 j] 不等于 字符串 取字符 下标 k
      return false; // 返回 false
    } else if (k == s.length() - 1) { // 否则，若 下标 k 等于 字符串.长度() 减 1
      return true; // 返回 true
    }
    visited[i][j] = 'Y'; // 把 'Y'; 写入 visited[i][j]
    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    boolean result = false; // 把 false; 写入 boolean result
    for (int[] d : directions) { // for (int[] d : directions) {
      int newi = i + d[0], newj = j + d[1]; // 把 下标 i 加 d[0], newj 赋值为 下标 j 加 d[1] 存入 newi
      if (newi >= 0 && newi < h && newj >= 0
          && newj < w) { // 若 newi 不低于 0 且 newi 小于 h 且 newj 不低于 0 且 newj 小于 权重
        if (visited[newi][newj] != 'Y') { // 若 已访问集合[newi][newj] 不等于 'Y'
          visited[newi][newj] = 'Y'; // 把 'Y'; 写入 visited[newi][newj]
          boolean flag =
              check(newi, newj, s, k + 1); // 把 check(newi, newj, 字符串, 下标 k 加 1); 写入 boolean flag
          if (flag) { // 若 flag
            result = true; // 把 true; 写入 结果
            break; // 跳出循环
          }
          visited[newi][newj] = 'N'; // 把 'N'; 写入 visited[newi][newj]
        }
      }
    }
    visited[i][j] = 'N'; // 把 'N'; 写入 visited[i][j]
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc79_solution111 s = new lc79_solution111(); // 把 new lc79_solution111(); 写入 lc79_solution111 s
    String[] board = {"ABC", "BDS", "ATE"}; // 把 {「ABC」, 「ABC」, 「ABC」}; 写入 String[] board
    boolean[] gots = {s.exist(board, "ABD"), s.exist(board, "ZZZ")};
    boolean[] wants = {true, false}; // 把 {true, false}; 写入 boolean[] wants
    for (int i = 0; i < gots.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 gots.长度 就继续
      if (gots[i] != wants[i]) { // 若 gots[下标 i] 不等于 wants[下标 i]
        System.out.println(
            "FAIL exist case " + i + " got " + gots[i] + " want " + wants[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
