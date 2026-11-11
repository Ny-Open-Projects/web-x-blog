// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345965
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc384_solution111 { // 定义类型
  private int[] nums; // private int[] 数组;
  private int[] original; // private int[] original;
  private Random rnd; // private Random rnd;

  public lc384_solution111(int[] nums) { // 定义函数/方法 lc384_solution111
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
    for (int i = a.length - 1; i > 0; i--) { // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 超过 0 就继续
      int j = rnd.nextInt(i + 1); // 把 rnd.nextInt(下标 i 加 1) 存入 下标 j
      int t = a[i];
      a[i] = a[j];
      a[j] = t;
    }
    this.nums = a; // 把 数组; 写入 数组
    return this.nums; // 返回 this.数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc384_solution111 s = new lc384_solution111(new int[] {1, 2, 3});
    int[] r = s.reset(); // 把 字符串.reset(); 写入 int[] r
    if (!(r[0] == 1 && r[1] == 2 && r[2] == 3)) throw new RuntimeException("FAILED reset");
    int[] sh = s.shuffle(); // 把 字符串.shuffle(); 写入 int[] sh
    int[] sorted = sh.clone(); // 把 sh.clone(); 写入 int[] sorted
    Arrays.sort(sorted); // 排序
    if (!(sorted[0] == 1 && sorted[1] == 2 && sorted[2] == 3))
      throw new RuntimeException("FAILED shuffle");
    int[] r2 = s.reset(); // 把 字符串.reset(); 写入 int[] r2
    if (!(r2[0] == 1 && r2[1] == 2 && r2[2] == 3)) throw new RuntimeException("FAILED reset2");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
