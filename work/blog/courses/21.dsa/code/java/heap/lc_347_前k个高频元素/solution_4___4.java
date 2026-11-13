// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc347_solution44 { // 定义类型
  public int[] topKFrequent(int[] nums, int k) { // 定义函数/方法 topKFrequent
    Map<Integer, Integer> freq =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> freq
    for (int n : nums) { // for (int 元素个数 : 数组) {
      freq.put(n, freq.getOrDefault(n, 0) + 1); // 频次表.put(元素个数, 频次表.getOrDefault(元素个数, 0) 加 1);
    }
    List<Map.Entry<Integer, Integer>> list = new ArrayList<>(freq.entrySet());
    list.sort((a, b) -> b.getValue() - a.getValue()); // 排序
    int[] result = new int[k]; // 把 new int[下标 k]; 写入 int[] result
    for (int i = 0; i < k; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 就继续
      result[i] = list.get(i).getKey(); // 把 列表 查找 下标 i).getKey(); 写入 result[i]
    }
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc347_solution44 s = new lc347_solution44(); // 把 new lc347_solution44(); 写入 lc347_solution44 s
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
