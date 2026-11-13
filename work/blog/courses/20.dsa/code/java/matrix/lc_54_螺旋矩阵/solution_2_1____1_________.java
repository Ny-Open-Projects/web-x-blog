// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc54_solution211 { // 定义类型
  public List<Integer> spiralOrder(int[][] matrix) { // 定义函数/方法 spiralOrder
    if (matrix == null || matrix.length == 0)
      return new ArrayList<>(); // 若 矩阵 等于 null 或 矩阵.长度 等于 0，直接返回 new ArrayList 小于 超过 ()
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    int top = 0, bottom = matrix.length - 1; // 把 0, bottom 赋值为 矩阵.长度 减 1 存入 top
    int left = 0, right = matrix[0].length - 1; // 把 0, 右边界 赋值为 矩阵[0].长度 减 1 存入 左边界
    while (top <= bottom && left <= right) { // 循环，直到不满足「top 不超过 bottom 且 左边界 不超过 右边界」
      for (int j = left; j <= right; j++)
        res.add(matrix[top][j]); // 让 下标 j 从 左边界 开始计数，下标 j 不超过 右边界 就继续
      top++; // top 加一
      for (int i = top; i <= bottom; i++)
        res.add(matrix[i][right]); // 让 下标 i 从 top 开始计数，下标 i 不超过 bottom 就继续
      right--; // 右边界 减一
      if (top <= bottom) { // 若 top 不超过 bottom
        for (int j = right; j >= left; j--)
          res.add(matrix[bottom][j]); // 让 下标 j 从 右边界 开始计数，下标 j 不低于 左边界 就继续
        bottom--; // bottom 减一
      }
      if (left <= right) { // 若 左边界 不超过 右边界
        for (int i = bottom; i >= top; i--)
          res.add(matrix[i][left]); // 让 下标 i 从 bottom 开始计数，下标 i 不低于 top 就继续
        left++; // 左边界 加一
      }
    }
    return res; // 返回 结果
  }

  static int[] toArr(List<Integer> l) {
    int[] a = new int[l.size()];
    for (int i = 0; i < a.length; i++) a[i] = l.get(i);
    return a;
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc54_solution211 s = new lc54_solution211(); // 把 new lc54_solution211(); 写入 lc54_solution211 s
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
