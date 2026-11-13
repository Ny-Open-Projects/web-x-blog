// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145344295
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class DupS2 { // 定义类型
  static boolean containsDuplicate(int[] nums) { // 定义函数/方法 containsDuplicate
    Arrays.sort(nums); // 排序
    for (int i = 1; i < nums.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] == nums[i - 1]) return true; // 若 数组[下标 i] 等于 数组[下标 i 减 1]，直接返回 true
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean[] got = { // 把 { 写入 boolean[] got
      DupS2.containsDuplicate(new int[] {1, 2, 3}),
      DupS2.containsDuplicate(new int[] {1, 2, 3, 1}),
      DupS2.containsDuplicate(new int[] {1}),
    };
    boolean[] want = {false, true, false}; // 把 { false, true, false }; 写入 boolean[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
