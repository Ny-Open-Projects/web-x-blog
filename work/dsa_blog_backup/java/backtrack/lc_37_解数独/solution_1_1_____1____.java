// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238257
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc37_solution111 { // 定义类型
  public static void solveSudoku(char[][] board) { // public static void solveSudoku(char[][] 棋盘) {
    backtrack(board); // backtrack(棋盘);
  }

  static boolean is_valid(char[][] board, int row, int col, char num) { // 定义判定函数 is_valid
    for (int i = 0; i < 9; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
      if (board[i][col] == num) return false; // 若 棋盘[下标 i][col] 等于 num，直接返回 false
      if (board[row][i] == num) return false; // 若 棋盘[row][下标 i] 等于 num，直接返回 false
    }
    int sr = 3 * (row / 3), sc = 3 * (col / 3); // 把 3 乘 (row 除以 3), sc 赋值为 3 乘 (col 除以 3) 存入 sr
    for (int i = 0; i < 3; i++) // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
    for (int j = 0; j < 3; j++) // 让 下标 j 从 0 开始计数，下标 j 小于 3 就继续
      if (board[sr + i][sc + j] == num)
          return false; // 若 棋盘[sr 加 下标 i][sc 加 下标 j] 等于 num，直接返回 false
    return true; // 返回 true
  }

  static boolean backtrack(char[][] board) { // 定义函数/方法 backtrack
    for (int row = 0; row < 9; row++) // 让 row 从 0 开始计数，row 小于 9 就继续
    for (int col = 0; col < 9; col++) // 让 col 从 0 开始计数，col 小于 9 就继续
      if (board[row][col] == '.') { // 若 棋盘[row][col] 等于 '.'
          for (char num = '1';
              num <= '9';
              num++) { // 把 '1'; num 不超过 '9'; num 加一 ) { 写入 for (char num
            if (is_valid(board, row, col, num)) { // 若 is_valid(棋盘, row, col, num
              board[row][col] = num; // 把 num; 写入 board[row][col]
              if (backtrack(board)) return true; // 若 backtrack(棋盘)，直接返回 true
              board[row][col] = '.'; // 把 '.'; 写入 board[row][col]
            }
          }
          return false; // 返回 false
        }
    return true; // 返回 true
  }

  static boolean isValid(char[][] b) { // 定义判定函数 isValid
    for (int i = 0; i < 9; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
      boolean[] seen = new boolean[9]; // 把 new boolean[9]; 写入 boolean[] seen
      for (int j = 0; j < 9; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 9 就继续
        int v = b[i][j] - '1'; // 把 b[下标 i][下标 j] 减 '1' 存入 值
        if (v < 0 || v > 8 || seen[v]) return false; // 若 值 小于 0 或 值 超过 8 或 已见集合[值]，直接返回 false
        seen[v] = true; // 把 true; 写入 seen[v]
      }
    }
    for (int j = 0; j < 9; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 9 就继续
      boolean[] seen = new boolean[9]; // 把 new boolean[9]; 写入 boolean[] seen
      for (int i = 0; i < 9; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
        int v = b[i][j] - '1'; // 把 b[下标 i][下标 j] 减 '1' 存入 值
        if (v < 0 || v > 8 || seen[v]) return false; // 若 值 小于 0 或 值 超过 8 或 已见集合[值]，直接返回 false
        seen[v] = true; // 把 true; 写入 seen[v]
      }
    }
    for (int bi = 0; bi < 3; bi++)
      for (int bj = 0; bj < 3; bj++) { // 让 bi 从 0 开始计数，bi 小于 3 就继续
        boolean[] seen = new boolean[9]; // 把 new boolean[9]; 写入 boolean[] seen
        for (int i = 0; i < 3; i++)
          for (int j = 0; j < 3; j++) { // 让 下标 i 从 0 开始计数，下标 i 小于 3 就继续
            int v = b[bi * 3 + i][bj * 3 + j] - '1'; // 把 b[bi 乘 3 加 下标 i][bj 乘 3 加 下标 j] 减 '1' 存入 值
            if (v < 0 || v > 8 || seen[v]) return false; // 若 值 小于 0 或 值 超过 8 或 已见集合[值]，直接返回 false
            seen[v] = true; // 把 true; 写入 seen[v]
          }
      }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    char[][] board = { // 把 { 写入 char[][] board
      {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
      {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
      {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
      {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
      {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
      {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
      {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
      {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
      {'.', '.', '.', '.', '8', '.', '.', '7', '9'} // {'.','.','.','.','8','.','.','7','9'}
    };
    solveSudoku(board); // solveSudoku(棋盘);
    if (!isValid(board))
      throw new RuntimeException(
          "FAILED"); // 若 取反 isValid(棋盘)) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
