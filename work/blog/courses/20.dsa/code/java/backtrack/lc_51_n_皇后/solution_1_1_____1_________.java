// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc51_solution111 { // 定义类型
  private List<List<String>> solutions; // private List 小于 List 小于 String 超过 超过 solutions;
  private int n; // private int 元素个数;
  private int[] queens; // private int[] queens;
  private Set<Integer> columns; // private Set 小于 Integer 超过 columns;
  private Set<Integer> diagonal1; // private Set 小于 Integer 超过 diagonal1;
  private Set<Integer> diagonal2; // private Set 小于 Integer 超过 diagonal2;

  public List<List<String>> solveNQueens(int n) { // 定义函数/方法 solveNQueens
    solutions = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 solutions
    this.n = n; // 把 元素个数; 写入 元素个数
    queens = new int[n]; // 把 new int[元素个数]; 写入 queens
    Arrays.fill(queens, -1); // Arrays.fill(queens, 减 1);
    columns = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 columns
    diagonal1 = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 diagonal1
    diagonal2 = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 diagonal2
    backtrack(0); // backtrack(0);
    return solutions; // 返回 solutions
  }

  private void backtrack(int row) { // 定义函数/方法 backtrack
    if (row == n) { // 若 row 等于 元素个数
      solutions.add(generateBoard()); // solutions 追加 generateBoard());
    } else { // 否则
      for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (columns.contains(i) || diagonal1.contains(row - i) || diagonal2.contains(row + i)) {
          continue; // 跳过本轮，进入下一次
        }
        queens[row] = i; // 把 下标 i; 写入 queens[row]
        columns.add(i); // columns 追加 下标 i);
        diagonal1.add(row - i); // diagonal1 追加 row 减 下标 i);
        diagonal2.add(row + i); // diagonal2 追加 row 加 下标 i);
        backtrack(row + 1); // backtrack(row 加 1);
        columns.remove(i); // columns 弹出 下标 i);
        diagonal1.remove(row - i); // diagonal1 弹出 row 减 下标 i);
        diagonal2.remove(row + i); // diagonal2 弹出 row 加 下标 i);
      }
    }
  }

  private List<String> generateBoard() { // 定义函数/方法 generateBoard
    List<String> board = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> board
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      char[] row = new char[n]; // 把 new char[元素个数]; 写入 char[] row
      Arrays.fill(row, '.'); // Arrays.fill(row, '.');
      row[queens[i]] = 'Q'; // 把 'Q'; 写入 row[queens[i]]
      board.add(new String(row)); // 棋盘 追加 new String(row));
    }
    return board; // 返回 棋盘
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc51_solution111 s = new lc51_solution111(); // 把 new lc51_solution111(); 写入 lc51_solution111 s
    List<List<String>> r = s.solveNQueens(4); // 把 字符串.solveNQueens(4); 写入 List<List<String>> r
    if (r.size() != 2) throw new RuntimeException("FAILED: " + r.size());
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
