// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134689827
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc46 { // 定义类型
  List<List<Integer>> permute(int[] nums) { // 定义函数/方法 permute
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    backtrack(nums, new ArrayList<>(), res); // backtrack(数组, new ArrayList 小于 超过 (), 结果);
    return res; // 返回 结果
  }

  void backtrack(int[] nums, List<Integer> path, List<List<Integer>> res) { // 定义函数/方法 backtrack
    if (path.size() == nums.length) {
      res.add(new ArrayList<>(path));
      return;
    }
    for (int i = 0; i < nums.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (path.contains(nums[i])) continue; // 若 当前路径 是否包含 数组[下标 i])) continue;
      path.add(nums[i]); // 当前路径 追加 数组[下标 i]);
      backtrack(nums, path, res); // backtrack(数组,当前路径,结果);
      path.remove(path.size() - 1); // 当前路径 弹出 当前路径.大小() 减 1);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args){
    Lc46 s = new Lc46(); // 把 new Lc46(); 写入 Lc46 s
    List<List<Integer>> got =
        s.permute(
            new int[] {1, 2, 3}); // 把 字符串.permute(new int[]{1,2,3}); 写入 List<List<Integer>> got
    Set<String> want = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<String> want
    String[] ws = {"1,2,3", "1,3,2", "2,1,3", "2,3,1", "3,1,2", "3,2,1"};
    for (String w : ws) want.add(w); // for(String 权重:ws) want 追加 权重);
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
        got.size() == 6
            && gotSet.equals(want); // 把 got.大小() 等于 6 且 gotSet.equals(want); 写入 boolean ok
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
