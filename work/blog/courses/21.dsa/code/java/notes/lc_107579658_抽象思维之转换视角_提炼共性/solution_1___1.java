// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc107579658_solution11 { // 定义类型
  static int countSolutions(boolean queen) { // 定义函数/方法 countSolutions
    int SIZE = queen ? 8 : 5; // 把 queen ? 8 : 5 存入 SIZE
    int[][] like = { // 把 { 写入 int[][] like
      {0, 0, 1, 1, 0},
      {1, 1, 0, 0, 1},
      {0, 1, 1, 0, 1},
      {0, 0, 0, 1, 0},
      {0, 1, 0, 0, 1},
    };
    int[] Q = new int[SIZE]; // 把 new int[SIZE]; 写入 int[] Q
    boolean[] rows = new boolean[SIZE]; // 把 new boolean[SIZE]; 写入 boolean[] rows
    Arrays.fill(rows, true); // Arrays.fill(行数, true);
    boolean[] diag1 = new boolean[2 * SIZE - 1]; // 把 new boolean[2 乘 SIZE 减 1]; 写入 boolean[] diag1
    boolean[] diag2 = new boolean[2 * SIZE - 1]; // 把 new boolean[2 乘 SIZE 减 1]; 写入 boolean[] diag2
    Arrays.fill(diag1, true); // Arrays.fill(diag1, true);
    Arrays.fill(diag2, true); // Arrays.fill(diag2, true);
    int[] count = {0}; // 把 {0}; 写入 int[] count

    class Back { // 定义类型
      void place(int col) { // 定义函数/方法 place
        if (col == SIZE) { // 若 col 等于 SIZE
          count[0]++; // 计数[0] 加一 ;
          return; // return;
        }
        for (int row = 0; row < SIZE; row++) { // 让 row 从 0 开始计数，row 小于 SIZE 就继续
          if (!queen && like[row][col] != 1)
            continue; // 若 取反 queen 且 like[row][col] 不等于 1) continue;
          if (!rows[row]) continue; // 若 取反 行数[row]) continue;
          if (queen) { // 若 queen
            int d1 = col - row + SIZE - 1; // 把 col 减 row 加 SIZE 减 1 存入 d1
            int d2 = col + row; // 把 col 加 row 存入 d2
            if (!diag1[d1] || !diag2[d2]) continue; // 若 取反 diag1[d1] 或 取反 diag2[d2]) continue;
            diag1[d1] = diag2[d2] = false; // 把 diag2[d2] 赋值为 false; 写入 diag1[d1]
            Q[col] = row; // 把 row; 写入 Q[col]
            rows[row] = false; // 把 false; 写入 rows[row]
            place(col + 1); // place(col 加 1);
            rows[row] = true; // 把 true; 写入 rows[row]
            diag1[d1] = diag2[d2] = true; // 把 diag2[d2] 赋值为 true; 写入 diag1[d1]
          } else { // 否则
            Q[col] = row; // 把 row; 写入 Q[col]
            rows[row] = false; // 把 false; 写入 rows[row]
            place(col + 1); // place(col 加 1);
            rows[row] = true; // 把 true; 写入 rows[row]
          }
        }
      }
    }
    new Back().place(0); // new Back().place(0);
    return count[0]; // 返回 计数[0]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int books = countSolutions(false); // 把 countSolutions(false) 存入 books
    int queens = countSolutions(true); // 把 countSolutions(true) 存入 queens
    if (books != 2) { // 若 books 不等于 2
      System.out.println("FAIL books " + books); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    if (queens != 92) { // 若 queens 不等于 92
      System.out.println("FAIL queens " + queens); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
