// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134701204
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  List<List<Integer>> subsets(int[] nums) { // 定义函数/方法 subsets
    List<List<Integer>> result =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> result
    List<Integer> path = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> path
    backtrack(0, path, nums, result); // backtrack(0, 当前路径, 数组, 结果);
    return result; // 返回 结果
  }

  void backtrack(
      int start, List<Integer> path, int[] nums, List<List<Integer>> result) { // 定义函数/方法 backtrack
    result.add(new ArrayList<>(path)); // 结果 追加 new ArrayList 小于 超过 (当前路径));
    for (int i = start; i < nums.length; i++) { // 让 下标 i 从 起点 开始计数，下标 i 小于 数组.长度 就继续
      path.add(nums[i]); // 当前路径 追加 数组[下标 i]);
      backtrack(i + 1, path, nums, result); // backtrack(下标 i 加 1, 当前路径, 数组, 结果);
      path.remove(path.size() - 1); // 当前路径 弹出 当前路径.大小() 减 1);
    }
  }

  static String key(List<Integer> x) {
    int[] t = new int[x.size()];
    for (int i = 0; i < x.size(); i++) t[i] = x.get(i);
    java.util.Arrays.sort(t);
    return java.util.Arrays.toString(t);
  } // 排序

  static boolean sameSet(List<List<Integer>> a, List<List<Integer>> b) { // 定义函数/方法 sameSet
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    Set<String> sa = new HashSet<>(), sb = new HashSet<>();
    for (List<Integer> x : a) sa.add(key(x)); // for (List 小于 Integer 超过 x : 数组) sa 追加 key(x));
    for (List<Integer> x : b) sb.add(key(x)); // for (List 小于 Integer 超过 x : b) sb 追加 key(x));
    return sa.equals(sb); // 返回 sa.equals(sb)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    List<List<Integer>> want =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> want
    want.add(new ArrayList<>()); // want 追加 new ArrayList 小于 超过 ());
    want.add(Arrays.asList(1)); // want 追加 Arrays.asList(1));
    want.add(Arrays.asList(2)); // want 追加 Arrays.asList(2));
    want.add(Arrays.asList(3)); // want 追加 Arrays.asList(3));
    want.add(Arrays.asList(1, 2)); // want 追加 Arrays.asList(1,2));
    want.add(Arrays.asList(1, 3)); // want 追加 Arrays.asList(1,3));
    want.add(Arrays.asList(2, 3)); // want 追加 Arrays.asList(2,3));
    want.add(Arrays.asList(1, 2, 3)); // want 追加 Arrays.asList(1,2,3));
    List<List<Integer>> got = s.subsets(new int[] {1, 2, 3});
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!sameSet(got, want)) {
      ok = false;
      System.out.println("FAIL got=" + got);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
