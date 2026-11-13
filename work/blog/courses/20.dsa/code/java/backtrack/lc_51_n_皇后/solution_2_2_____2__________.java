// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc51_solution222 { // 定义类型
  public List<List<String>> solveNQueens(int n) { // 定义函数/方法 solveNQueens
    List<List<String>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> res
    int[] cols = new int[n]; // 把 new int[元素个数]; 写入 int[] cols
    Arrays.fill(cols, -1); // Arrays.fill(列数, 减 1);
    backtrack(0, n, cols, res); // backtrack(0, 元素个数, 列数, 结果);
    return res; // 返回 结果
  }

  private void backtrack(int row, int n, int[] cols, List<List<String>> res) { // 定义函数/方法 backtrack
    if (row == n) { // 若 row 等于 元素个数
      List<String> board = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> board
      for (int c : cols) { // for (int 字符 : 列数) {
        char[] line = new char[n]; // 把 new char[元素个数]; 写入 char[] line
        Arrays.fill(line, '.'); // Arrays.fill(line, '.');
        line[c] = 'Q'; // 把 'Q'; 写入 line[c]
        board.add(new String(line)); // 棋盘 追加 new String(line));
      }
      res.add(board); // 结果 追加 棋盘);
      return; // return;
    }
    for (int col = 0; col < n; col++) { // 让 col 从 0 开始计数，col 小于 元素个数 就继续
      if (isValid(row, col, cols)) { // 若 isValid(row, col, 列数
        cols[row] = col; // 把 col; 写入 cols[row]
        backtrack(row + 1, n, cols, res); // backtrack(row 加 1, 元素个数, 列数, 结果);
        cols[row] = -1; // 把 减 1; 写入 cols[row]
      }
    }
  }

  private boolean isValid(int row, int col, int[] cols) { // 定义判定函数 isValid
    for (int r = 0; r < row; r++) { // 让 右指针 从 0 开始计数，右指针 小于 row 就继续
      if (cols[r] == col || Math.abs(cols[r] - col) == Math.abs(r - row)) return false;
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc51_solution222 s = new lc51_solution222(); // 把 new lc51_solution222(); 写入 lc51_solution222 s
    List<List<String>> r = s.solveNQueens(4); // 把 字符串.solveNQueens(4); 写入 List<List<String>> r
    if (r.size() != 2) throw new RuntimeException("FAILED: " + r.size());
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
