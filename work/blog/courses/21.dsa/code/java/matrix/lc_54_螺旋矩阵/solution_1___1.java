// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc54_solution11 { // 定义类型
  public List<Integer> spiralOrder(int[][] matrix) { // 定义函数/方法 spiralOrder
    if (matrix == null || matrix.length == 0)
      return new ArrayList<>(); // 若 矩阵 等于 null 或 矩阵.长度 等于 0，直接返回 new ArrayList 小于 超过 ()
    List<Integer> r = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> r
    int rowBegin = 0, rowEnd = matrix.length - 1; // 把 0, rowEnd 赋值为 矩阵.长度 减 1 存入 rowBegin
    int colBegin = 0, colEnd = matrix[0].length - 1; // 把 0, colEnd 赋值为 矩阵[0].长度 减 1 存入 colBegin
    while (rowBegin <= rowEnd
        && colBegin <= colEnd) { // 循环，直到不满足「rowBegin 不超过 rowEnd 且 colBegin 不超过 colEnd」
      for (int j = colBegin; j <= colEnd; j++) { // 让 下标 j 从 colBegin 开始计数，下标 j 不超过 colEnd 就继续
        r.add(matrix[rowBegin][j]); // 右指针 追加 矩阵[rowBegin][下标 j]);
      }
      rowBegin++; // rowBegin 加一
      for (int i = rowBegin; i <= rowEnd; i++) { // 让 下标 i 从 rowBegin 开始计数，下标 i 不超过 rowEnd 就继续
        r.add(matrix[i][colEnd]); // 右指针 追加 矩阵[下标 i][colEnd]);
      }
      colEnd--; // colEnd 减一
      if (rowBegin <= rowEnd) { // 若 rowBegin 不超过 rowEnd
        for (int j = colEnd; j >= colBegin; j--) { // 让 下标 j 从 colEnd 开始计数，下标 j 不低于 colBegin 就继续
          r.add(matrix[rowEnd][j]); // 右指针 追加 矩阵[rowEnd][下标 j]);
        }
        rowEnd--; // rowEnd 减一
      }
      if (colBegin <= colEnd) { // 若 colBegin 不超过 colEnd
        for (int i = rowEnd; i >= rowBegin; i--) { // 让 下标 i 从 rowEnd 开始计数，下标 i 不低于 rowBegin 就继续
          r.add(matrix[i][colBegin]); // 右指针 追加 矩阵[下标 i][colBegin]);
        }
        colBegin++; // colBegin 加一
      }
    }
    return r; // 返回 右指针
  }

  static int[] toArr(List<Integer> l) {
    int[] a = new int[l.size()];
    for (int i = 0; i < a.length; i++) a[i] = l.get(i);
    return a;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc54_solution11 s = new lc54_solution11(); // 把 new lc54_solution11(); 写入 lc54_solution11 s
    Object[] t1 =
        new Object[] {
          new int[][] {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, new int[] {1, 2, 3, 6, 9, 8, 7, 4, 5}
        };
    Object[] t2 =
        new Object[] {null, new int[] {}}; // 把 new Object[]{null, new int[]{}}; 写入 Object[] t2
    Object[] t3 = new Object[] {new int[][] {{1, 2, 3}}, new int[] {1, 2, 3}};
    Object[] t4 = new Object[] {new int[][] {{1}, {2}, {3}}, new int[] {1, 2, 3}};
    Object[][] tests = {t1, t2, t3, t4}; // 把 {t1, t2, t3, t4}; 写入 Object[][] tests
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests) { // for (Object[] 另一字符串 : tests) {
      int[][] inp = (int[][]) t[0]; // 把 (int[][]) 另一字符串[0]; 写入 int[][] inp
      int[] want = (int[]) t[1]; // 把 (int[]) 另一字符串[1]; 写入 int[] want
      List<Integer> got = s.spiralOrder(inp); // 把 字符串.spiralOrder(inp); 写入 List<Integer> got
      if (!Arrays.equals(toArr(got), want)) { // 若 取反 Arrays.equals(toArr(got), want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL spiralOrder("
                + Arrays.deepToString(inp)
                + ")="
                + got
                + " want "
                + Arrays.toString(want)); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
