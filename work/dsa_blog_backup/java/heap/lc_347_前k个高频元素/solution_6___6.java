// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc347_solution66 { // 定义类型
  public int[] topKFrequent(int[] nums, int k) { // 定义函数/方法 topKFrequent
    Map<Integer, Integer> cnt =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> cnt
    for (int n : nums) { // for (int 元素个数 : 数组) {
      cnt.put(n, cnt.getOrDefault(n, 0) + 1); // 计数.put(元素个数, 计数.getOrDefault(元素个数, 0) 加 1);
    }
    int maxFreq = 0; // 把 0 存入 maxFreq
    for (int f : cnt.values()) { // for (int f : 计数.values()) {
      maxFreq = Math.max(maxFreq, f); // 把 Math.取较大值 maxFreq, f); 写入 maxFreq
    }
    List<List<Integer>> buckets =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> buckets
    for (int i = 0; i <= maxFreq; i++) { // 让 下标 i 从 0 开始计数，下标 i 不超过 maxFreq 就继续
      buckets.add(new ArrayList<>()); // buckets 追加 new ArrayList 小于 超过 ());
    }
    for (Map.Entry<Integer, Integer> e :
        cnt.entrySet()) { // for (Map.Entry 小于 Integer, Integer 超过 e : 计数.entrySet()) {
      buckets.get(e.getValue()).add(e.getKey()); // buckets 查找 e.getValue()) 追加 e.getKey());
    }
    int[] result = new int[k]; // 把 new int[下标 k]; 写入 int[] result
    int idx = 0; // 把 0 存入 idx
    for (int f = maxFreq; f > 0 && idx < k; f--) { // 让 f 从 maxFreq 开始计数，f 超过 0 且 idx 小于 下标 k 就继续
      for (int num : buckets.get(f)) { // for (int num : buckets 查找 f)) {
        result[idx++] = num; // 把 num; 写入 result[idx++]
        if (idx == k) break; // 若 idx 等于 下标 k) break;
      }
    }
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc347_solution66 s = new lc347_solution66(); // 把 new lc347_solution66(); 写入 lc347_solution66 s
    int[][] inputs = {{1, 1, 1, 2, 2, 3}, {1}, {4, 1, -1, 2, -1, 2, 3}};
    int[] ks = {2, 1, 2}; // 把 {2, 1, 2}; 写入 int[] ks
    int[][] wants = {{1, 2}, {1}, {-1, 2}}; // 把 { {1, 2}, {1}, { 减 1, 2} }; 写入 int[][] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int t = 0; t < inputs.length; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 inputs.长度 就继续
      int[] got =
          s.topKFrequent(
              inputs[t], ks[t]); // 把 字符串.topKFrequent(inputs[另一字符串], ks[另一字符串]); 写入 int[] got
      Arrays.sort(got); // 排序
      int[] w = wants[t].clone(); // 把 wants[另一字符串].clone(); 写入 int[] w
      Arrays.sort(w); // 排序
      if (!Arrays.equals(got, w)) { // 若 取反 Arrays.equals(got, 权重
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL topKFrequent("
                + Arrays.toString(inputs[t])
                + ","
                + ks[t]
                + ")="
                + Arrays.toString(got)
                + " want "
                + Arrays.toString(w)); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
