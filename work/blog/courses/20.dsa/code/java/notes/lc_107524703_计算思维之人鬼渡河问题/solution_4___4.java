// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class RiverWithDir { // 定义类型
  static int[][] D = {
    {2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}
  }; // 把 {{2,0},{1,0},{1,1},{0,1},{0,2}}; 写入 static int[][] D

  static boolean safe(int r, int g) { // 定义函数/方法 safe
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
  }

  static boolean jump(
      int r, int g, int dir, int step, Set<String> visited, List<int[]> path) { // 定义函数/方法 jump
    if (r == 0 && g == 0 && step % 2 == 0)
      return true; // 若 右指针 等于 0 且 g 等于 0 且 步数 对…取模 2 等于 0，直接返回 true
    String key = r + "," + g + "," + (step % 2); // 把 右指针 加 「,」 加 g 加 「,」 加 (步数 对…取模 2) 存入 key
    if (visited.contains(key)) return false; // 若 已访问集合 是否包含 key)，直接返回 false
    visited.add(key); // 已访问集合 追加 key);
    for (int[] d : D) { // for (int[] d : D) {
      int nr = r + dir * d[0]; // 把 右指针 加 dir 乘 d[0] 存入 nr
      int ng = g + dir * d[1]; // 把 g 加 dir 乘 d[1] 存入 ng
      if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
      if (jump(
          nr, ng, -dir, step + 1, visited, path)) { // 若 jump(nr, ng, 减 dir, 步数 加 1, 已访问集合, 当前路径
        path.add(new int[] {d[0], d[1]}); // 当前路径 追加 new int[]{d[0], d[1]});
        return true; // 返回 true
      }
    }
    return false; // 返回 false
  }

  static List<int[]> solve() { // 定义函数/方法 solve
    Set<String> visited = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<String> visited
    List<int[]> path = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<int[]> path
    jump(3, 3, -1, 0, visited, path); // jump(3, 3, 减 1, 0, 已访问集合, 当前路径);
    Collections.reverse(path); // 反转
    return path; // 返回 当前路径
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<int[]> plan = solve(); // 把 solve(); 写入 List<int[]> plan
    if (plan.size() != 0)
      throw new RuntimeException(
          "FAILED"); // 若 plan.大小() 不等于 0) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
