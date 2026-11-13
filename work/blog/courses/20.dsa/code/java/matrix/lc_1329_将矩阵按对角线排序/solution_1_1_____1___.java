// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1329_solution111 { // 定义类型
  public int[][] diagonalSort(int[][] mat) { // 定义函数/方法 diagonalSort
    int n = mat.length; // 把 mat.长度 存入 元素个数
    int m = mat[0].length; // 把 mat[0].长度 存入 映射表
    List<List<Integer>> diag =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> diag
    for (int i = 0; i < m + n - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 加 元素个数 减 1 就继续
      diag.add(new ArrayList<>()); // diag 追加 new ArrayList 小于 超过 ());
    }
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = 0; j < m; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 映射表 就继续
        diag.get(i - j + m - 1)
            .add(mat[i][j]); // diag 查找 下标 i 减 下标 j 加 映射表 减 1) 追加 mat[下标 i][下标 j]);
      }
    }
    for (List<Integer> d : diag) { // for (List 小于 Integer 超过 d : diag) {
      Collections.sort(d); // 排序
    }
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = 0; j < m; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 映射表 就继续
        mat[i][j] =
            diag.get(i - j + m - 1).get(0); // 把 diag 查找 下标 i 减 下标 j 加 映射表 减 1) 查找 0); 写入 mat[i][j]
        diag.get(i - j + m - 1).remove(0); // diag 查找 下标 i 减 下标 j 加 映射表 减 1) 弹出 0);
      }
    }
    return mat; // 返回 mat
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc1329_solution111 s =
        new lc1329_solution111(); // 把 new lc1329_solution111(); 写入 lc1329_solution111 s
    int[][][] tests = { // 把 { 写入 int[][][] tests
      {{3, 3, 1, 1}, {2, 2, 1, 2}, {1, 1, 1, 2}},
      {{10, 6, 8}, {15, 11, 7}, {14, 5, 12}},
      {{5}} // { {5} }
    };
    int[][][] wants = { // 把 { 写入 int[][][] wants
      {{1, 1, 1, 1}, {1, 2, 2, 2}, {1, 2, 3, 3}},
      {{10, 6, 8}, {5, 11, 7}, {14, 15, 12}},
      {{5}} // { {5} }
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int t = 0; t < tests.length; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 tests.长度 就继续
      int[][] got = s.diagonalSort(tests[t]); // 把 字符串.diagonalSort(tests[另一字符串]); 写入 int[][] got
      if (!Arrays.deepEquals(got, wants[t])) { // 若 取反 Arrays.deepEquals(got, wants[另一字符串]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL diagonalSort case "
                + t
                + " got "
                + Arrays.deepToString(got)
                + " want "
                + Arrays.deepToString(wants[t])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
