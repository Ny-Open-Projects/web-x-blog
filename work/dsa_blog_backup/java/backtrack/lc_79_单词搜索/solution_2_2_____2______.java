// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240191
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc79_solution222 { // 定义类型
  private char[][] board; // private char[][] 棋盘;
  private int m, n; // private int 映射表, 元素个数;
  private String word; // private String 单词;

  public boolean exist(String[] boardArr, String w) { // 定义函数/方法 exist
    if (boardArr == null || boardArr.length == 0 || boardArr[0].length() == 0) return false;
    m = boardArr.length; // 把 boardArr.长度; 写入 映射表
    n = boardArr[0].length(); // 把 boardArr[0].长度(); 写入 元素个数
    board = new char[m][n]; // 把 new char[映射表][元素个数]; 写入 棋盘
    for (int i = 0; i < m; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      board[i] = boardArr[i].toCharArray(); // 把 boardArr[下标 i].toCharArray(); 写入 board[i]
    }
    word = w; // 把 权重; 写入 单词
    for (int i = 0; i < m; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      for (int j = 0; j < n; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
        if (find(i, j, 0)) { // 若 find(下标 i, 下标 j, 0
          return true; // 返回 true
        }
      }
    }
    return false; // 返回 false
  }

  private boolean find(int i, int j, int cur) { // 定义函数/方法 find
    if (i < 0 || i >= m || j < 0
        || j >= n) { // 若 下标 i 小于 0 或 下标 i 不低于 映射表 或 下标 j 小于 0 或 下标 j 不低于 元素个数
      return false; // 返回 false
    }
    char letter = board[i][j]; // 把 棋盘[下标 i][下标 j]; 写入 char letter
    if (letter != word.charAt(cur)) { // 若 letter 不等于 单词 取字符 当前值
      return false; // 返回 false
    }
    if (cur == word.length() - 1) { // 若 当前值 等于 单词.长度() 减 1
      return true; // 返回 true
    }
    board[i][j] = ' '; // 把 ' '; 写入 board[i][j]
    boolean ret =
        find(i + 1, j, cur + 1) // 把 find(下标 i 加 1, 下标 j, 当前值 加 1) 写入 boolean ret
            || find(i - 1, j, cur + 1) // 或 find(下标 i 减 1, 下标 j, 当前值 加 1)
            || find(i, j + 1, cur + 1) // 或 find(下标 i, 下标 j 加 1, 当前值 加 1)
            || find(i, j - 1, cur + 1); // 或 find(下标 i, 下标 j 减 1, 当前值 加 1);
    board[i][j] = letter; // 把 letter; 写入 board[i][j]
    return ret; // 返回 ret
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc79_solution222 s = new lc79_solution222(); // 把 new lc79_solution222(); 写入 lc79_solution222 s
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
