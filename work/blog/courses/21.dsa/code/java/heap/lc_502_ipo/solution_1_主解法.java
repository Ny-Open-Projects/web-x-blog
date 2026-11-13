// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347672
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc502_solution1 { // 定义类型
  public int findMaximizedCapital(
      int k, int w, int[] profits, int[] capital) { // 定义函数/方法 findMaximizedCapital
    int n = profits.length; // 把 profits.长度 存入 元素个数
    Integer[] indices = new Integer[n]; // 把 new Integer[元素个数]; 写入 Integer[] indices
    for (int i = 0; i < n; i++) indices[i] = i; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    Arrays.sort(indices, (a, b) -> capital[a] - capital[b]); // 排序
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
    int i = 0; // 把 0 存入 下标 i
    for (int t = 0; t < k; t++) { // 让 另一字符串 从 0 开始计数，另一字符串 小于 下标 k 就继续
      while (i < n
          && capital[indices[i]] <= w) { // 循环，直到不满足「下标 i 小于 元素个数 且 capital[indices[下标 i]] 不超过 权重」
        maxHeap.offer(profits[indices[i]]); // maxHeap.offer(profits[indices[下标 i]]);
        i++; // 下标 i 加一
      }
      if (maxHeap.isEmpty()) break; // 若 maxHeap.isEmpty()) break;
      w += maxHeap.poll(); // 权重累加 maxHeap.poll()
    }
    return w; // 返回 权重
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc502_solution1 s = new lc502_solution1(); // 把 new lc502_solution1(); 写入 lc502_solution1 s
    int[][] cases = { // 把 { 写入 int[][] cases
      {2, 0, 4}, // k, w, want  (profits/capital follow)
    };
    // cases: (k, w, profits[], capital[], want)
    Object[] t1 = new Object[] {2, 0, new int[] {1, 2, 3}, new int[] {0, 1, 1}, 4};
    Object[] t2 = new Object[] {1, 0, new int[] {1, 2, 3}, new int[] {1, 2, 3}, 0};
    Object[] t3 = new Object[] {3, 0, new int[] {1, 2, 3}, new int[] {0, 1, 1}, 6};
    Object[][] tests = {t1, t2, t3}; // 把 {t1, t2, t3}; 写入 Object[][] tests
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] t : tests) { // for (Object[] 另一字符串 : tests) {
      int k = (int) t[0]; // 把 (int) 另一字符串[0] 存入 下标 k
      int w = (int) t[1]; // 把 (int) 另一字符串[1] 存入 权重
      int[] profits = (int[]) t[2]; // 把 (int[]) 另一字符串[2]; 写入 int[] profits
      int[] capital = (int[]) t[3]; // 把 (int[]) 另一字符串[3]; 写入 int[] capital
      int want = (int) t[4]; // 把 (int) 另一字符串[4] 存入 want
      int got = s.findMaximizedCapital(k, w, profits, capital);
      if (got != want) { // 若 got 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL findMaximizedCapital(" + k + "," + w + ")=" + got + " want " + want); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
