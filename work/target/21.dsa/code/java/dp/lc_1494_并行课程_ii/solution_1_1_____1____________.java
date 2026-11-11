// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145380711
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc1494_solution111 { // 定义类型
  private int n, k; // private int 元素个数, 下标 k;
  private int[] pre; // private int[] 前缀和;
  private HashMap<Integer, Integer> memo = new HashMap<>();

  public int minNumberOfSemesters(int n, int[][] relations, int k) { // 定义函数/方法 minNumberOfSemesters
    this.n = n; // 把 元素个数; 写入 元素个数
    this.k = k; // 把 下标 k; 写入 下标 k
    pre = new int[n]; // 把 new int[元素个数]; 写入 前缀和
    for (int[] r : relations) { // for (int[] 右指针 : relations) {
      pre[r[1] - 1] |= 1 << (r[0] - 1); // 把 1 小于 小于 (右指针[0] 减 1); 写入 pre[r[1] - 1] |
    }
    memo.clear(); // 记忆化表.clear();
    return dfs(0); // 返回 dfs(0)
  }

  private int dfs(int mask) { // 定义函数/方法 dfs
    if (memo.containsKey(mask))
      return memo.get(mask); // 若 记忆化表.containsKey(mask)，直接返回 记忆化表 查找 mask)
    int target = (1 << n) - 1; // 把 (1 小于 小于 元素个数) 减 1 存入 目标值
    if (mask == target) return 0; // 若 mask 等于 目标值，直接返回 0
    ArrayList<Integer> cand =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> cand
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if (((mask >> i) & 1) == 0 && (pre[i] & mask) == pre[i]) {
        cand.add(i); // cand 追加 下标 i);
      }
    }
    int[] best = {n + 1}; // 把 {元素个数 加 1}; 写入 int[] best
    int sz = Math.min(k, cand.size()); // 把 Math.取较小值 下标 k, cand.大小()) 存入 sz
    combine(
        mask,
        cand,
        0,
        new ArrayList<>(),
        sz,
        best); // combine(mask, cand, 0, new ArrayList 小于 超过 (), sz, 当前最优);
    memo.put(mask, best[0]); // 记忆化表.put(mask, 当前最优[0]);
    return best[0]; // 返回 当前最优[0]
  }

  private void combine(
      int mask,
      ArrayList<Integer> cand,
      int start,
      ArrayList<Integer> cur,
      int sz,
      int[] best) { // ArrayList 小于 Integer 超过 当前值, int sz, int[] 当前最优) {
    if (cur.size() >= 1) { // 若 当前值.大小() 不低于 1
      int nmask = mask; // 把 mask 存入 nmask
      for (int c : cur) nmask |= (1 << c); // 把 (1 小于 小于 字符); 写入 for (int c : cur) nmask |
      best[0] =
          Math.min(best[0], 1 + dfs(nmask)); // 把 Math.取较小值 当前最优[0], 1 加 dfs(nmask)); 写入 best[0]
    }
    if (cur.size() == sz) return; // 若 当前值.大小() 等于 sz) return;
    for (int i = start; i < cand.size(); i++) { // 让 下标 i 从 起点 开始计数，下标 i 小于 cand.大小() 就继续
      cur.add(cand.get(i)); // 当前值 追加 cand 查找 下标 i));
      combine(mask, cand, i + 1, cur, sz, best); // combine(mask, cand, 下标 i 加 1, 当前值, sz, 当前最优);
      cur.remove(cur.size() - 1); // 当前值 弹出 当前值.大小() 减 1);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc1494_solution111 s =
        new lc1494_solution111(); // 把 new lc1494_solution111(); 写入 lc1494_solution111 s
    int got = s.minNumberOfSemesters(4, new int[][] {{2, 1}, {3, 1}, {1, 4}}, 2);
    if (got != 3) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
