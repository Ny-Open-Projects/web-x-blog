// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc51_solution333 { // 定义类型
  public static List<List<String>> solveNQueens(int n) {
    List<List<String>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> res
    boolean[] cols = new boolean[n]; // 把 new boolean[元素个数]; 写入 boolean[] cols
    boolean[] diag1 = new boolean[2 * n]; // 把 new boolean[2 乘 元素个数]; 写入 boolean[] diag1
    boolean[] diag2 = new boolean[2 * n]; // 把 new boolean[2 乘 元素个数]; 写入 boolean[] diag2
    List<char[]> board = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<char[]> board
    backtrack(
        0, n, cols, diag1, diag2, board, res); // backtrack(0, 元素个数, 列数, diag1, diag2, 棋盘, 结果);
    return res; // 返回 结果
  }

  private static void backtrack(
      int r,
      int n,
      boolean[] cols,
      boolean[] d1,
      boolean[] d2,
      List<char[]> board,
      List<List<String>> res) { // List 小于 char[] 超过 棋盘, List 小于 List 小于 String 超过 超过 结果) {
    if (r == n) { // 若 右指针 等于 元素个数
      List<String> rows = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> rows
      for (char[] row : board)
        rows.add(new String(row)); // for (char[] row : 棋盘) 行数 追加 new String(row));
      res.add(rows); // 结果 追加 行数);
      return; // return;
    }
    for (int c = 0; c < n; c++) { // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
      if (cols[c] || d1[r - c + n] || d2[r + c])
        continue; // 若 列数[字符] 或 d1[右指针 减 字符 加 元素个数] 或 d2[右指针 加 字符]) continue;
      cols[c] =
          d1[r - c + n] =
              d2[r + c] = true; // 把 d1[右指针 减 字符 加 元素个数] 赋值为 d2[右指针 加 字符] 赋值为 true; 写入 cols[c]
      char[] row = new char[n]; // 把 new char[元素个数]; 写入 char[] row
      Arrays.fill(row, '.'); // Arrays.fill(row, '.');
      row[c] = 'Q'; // 把 'Q'; 写入 row[c]
      board.add(row); // 棋盘 追加 row);
      backtrack(
          r + 1, n, cols, d1, d2, board, res); // backtrack(右指针 加 1, 元素个数, 列数, d1, d2, 棋盘, 结果);
      board.remove(board.size() - 1); // 棋盘 弹出 棋盘.大小() 减 1);
      cols[c] =
          d1[r - c + n] =
              d2[r + c] = false; // 把 d1[右指针 减 字符 加 元素个数] 赋值为 d2[右指针 加 字符] 赋值为 false; 写入 cols[c]
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<List<String>> got = solveNQueens(4); // 把 solveNQueens(4); 写入 List<List<String>> got
    List<List<String>> want =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> want
    want.add(
        Arrays.asList(
            ".Q..", "...Q", "Q...",
            "..Q.")); // want 追加 Arrays.asList(「.Q..」, 「.Q..」, 「.Q..」, 「.Q..」));
    want.add(
        Arrays.asList(
            "..Q.", "Q...", "...Q",
            ".Q..")); // want 追加 Arrays.asList(「..Q.」, 「..Q.」, 「..Q.」, 「..Q.」));
    if (!got.equals(want)) { // 若 取反 got.equals(want
      System.out.println("FAIL solveNQueens(4)=" + got); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
