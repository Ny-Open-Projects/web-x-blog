// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345965
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class solution222FisherYates { // 定义类型
  private int[] nums; // private int[] 数组;
  private int[] original; // private int[] original;
  private Random rnd; // private Random rnd;

  public solution222FisherYates(int[] nums) { // 定义函数/方法 solution222FisherYates
    this.nums = nums.clone(); // 把 数组.clone(); 写入 数组
    this.original = nums.clone(); // 把 数组.clone(); 写入 this.original
    rnd = new Random(); // 把 new Random(); 写入 rnd
  }

  public int[] reset() { // 定义函数/方法 reset
    this.nums = original.clone(); // 把 original.clone(); 写入 数组
    return this.nums; // 返回 this.数组
  }

  public int[] shuffle() { // 定义函数/方法 shuffle
    int[] a = this.nums.clone(); // 把 this.数组.clone(); 写入 int[] a
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      int j = rnd.nextInt(a.length - i) + i; // 把 rnd.nextInt(数组.长度 减 下标 i) 加 下标 i 存入 下标 j
      int t = a[i];
      a[i] = a[j];
      a[j] = t;
    }
    this.nums = a; // 把 数组; 写入 数组
    return this.nums; // 返回 this.数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    solution222FisherYates s = new solution222FisherYates(new int[] {1, 2, 3});
    int[] r = s.reset(); // 把 字符串.reset(); 写入 int[] r
    if (!(r[0] == 1 && r[1] == 2 && r[2] == 3)) throw new RuntimeException("FAILED reset");
    int[] sh = s.shuffle(); // 把 字符串.shuffle(); 写入 int[] sh
    int[] sorted = sh.clone(); // 把 sh.clone(); 写入 int[] sorted
    Arrays.sort(sorted); // 排序
    if (!(sorted[0] == 1 && sorted[1] == 2 && sorted[2] == 3))
      throw new RuntimeException("FAILED shuffle");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
