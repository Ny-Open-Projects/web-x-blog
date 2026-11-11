// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
package com.webfault.dsa; // 引入依赖

import java.util.Random; // 引入依赖

// 方案11: 快速选择（Hoare 分区，随机 pivot）
class Main { // 定义类型
  static final Random RAND = new Random(); // 把 new Random(); 写入 static final Random RAND

  static int findKthLargest(int[] nums, int k) { // 定义函数/方法 findKthLargest
    int[] a = nums.clone(); // 把 数组.clone(); 写入 int[] a
    return quickselect(
        a, 0, a.length - 1, a.length - k); // 返回 quickselect(数组, 0, 数组.长度 减 1, 数组.长度 减 下标 k)
  }

  static int quickselect(int[] nums, int l, int r, int k) { // 定义函数/方法 quickselect
    if (l == r) { // 若 左指针 等于 右指针
      return nums[l]; // 返回 数组[左指针]
    }
    int pidx = l + RAND.nextInt(r - l + 1); // 把 左指针 加 RAND.nextInt(右指针 减 左指针 加 1) 存入 pidx
    int t = nums[l]; // 把 数组[左指针] 存入 另一字符串
    nums[l] = nums[pidx]; // 把 数组[pidx]; 写入 nums[l]
    nums[pidx] = t; // 把 另一字符串; 写入 nums[pidx]
    int pivot = nums[l]; // 把 数组[左指针] 存入 pivot
    int i = l - 1; // 把 左指针 减 1 存入 下标 i
    int j = r + 1; // 把 右指针 加 1 存入 下标 j
    while (i < j) { // 循环，直到不满足「下标 i 小于 下标 j」
      do { // do {
        i++; // 下标 i 加一
      } while (nums[i] < pivot); // } while (数组[下标 i] 小于 pivot);
      do { // do {
        j--; // 下标 j 减一
      } while (nums[j] > pivot); // } while (数组[下标 j] 超过 pivot);
      if (i < j) { // 若 下标 i 小于 下标 j
        int tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
        nums[i] = nums[j]; // 把 数组[下标 j]; 写入 nums[i]
        nums[j] = tmp; // 把 临时变量; 写入 nums[j]
      }
    }
    if (k <= j) { // 若 下标 k 不超过 下标 j
      return quickselect(nums, l, j, k); // 返回 quickselect(数组, 左指针, 下标 j, 下标 k)
    } else { // 否则
      return quickselect(nums, j + 1, r, k); // 返回 quickselect(数组, 下标 j 加 1, 右指针, 下标 k)
    }
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
