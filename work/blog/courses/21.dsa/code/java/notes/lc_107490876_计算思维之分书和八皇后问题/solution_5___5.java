// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  int SIZE = 8; // 把 8 存入 SIZE
  int[] colRow; // int[] colRow;
  boolean[] rows, diag1, diag2; // boolean[] 行数, diag1, diag2;
  List<int[]> results; // List 小于 int[] 超过 results;

  void place(int col) { // 定义函数/方法 place
    if (col == SIZE) {
      results.add(colRow.clone());
      return;
    } // 若 col 等于 SIZE) { results 追加 colRow.clone()); return; }
    for (int row = 0; row < SIZE; row++) { // 让 row 从 0 开始计数，row 小于 SIZE 就继续
      int d1 = col - row + (SIZE - 1); // 把 col 减 row 加 (SIZE 减 1) 存入 d1
      int d2 = col + row; // 把 col 加 row 存入 d2
      if (rows[row] && diag1[d1] && diag2[d2]) { // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
        colRow[col] = row; // 把 row; 写入 colRow[col]
        rows[row] =
            diag1[d1] = diag2[d2] = false; // 把 diag1[d1] 赋值为 diag2[d2] 赋值为 false; 写入 rows[row]
        place(col + 1); // place(col 加 1);
        rows[row] =
            diag1[d1] = diag2[d2] = true; // 把 diag1[d1] 赋值为 diag2[d2] 赋值为 true; 写入 rows[row]
      }
    }
  }

  List<int[]> nQueens() { // 定义函数/方法 nQueens
    colRow = new int[SIZE]; // 把 new int[SIZE]; 写入 colRow
    rows = new boolean[SIZE]; // 把 new boolean[SIZE]; 写入 行数
    diag1 = new boolean[2 * SIZE - 1]; // 把 new boolean[2 乘 SIZE 减 1]; 写入 diag1
    diag2 = new boolean[2 * SIZE - 1]; // 把 new boolean[2 乘 SIZE 减 1]; 写入 diag2
    Arrays.fill(rows, true); // Arrays.fill(行数, true);
    Arrays.fill(diag1, true); // Arrays.fill(diag1, true);
    Arrays.fill(diag2, true); // Arrays.fill(diag2, true);
    results = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 results
    place(0); // place(0);
    return results; // 返回 results
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    List<int[]> sols = s.nQueens(); // 把 字符串.nQueens(); 写入 List<int[]> sols
    boolean ok = true; // 把 true; 写入 boolean ok
    if (sols.size() != 92) {
      ok = false;
      System.out.println("FAIL count=" + sols.size());
    }
    if (!Arrays.equals(sols.get(0), new int[] {0, 4, 7, 5, 2, 6, 1, 3})) {
      ok = false;
      System.out.println("FAIL first=" + Arrays.toString(sols.get(0)));
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
