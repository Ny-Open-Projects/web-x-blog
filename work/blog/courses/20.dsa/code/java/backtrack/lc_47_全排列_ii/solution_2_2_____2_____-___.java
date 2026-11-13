// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233874
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc47 { // 定义类型
  List<List<Integer>> permuteUnique(int[] nums) { // 定义函数/方法 permuteUnique
    Arrays.sort(nums); // 排序
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    boolean[] used = new boolean[nums.length]; // 把 new boolean[数组.长度]; 写入 boolean[] used
    backtrack(
        nums, used, new ArrayList<>(), res); // backtrack(数组, 已用标记, new ArrayList 小于 超过 (), 结果);
    return res; // 返回 结果
  }

  void backtrack(
      int[] nums,
      boolean[] used,
      List<Integer> path,
      List<List<Integer>> res) { // 定义函数/方法 backtrack
    if (path.size() == nums.length) {
      res.add(new ArrayList<>(path));
      return;
    }
    for (int i = 0; i < nums.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (used[i]) continue; // 若 已用标记[下标 i]) continue;
      if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
      used[i] = true;
      path.add(nums[i]); // 把 true; 当前路径 追加 数组[下标 i]); 写入 used[i]
      backtrack(nums, used, path, res); // backtrack(数组,已用标记,当前路径,结果);
      path.remove(path.size() - 1);
      used[i] = false; // 把 false; 写入 path.remove(path.size()-1); used[i]
    }
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc47 s = new Lc47(); // 把 new Lc47(); 写入 Lc47 s
    List<List<Integer>> got = s.permuteUnique(new int[] {1, 1, 2});
    Set<String> want = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<String> want
    want.add("1,1,2");
    want.add("1,2,1");
    want.add("2,1,1"); // want 追加 「1,1,2」);want 追加 「1,1,2」);want 追加 「1,1,2」);
    Set<String> gotSet = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<String> gotSet
    for (List<Integer> p : got) {
      StringBuilder sb = new StringBuilder();
      for (int v : p) {
        if (sb.length() > 0) sb.append(",");
        sb.append(v);
      }
      gotSet.add(sb.toString());
    } // 把 「,」 追加到列表尾部
    boolean ok =
        got.size() == 3
            && gotSet.equals(want); // 把 got.大小() 等于 3 且 gotSet.equals(want); 写入 boolean ok
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
