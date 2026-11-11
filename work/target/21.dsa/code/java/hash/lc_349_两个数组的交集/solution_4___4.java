// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133279737
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型
  static List<Integer> intersection(int[] nums1, int[] nums2) { // 定义函数/方法 intersection
    Set<Integer> s1 = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> s1
    for (int v : nums1) s1.add(v); // for (int 值 : 数组1) s1 追加 值);
    Set<Integer> res = new LinkedHashSet<>(); // 把 new LinkedHashSet 小于 超过 (); 写入 Set<Integer> res
    for (int v : nums2)
      if (s1.contains(v)) res.add(v); // for (int 值 : 数组2) if (s1 是否包含 值)) 结果 追加 值);
    return new ArrayList<>(res); // 返回 new ArrayList 小于 超过 (结果)
  }

  static boolean eqList(List<Integer> a, List<Integer> b, boolean sortRes) { // 定义函数/方法 eqList
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    List<Integer> x = new ArrayList<>(a), y = new ArrayList<>(b);
    if (sortRes) {
      Collections.sort(x);
      Collections.sort(y);
    } // 若 sortRes) { Collections 排序 x); Collections 排序 y); }
    for (int i = 0; i < x.size(); i++)
      if (!x.get(i).equals(y.get(i))) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 x.大小() 就继续
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] data = {{{1, 2, 2, 1}, {2, 2}}, {{4, 9, 5}, {9, 4, 9, 8, 4}}, {{1, 2}, {3, 4}}};
    int[][] wants = {{2}, {9, 4}, {}}; // 把 {{2}, {9,4}, {}}; 写入 int[][] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < data.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 data.长度 就继续
      List<Integer> got = intersection(data[i][0], data[i][1]);
      List<Integer> want = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> want
      for (int v : wants[i]) want.add(v); // for (int 值 : wants[下标 i]) want 追加 值);
      if (!eqList(got, want, true)) { // 若 取反 eqList(got, want, true
        System.out.println(
            "FAIL nums1="
                + Arrays.toString(data[i][0])
                + " nums2="
                + Arrays.toString(data[i][1])
                + " want="
                + want
                + " got="
                + got); // 打印输出
        ok = false; // 把 false; 写入 ok
      }
    }
    if (!ok) {
      System.out.println("RESULT: FAIL");
      System.exit(1);
    } // 若 取反 ok) { System.out.输出(「RESULT: FAIL」); System.exit(1); }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
