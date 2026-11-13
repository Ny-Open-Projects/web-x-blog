// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134429994
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.Arrays; // 引入依赖
import java.util.Collections; // 引入依赖
import java.util.List; // 引入依赖

class solution_11___11 { // 定义类型
  static int firstMissingPositive(int[] nums) { // 定义函数/方法 firstMissingPositive
    if (nums.length == 0) return 1; // 若 数组.长度 等于 0，直接返回 1
    List<Integer> pos = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> pos
    for (int item : nums) { // for (int item : 数组) {
      if (item > 0) pos.add(item); // 若 item 超过 0) pos 追加 item);
    }
    if (pos.isEmpty()) return 1; // 若 pos.isEmpty()，直接返回 1
    Collections.sort(pos); // 排序
    if (pos.get(0) != 1) return 1; // 若 pos 查找 0) 不等于 1，直接返回 1
    int n = pos.size(); // 把 pos.大小() 存入 元素个数
    for (int i = 0; i < n - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
      if (pos.get(i + 1) - pos.get(i) > 1) { // 若 pos 查找 下标 i 加 1) 减 pos 查找 下标 i) 超过 1
        return pos.get(i) + 1; // 返回 pos 查找 下标 i) 加 1
      }
    }
    return pos.get(n - 1) + 1; // 返回 pos 查找 元素个数 减 1) 加 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean fail = false; // 把 false; 写入 boolean fail
    fail |= !check(new int[] {1, 2, 0}, 3); // 把 取反 check(new int[]{1, 2, 0}, 3); 写入 fail |
    fail |= !check(new int[] {3, 4, -1, 1}, 2); // 把 取反 check(new int[]{3, 4, 减 1, 1}, 2); 写入 fail |
    fail |=
        !check(
            new int[] {7, 8, 9, 11, 12}, 1); // 把 取反 check(new int[]{7, 8, 9, 11, 12}, 1); 写入 fail |
    if (fail) throw new RuntimeException("FAILED"); // 若 fail) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean check(int[] nums, int want) { // 定义判定函数 check
    int got = firstMissingPositive(nums); // 把 firstMissingPositive(数组) 存入 got
    if (got != want) { // 若 got 不等于 want
      System.out.println(
          "FAIL firstMissingPositive("
              + Arrays.toString(nums)
              + ")="
              + got
              + " want "
              + want); // 打印输出
      return false; // 返回 false
    }
    return true; // 返回 true
  }
}
