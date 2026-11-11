// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class SeqS2 { // 定义类型
  static int seqSearch(int[] nums, int target) { // 定义函数/方法 seqSearch
    for (int i = 0; i < nums.length; i++)
      if (nums[i] == target) return i; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] lst = {15, 4, 23, 52, 1}; // 把 {15, 4, 23, 52, 1}; 写入 int[] lst
    int[] got = {SeqS2.seqSearch(lst, 23), SeqS2.seqSearch(lst, 123)};
    int[] want = {2, -1}; // 把 { 2, 减 1 }; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!Arrays.equals(got, want)) { // 若 取反 Arrays.equals(got, want
      ok = false; // 把 false; 写入 ok
      System.out.println(
          "FAIL seqSearch got " + Arrays.toString(got) + " want " + Arrays.toString(want)); // 打印输出
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
