// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134701204
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  List<List<Integer>> subsets(int[] nums) { // 定义函数/方法 subsets
    List<List<Integer>> res =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> res
    res.add(new ArrayList<>()); // 结果 追加 new ArrayList 小于 超过 ());
    for (int num : nums) { // for (int num : 数组) {
      int sz = res.size(); // 把 结果.大小() 存入 sz
      for (int i = 0; i < sz; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 sz 就继续
        List<Integer> cur =
            new ArrayList<>(
                res.get(i)); // 把 new ArrayList 小于 超过 (结果 查找 下标 i)); 写入 List<Integer> cur
        cur.add(num); // 当前值 追加 num);
        res.add(cur); // 结果 追加 当前值);
      }
    }
    return res; // 返回 结果
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
