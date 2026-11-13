// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
package com.webfault.dsa; // 引入依赖

// 方案8: 计数排序（按值域计数，从大到小扫）
class Main { // 定义类型
  static int findKthLargest(int[] nums, int k) { // 定义函数/方法 findKthLargest
    int lo = Integer.MAX_VALUE,
        hi = Integer.MIN_VALUE; // 把 Integer.MAX_VALUE, 右边界 赋值为 Integer.MIN_VALUE 存入 左边界
    for (int x : nums) { // for (int x : 数组) {
      lo = Math.min(lo, x); // 把 Math.取较小值 左边界, x); 写入 左边界
      hi = Math.max(hi, x); // 把 Math.取较大值 右边界, x); 写入 右边界
    }
    int[] count = new int[hi - lo + 1]; // 把 new int[右边界 减 左边界 加 1]; 写入 int[] count
    for (int x : nums) count[x - lo]++; // for (int x : 数组) 计数[x 减 左边界] 加一 ;
    int remaining = k; // 把 下标 k 存入 remaining
    for (int v = hi; v >= lo; v--) { // 让 值 从 右边界 开始计数，值 不低于 左边界 就继续
      remaining -= count[v - lo]; // remaining累减 计数[值 减 左边界]
      if (remaining <= 0) return v; // 若 remaining 不超过 0，直接返回 值
    }
    return lo; // 返回 左边界
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = {{3, 2, 1, 5, 6, 4}, {3, 2, 3, 1, 2, 4, 5, 5, 6}, {1}, {2, 1}, {5, 5, 5}};
    int[] ks = {2, 4, 1, 2, 2}; // 把 {2, 4, 1, 2, 2}; 写入 int[] ks
    int[] wants = {5, 4, 1, 1, 5}; // 把 {5, 4, 1, 1, 5}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < cases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
      int got = findKthLargest(cases[i], ks[i]); // 把 findKthLargest(cases[下标 i], ks[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL findKthLargest(case"
                + i
                + ", k="
                + ks[i]
                + ")="
                + got
                + " want "
                + wants[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
