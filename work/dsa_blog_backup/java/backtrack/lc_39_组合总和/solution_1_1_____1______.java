// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239508
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc39_solution111 { // 定义类型
  public List<List<Integer>> combinationSum(
      int[] candidates, int target) { // 定义函数/方法 combinationSum
    Arrays.sort(candidates); // 排序
    List<List<Integer>> result =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> result
    backtrack(
        candidates,
        target,
        0,
        new ArrayList<>(),
        result); // backtrack(候选数组, 目标值, 0, new ArrayList 小于 超过 (), 结果);
    return result; // 返回 结果
  }

  private void backtrack(
      int[] c,
      int remaining,
      int start,
      List<Integer> path,
      List<List<Integer>> result) { // 定义函数/方法 backtrack
    if (remaining == 0) { // 若 remaining 等于 0
      result.add(new ArrayList<>(path)); // 结果 追加 new ArrayList 小于 超过 (当前路径));
      return; // return;
    }
    for (int i = start; i < c.length; i++) { // 让 下标 i 从 起点 开始计数，下标 i 小于 字符.长度 就继续
      if (c[i] > remaining) break; // 若 字符[下标 i] 超过 remaining) break;
      path.add(c[i]); // 当前路径 追加 字符[下标 i]);
      backtrack(
          c,
          remaining - c[i],
          i,
          path,
          result); // backtrack(字符, remaining 减 字符[下标 i], 下标 i, 当前路径, 结果);
      path.remove(path.size() - 1); // 当前路径 弹出 当前路径.大小() 减 1);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc39_solution111 s = new lc39_solution111(); // 把 new lc39_solution111(); 写入 lc39_solution111 s
    List<List<Integer>> r = s.combinationSum(new int[] {2, 3, 6, 7}, 7);
    List<List<Integer>> exp =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> exp
    exp.add(Arrays.asList(2, 2, 3)); // exp 追加 Arrays.asList(2, 2, 3));
    exp.add(Arrays.asList(7)); // exp 追加 Arrays.asList(7));
    if (!r.equals(exp)) throw new RuntimeException("FAILED: " + r);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
