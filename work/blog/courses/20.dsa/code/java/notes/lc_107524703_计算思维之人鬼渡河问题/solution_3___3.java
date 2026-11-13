// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class RiverCrossing3 { // 定义类型
  static int[][] D = {
    {2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}
  }; // 把 {{2,0},{1,0},{1,1},{0,1},{0,2}}; 写入 static int[][] D

  static boolean safe(int r, int g) { // 定义函数/方法 safe
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
  }

  static boolean dfs(int r, int g, int step, Set<String> visited, List<int[]> path) { // 定义函数/方法 dfs
    if (r == 0 && g == 0) return true; // 若 右指针 等于 0 且 g 等于 0，直接返回 true
    String key = r + "," + g + "," + (step % 2); // 把 右指针 加 「,」 加 g 加 「,」 加 (步数 对…取模 2) 存入 key
    if (visited.contains(key)) return false; // 若 已访问集合 是否包含 key)，直接返回 false
    visited.add(key); // 已访问集合 追加 key);
    boolean odd = (step % 2 == 1); // 把 (步数 对…取模 2 等于 1); 写入 boolean odd
    for (int[] d : D) { // for (int[] d : D) {
      int dr = d[0], dg = d[1]; // 把 d[0], dg 赋值为 d[1] 存入 dr
      int nr, ng; // int nr, ng;
      if (odd) { // 若 odd
        if (r < dr || g < dg) continue; // 若 右指针 小于 dr 或 g 小于 dg) continue;
        nr = r - dr;
        ng = g - dg; // 把 右指针 减 dr; ng 赋值为 g 减 dg; 写入 nr
      } else { // 否则
        if ((3 - r) < dr || (3 - g) < dg) continue; // 若 (3 减 右指针) 小于 dr 或 (3 减 g) 小于 dg) continue;
        nr = r + dr;
        ng = g + dg; // 把 右指针 加 dr; ng 赋值为 g 加 dg; 写入 nr
      }
      if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
      if (dfs(nr, ng, step + 1, visited, path)) { // 若 dfs(nr, ng, 步数 加 1, 已访问集合, 当前路径
        path.add(new int[] {dr, dg}); // 当前路径 追加 new int[]{dr, dg});
        return true; // 返回 true
      }
    }
    return false; // 返回 false
  }

  static List<int[]> solve() { // 定义函数/方法 solve
    Set<String> visited = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<String> visited
    List<int[]> path = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<int[]> path
    dfs(3, 3, 1, visited, path); // dfs(3, 3, 1, 已访问集合, 当前路径);
    Collections.reverse(path); // 反转
    return path; // 返回 当前路径
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<int[]> plan = solve(); // 把 solve(); 写入 List<int[]> plan
    int[][] exp = {
      {1, 1}, {1, 0}, {0, 2}, {0, 1}, {2, 0}, {1, 1}, {2, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1}
    };
    boolean ok = plan.size() == exp.length; // 把 plan.大小() 等于 exp.长度; 写入 boolean ok
    for (int i = 0; i < exp.length && ok; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 exp.长度 且 ok 就继续
      if (plan.get(i)[0] != exp[i][0] || plan.get(i)[1] != exp[i][1]) ok = false;
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
