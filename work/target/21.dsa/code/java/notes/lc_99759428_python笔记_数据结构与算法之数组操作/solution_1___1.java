// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ArrOpsS1 { // 定义类型
  static int[] twoSum(int[] nums, int target) { // 定义函数/方法 twoSum
    Map<Integer, Integer> mp =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> mp
    for (int i = 0; i < nums.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      int complement = target - nums[i]; // 把 目标值 减 数组[下标 i] 存入 complement
      if (mp.containsKey(complement)) return new int[] {mp.get(complement), i};
      mp.put(nums[i], i); // mp.put(数组[下标 i], 下标 i);
    }
    return new int[] {}; // 返回 new int[]{}
  }

  static int maxSubArray(int[] nums) { // 定义函数/方法 maxSubArray
    int maxSum = nums[0], currentSum = nums[0]; // 把 数组[0], currentSum 赋值为 数组[0] 存入 maxSum
    for (int i = 1; i < nums.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      currentSum =
          Math.max(
              nums[i],
              currentSum + nums[i]); // 把 Math.取较大值 数组[下标 i], currentSum 加 数组[下标 i]); 写入 currentSum
      maxSum = Math.max(maxSum, currentSum); // 把 Math.取较大值 maxSum, currentSum); 写入 maxSum
    }
    return maxSum; // 返回 maxSum
  }

  static void rotateArray(int[] nums, int k) { // 定义函数/方法 rotateArray
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return; // 若 元素个数 等于 0) return;
    k %= n; // 把 元素个数; 写入 k %
    reverse(nums, 0, n - 1); // reverse(数组, 0, 元素个数 减 1);
    reverse(nums, 0, k - 1); // reverse(数组, 0, 下标 k 减 1);
    reverse(nums, k, n - 1); // reverse(数组, 下标 k, 元素个数 减 1);
  }

  static void reverse(int[] a, int l, int r) { // 定义函数/方法 reverse
    while (l < r) {
      int t = a[l];
      a[l] = a[r];
      a[r] = t;
      l++;
      r--;
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok
    int[] ts =
        ArrOpsS1.twoSum(
            new int[] {2, 7, 11, 15},
            9); // 把 ArrOpsS1.twoSum(new int[]{2, 7, 11, 15}, 9); 写入 int[] ts
    if (!Arrays.equals(ts, new int[] {0, 1})) {
      ok = false;
      System.out.println("FAIL twoSum=" + Arrays.toString(ts));
    }
    int ms = ArrOpsS1.maxSubArray(new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4});
    if (ms != 6) {
      ok = false;
      System.out.println("FAIL maxSubArray=" + ms);
    }
    int[] rot = {1, 2, 3, 4, 5}; // 把 {1, 2, 3, 4, 5}; 写入 int[] rot
    ArrOpsS1.rotateArray(rot, 2); // ArrOpsS1.rotateArray(rot, 2);
    if (!Arrays.equals(rot, new int[] {4, 5, 1, 2, 3})) {
      ok = false;
      System.out.println("FAIL rotateArray=" + Arrays.toString(rot));
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
