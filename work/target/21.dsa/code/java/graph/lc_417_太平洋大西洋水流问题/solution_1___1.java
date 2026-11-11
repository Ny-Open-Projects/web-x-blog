// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc417_solution11 { // 定义类型
  public List<List<Integer>> pacificAtlantic(int[][] matrix) { // 定义函数/方法 pacificAtlantic
    if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return new ArrayList<>();
    int m = matrix.length, n = matrix[0].length; // 把 矩阵.长度, 元素个数 赋值为 矩阵[0].长度 存入 映射表
    boolean[][] pacific = new boolean[m][n]; // 把 new boolean[映射表][元素个数]; 写入 boolean[][] pacific
    boolean[][] atlantic = new boolean[m][n]; // 把 new boolean[映射表][元素个数]; 写入 boolean[][] atlantic
    for (int r = 0; r < m; r++) { // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
      dfs(matrix, r, 0, pacific, m, n); // dfs(矩阵, 右指针, 0, pacific, 映射表, 元素个数);
      dfs(matrix, r, n - 1, atlantic, m, n); // dfs(矩阵, 右指针, 元素个数 减 1, atlantic, 映射表, 元素个数);
    }
    for (int c = 0; c < n; c++) { // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
      dfs(matrix, 0, c, pacific, m, n); // dfs(矩阵, 0, 字符, pacific, 映射表, 元素个数);
      dfs(matrix, m - 1, c, atlantic, m, n); // dfs(矩阵, 映射表 减 1, 字符, atlantic, 映射表, 元素个数);
    }
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    for (int r = 0; r < m; r++) // 让 右指针 从 0 开始计数，右指针 小于 映射表 就继续
    for (int c = 0; c < n; c++) // 让 字符 从 0 开始计数，字符 小于 元素个数 就继续
      if (pacific[r][c] && atlantic[r][c]) res.add(Arrays.asList(r, c));
    return res; // 返回 结果
  }

  private void dfs(int[][] matrix, int r, int c, boolean[][] flow, int m, int n) { // 定义函数/方法 dfs
    flow[r][c] = true; // 把 true; 写入 flow[r][c]
    int[][] dirs = {
      {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    }; // 把 {{ 减 1, 0}, {1, 0}, {0, 减 1}, {0, 1}}; 写入 int[][] dirs
    for (int[] d : dirs) { // for (int[] d : dirs) {
      int nr = r + d[0], nc = c + d[1]; // 把 右指针 加 d[0], nc 赋值为 字符 加 d[1] 存入 nr
      if (nr >= 0
          && nr < m
          && nc >= 0
          && nc < n // 若 nr 不低于 0 且 nr 小于 映射表 且 nc 不低于 0 且 nc 小于 元素个数
          && !flow[nr][nc]
          && matrix[nr][nc]
              >= matrix[r][c]) // 把 矩阵[右指针][字符]) 写入 && !flow[nr][nc] && matrix[nr][nc] >
      dfs(matrix, nr, nc, flow, m, n); // dfs(矩阵, nr, nc, flow, 映射表, 元素个数);
    }
  }

  static void sortPairs(List<List<Integer>> list) { // 定义函数/方法 sortPairs
    list.sort((a, b) -> a.get(0) != b.get(0) ? a.get(0) - b.get(0) : a.get(1) - b.get(1)); // 排序
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc417_solution11 s = new lc417_solution11(); // 把 new lc417_solution11(); 写入 lc417_solution11 s
    int[][] M = {
      {1, 2, 2, 3, 5}, {3, 2, 3, 4, 4}, {2, 4, 5, 3, 1}, {6, 7, 1, 4, 5}, {5, 1, 1, 2, 4}
    };
    List<List<Integer>> got =
        s.pacificAtlantic(M); // 把 字符串.pacificAtlantic(M); 写入 List<List<Integer>> got
    sortPairs(got); // sortPairs(got);
    List<List<Integer>> want =
        Arrays.asList(
            Arrays.asList(0, 4),
            Arrays.asList(1, 3),
            Arrays.asList(1, 4),
            Arrays.asList(2, 2),
            Arrays.asList(3, 0),
            Arrays.asList(3, 1),
            Arrays.asList(4, 0));
    if (!got.equals(want)) { // 若 取反 got.equals(want
      System.out.println("FAIL got " + got); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
