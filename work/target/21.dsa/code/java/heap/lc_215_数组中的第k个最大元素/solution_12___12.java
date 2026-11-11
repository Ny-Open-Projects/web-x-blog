// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
package com.webfault.dsa; // 引入依赖

// 方案12: heapq.nlargest(k, nums)[-1]（降序排序取前 k 个的最后一个）
class Main { // 定义类型
  static int findKthLargest(int[] nums, int k) { // 定义函数/方法 findKthLargest
    int[] c = nums.clone(); // 把 数组.clone(); 写入 int[] c
    java.util.Arrays.sort(c); // 排序
    // 升序数组的倒数第 k 个即第 k 大，等价于 nlargest(k)[-1]
    return c[c.length - k]; // 返回 字符[字符.长度 减 下标 k]
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
