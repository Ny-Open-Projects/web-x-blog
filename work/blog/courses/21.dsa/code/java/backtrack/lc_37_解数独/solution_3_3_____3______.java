// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238257
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc37_solution333 { // 定义类型
  private char[][] board; // private char[][] 棋盘;
  private boolean[][] line = new boolean[9][9]; // 把 new boolean[9][9]; 写入 private boolean[][] line
  private boolean[][] column =
      new boolean[9][9]; // 把 new boolean[9][9]; 写入 private boolean[][] column
  private boolean[][][] block =
      new boolean[3][3][9]; // 把 new boolean[3][3][9]; 写入 private boolean[][][] block
  private List<int[]> spaces =
      new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 private List<int[]> spaces

  public void solveSudoku(char[][] board) { // 定义函数/方法 solveSudoku
    this.board = board; // 把 棋盘; 写入 棋盘
    for (int i = 0; i < 9; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
      for (int j = 0; j < 9; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 9 就继续
        if (board[i][j] == '.') { // 若 棋盘[下标 i][下标 j] 等于 '.'
          spaces.add(new int[] {i, j}); // spaces 追加 new int[]{下标 i, 下标 j});
        } else { // 否则
          int digit = board[i][j] - '1'; // 把 棋盘[下标 i][下标 j] 减 '1' 存入 digit
          line[i][digit] = true; // 把 true; 写入 line[i][digit]
          column[j][digit] = true; // 把 true; 写入 column[j][digit]
          block[i / 3][j / 3][digit] = true; // 把 true; 写入 block[i / 3][j / 3][digit]
        }
      }
    }
    dfs(0); // dfs(0);
  }

  private boolean dfs(int pos) { // 定义函数/方法 dfs
    if (pos == spaces.size()) { // 若 pos 等于 spaces.大小(
      return true; // 返回 true
    }
    int i = spaces.get(pos)[0]; // 把 spaces 查找 pos)[0] 存入 下标 i
    int j = spaces.get(pos)[1]; // 把 spaces 查找 pos)[1] 存入 下标 j
    for (int digit = 0; digit < 9; digit++) { // 让 digit 从 0 开始计数，digit 小于 9 就继续
      if (!line[i][digit] && !column[j][digit] && !block[i / 3][j / 3][digit]) {
        line[i][digit] = true; // 把 true; 写入 line[i][digit]
        column[j][digit] = true; // 把 true; 写入 column[j][digit]
        block[i / 3][j / 3][digit] = true; // 把 true; 写入 block[i / 3][j / 3][digit]
        board[i][j] = (char) ('1' + digit); // 把 (char) ('1' 加 digit); 写入 board[i][j]
        if (dfs(pos + 1)) { // 若 dfs(pos 加 1
          return true; // 返回 true
        }
        line[i][digit] = false; // 把 false; 写入 line[i][digit]
        column[j][digit] = false; // 把 false; 写入 column[j][digit]
        block[i / 3][j / 3][digit] = false; // 把 false; 写入 block[i / 3][j / 3][digit]
        board[i][j] = '.'; // 把 '.'; 写入 board[i][j]
      }
    }
    return false; // 返回 false
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
    lc37_solution333 s = new lc37_solution333(); // 把 new lc37_solution333(); 写入 lc37_solution333 s
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
    s.solveSudoku(board); // 字符串.solveSudoku(棋盘);
    if (!isValid(board))
      throw new RuntimeException(
          "FAILED"); // 若 取反 isValid(棋盘)) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
