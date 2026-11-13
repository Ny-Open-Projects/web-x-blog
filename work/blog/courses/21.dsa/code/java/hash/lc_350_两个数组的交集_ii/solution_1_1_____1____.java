// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc350_solution11 { // 定义类型
  static List<Integer> intersect(int[] nums1, int[] nums2) { // 定义函数/方法 intersect
    if (nums1.length > nums2.length)
      return intersect(nums2, nums1); // 若 数组1.长度 超过 数组2.长度，直接返回 intersect(数组2, 数组1)
    Map<Integer, Integer> mp =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> mp
    for (int num : nums1) mp.put(num, mp.getOrDefault(num, 0) + 1);
    List<Integer> intersection =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> intersection
    for (int num : nums2) { // for (int num : 数组2) {
      if (mp.containsKey(num) && mp.get(num) > 0) { // 若 mp.containsKey(num) 且 mp 查找 num) 超过 0
        intersection.add(num); // intersection 追加 num);
        mp.put(num, mp.get(num) - 1); // mp.put(num, mp 查找 num) 减 1);
      }
    }
    return intersection; // 返回 intersection
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<Integer> got = intersect(new int[] {1, 2, 2, 1}, new int[] {2, 2});
    if (!(got.size() == 2
        && got.get(0) == 2
        && got.get(1) == 2)) // 若 取反 (got.大小() 等于 2 且 got 查找 0) 等于 2 且 got 查找 1) 等于 2
    throw new RuntimeException("FAILED: " + got); // throw new RuntimeException(「FAILED: 」 加 got);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
