// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
package com.webfault.dsa; // 引入依赖

// 方案3: 部分冒泡（仅排好最大的 k 个所在的尾部 k 个位置）
class Main { // 定义类型
  static int findKthLargest(int[] nums, int k) { // 定义函数/方法 findKthLargest
    int[] a = nums.clone(); // 把 数组.clone(); 写入 int[] a
    int length = a.length - 1; // 把 数组.长度 减 1 存入 长度
    for (int i = length; i > length - k; i--) { // 让 下标 i 从 长度 开始计数，下标 i 超过 长度 减 下标 k 就继续
      for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        if (a[j] > a[j + 1]) { // 若 数组[下标 j] 超过 数组[下标 j 加 1]
          int t = a[j]; // 把 数组[下标 j] 存入 另一字符串
          a[j] = a[j + 1]; // 把 数组[下标 j 加 1]; 写入 a[j]
          a[j + 1] = t; // 把 另一字符串; 写入 a[j + 1]
        }
      }
    }
    return a[length - k + 1]; // 返回 数组[长度 减 下标 k 加 1]
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
