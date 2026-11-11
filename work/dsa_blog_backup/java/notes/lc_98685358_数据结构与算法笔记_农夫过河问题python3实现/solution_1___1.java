// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class FarmerS1 { // 定义类型
  static boolean isSafe(int[] s) { // 定义判定函数 isSafe
    int f = s[0],
        w = s[1],
        g = s[2],
        c = s[3]; // 把 字符串[0], 权重 赋值为 字符串[1], g 赋值为 字符串[2], 字符 赋值为 字符串[3] 存入 f
    if (w == g && f != w) return false; // 若 权重 等于 g 且 f 不等于 权重，直接返回 false
    if (g == c && f != g) return false; // 若 g 等于 字符 且 f 不等于 g，直接返回 false
    return true; // 返回 true
  }

  static String key(int[] s) {
    return s[0] + "," + s[1] + "," + s[2] + "," + s[3];
  }

  static List<int[]> solve() { // 定义函数/方法 solve
    int[] start = {0, 0, 0, 0}; // 把 {0, 0, 0, 0}; 写入 int[] start
    int[] goal = {1, 1, 1, 1}; // 把 {1, 1, 1, 1}; 写入 int[] goal
    Map<String, int[]> prev = new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<String, int[]> prev
    Queue<int[]> q = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Queue<int[]> q
    q.add(start); // 节点 追加 起点);
    prev.put(key(start), null); // 前一个.put(key(起点), null);
    while (!q.isEmpty()) { // 循环，直到不满足「取反 节点.isEmpty(」
      int[] cur = q.poll(); // 把 节点.poll(); 写入 int[] cur
      if (Arrays.equals(cur, goal)) { // 若 Arrays.equals(当前值, goal
        List<int[]> path = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<int[]> path
        int[] p = cur; // 把 当前值; 写入 int[] p
        while (p != null) {
          path.add(0, p);
          p = prev.get(key(p));
        }
        return path; // 返回 当前路径
      }
      int farmer = cur[0]; // 把 当前值[0] 存入 farmer
      for (int i = 0; i < 4; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
        if (i != 0 && cur[i] != farmer) continue; // 若 下标 i 不等于 0 且 当前值[下标 i] 不等于 farmer) continue;
        int[] nxt = cur.clone(); // 把 当前值.clone(); 写入 int[] nxt
        nxt[0] = 1 - farmer; // 把 1 减 farmer; 写入 nxt[0]
        if (i != 0) nxt[i] = 1 - farmer; // 若 下标 i 不等于 0) nxt[下标 i] 赋值为 1 减 farmer;
        if (prev.containsKey(key(nxt))) continue; // 若 前一个.containsKey(key(nxt))) continue;
        if (!isSafe(nxt)) continue; // 若 取反 isSafe(nxt)) continue;
        prev.put(key(nxt), cur); // 前一个.put(key(nxt), 当前值);
        q.add(nxt); // 节点 追加 nxt);
      }
    }
    return null; // 返回 null
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<int[]> got = FarmerS1.solve(); // 把 FarmerS1.solve(); 写入 List<int[]> got
    int[][][] want = { // 把 { 写入 int[][][] want
      {{0, 0, 0, 0}}, {{1, 0, 1, 0}}, {{0, 0, 1, 0}}, {{1, 1, 1, 0}},
      {{0, 1, 0, 0}}, {{1, 1, 0, 1}}, {{0, 1, 0, 1}}, {{1, 1, 1, 1}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    if (got == null || got.size() != want.length)
      ok = false; // 若 got 等于 null 或 got.大小() 不等于 want.长度) ok 赋值为 false;
    else { // 否则
      for (int i = 0; i < want.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
        if (!Arrays.equals(
            got.get(i), want[i][0])) { // 若 取反 Arrays.equals(got 查找 下标 i), want[下标 i][0]
          ok = false; // 把 false; 写入 ok
          System.out.println(
              "FAIL step "
                  + i
                  + " got "
                  + Arrays.toString(got.get(i))
                  + " want "
                  + Arrays.toString(want[i][0])); // 打印输出
        }
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
