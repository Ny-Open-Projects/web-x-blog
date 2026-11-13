// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc347_solution11 { // 定义类型
  static int[] topKFrequent(int[] nums, int k) { // 定义函数/方法 topKFrequent
    Map<Integer, Integer> map =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> map
    for (int n : nums) { // for (int 元素个数 : 数组) {
      map.put(n, map.getOrDefault(n, 0) + 1); // 映射表.put(元素个数, 映射表.getOrDefault(元素个数, 0) 加 1);
    }
    PriorityQueue<Integer> h = new PriorityQueue<>((a, b) -> map.get(b) - map.get(a));
    for (int key : map.keySet()) { // for (int key : 映射表.keySet()) {
      h.offer(key); // h.offer(key);
    }
    int[] result = new int[k]; // 把 new int[下标 k]; 写入 int[] result
    for (int i = 0; i < k; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 就继续
      result[i] = h.poll(); // 把 h.poll(); 写入 result[i]
    }
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] got =
        topKFrequent(
            new int[] {1, 1, 1, 2, 2, 3},
            2); // 把 topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2); 写入 int[] got
    if (got.length != 2) throw new RuntimeException("FAILED length: " + got.length);
    Set<Integer> set = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<Integer> set
    for (int v : got) set.add(v); // for (int 值 : got) set 追加 值);
    if (!(set.contains(1) && set.contains(2))) // 若 取反 (set 是否包含 1) 且 set 是否包含 2
    throw new RuntimeException("FAILED: " + Arrays.toString(got));
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
