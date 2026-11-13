// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344649
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc295_solution333 { // 定义类型
  static class MedianFinder { // static class MedianFinder {
    List<Integer> nums = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> nums

    void addNum(int num) { // 定义函数/方法 addNum
      int i = Collections.binarySearch(nums, num); // 把 Collections.binarySearch(数组, num) 存入 下标 i
      if (i < 0) i = -i - 1; // 若 下标 i 小于 0) 下标 i 赋值为 减 下标 i 减 1;
      nums.add(i, num); // 数组 追加 下标 i, num);
    }

    Double findMedian() { // 定义函数/方法 findMedian
      int n = nums.size(); // 把 数组.大小() 存入 元素个数
      if (n == 0) return null; // 若 元素个数 等于 0，直接返回 null
      if (n % 2 == 1)
        return (double) nums.get(n / 2); // 若 元素个数 对…取模 2 等于 1，直接返回 (double) 数组 查找 元素个数 除以 2)
      return (nums.get(n / 2 - 1) + nums.get(n / 2))
          / 2.0; // 返回 (数组 查找 元素个数 除以 2 减 1) 加 数组 查找 元素个数 除以 2)) 除以 2.0
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    MedianFinder mf = new MedianFinder(); // 把 new MedianFinder(); 写入 MedianFinder mf
    for (int x : new int[] {1, 2, 3, 4, 5})
      mf.addNum(x); // for (int x : new int[]{1, 2, 3, 4, 5}) mf.addNum(x);
    Double got = mf.findMedian(); // 把 mf.findMedian(); 写入 Double got
    if (got == null || got != 3.0) throw new RuntimeException("FAILED: got " + got + " want 3.0");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
