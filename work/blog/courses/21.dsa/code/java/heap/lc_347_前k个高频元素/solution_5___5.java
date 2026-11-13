// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc347_solution55 { // 定义类型
  public int[] topKFrequent(int[] nums, int k) { // 定义函数/方法 topKFrequent
    Map<Integer, Integer> cnt =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> cnt
    for (int n : nums) { // for (int 元素个数 : 数组) {
      cnt.put(n, cnt.getOrDefault(n, 0) + 1); // 计数.put(元素个数, 计数.getOrDefault(元素个数, 0) 加 1);
    }
    PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    for (Map.Entry<Integer, Integer> e :
        cnt.entrySet()) { // for (Map.Entry 小于 Integer, Integer 超过 e : 计数.entrySet()) {
      heap.offer(
          new int[] {e.getValue(), e.getKey()}); // 堆.offer(new int[]{e.getValue(), e.getKey()});
      if (heap.size() > k) { // 若 堆.大小() 超过 下标 k
        heap.poll(); // 堆.poll();
      }
    }
    int[] result = new int[k]; // 把 new int[下标 k]; 写入 int[] result
    int i = 0; // 把 0 存入 下标 i
    while (!heap.isEmpty()) { // 循环，直到不满足「取反 堆.isEmpty(」
      result[i++] = heap.poll()[1]; // 把 堆.poll()[1]; 写入 result[i++]
    }
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc347_solution55 s = new lc347_solution55(); // 把 new lc347_solution55(); 写入 lc347_solution55 s
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
