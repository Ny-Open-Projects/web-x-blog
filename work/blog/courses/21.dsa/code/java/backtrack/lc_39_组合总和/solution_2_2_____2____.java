// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239508
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc39_solution222 { // 定义类型
  public List<List<Integer>> combinationSum(
      int[] candidates, int target) { // 定义函数/方法 combinationSum
    Arrays.sort(candidates); // 排序
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    backtrack(
        candidates,
        target,
        0,
        new ArrayList<>(),
        res); // backtrack(候选数组, 目标值, 0, new ArrayList 小于 超过 (), 结果);
    return res; // 返回 结果
  }

  private void backtrack(
      int[] c,
      int target,
      int start,
      List<Integer> cur,
      List<List<Integer>> res) { // 定义函数/方法 backtrack
    if (target == 0) { // 若 目标值 等于 0
      res.add(new ArrayList<>(cur)); // 结果 追加 new ArrayList 小于 超过 (当前值));
      return; // return;
    }
    for (int i = start; i < c.length; i++) { // 让 下标 i 从 起点 开始计数，下标 i 小于 字符.长度 就继续
      if (c[i] > target) continue; // 若 字符[下标 i] 超过 目标值) continue;
      cur.add(c[i]); // 当前值 追加 字符[下标 i]);
      backtrack(c, target - c[i], i, cur, res); // backtrack(字符, 目标值 减 字符[下标 i], 下标 i, 当前值, 结果);
      cur.remove(cur.size() - 1); // 当前值 弹出 当前值.大小() 减 1);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc39_solution222 s = new lc39_solution222(); // 把 new lc39_solution222(); 写入 lc39_solution222 s
    List<List<Integer>> r = s.combinationSum(new int[] {2, 3, 6, 7}, 7);
    List<List<Integer>> exp =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> exp
    exp.add(Arrays.asList(2, 2, 3)); // exp 追加 Arrays.asList(2, 2, 3));
    exp.add(Arrays.asList(7)); // exp 追加 Arrays.asList(7));
    if (!r.equals(exp)) throw new RuntimeException("FAILED: " + r);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
