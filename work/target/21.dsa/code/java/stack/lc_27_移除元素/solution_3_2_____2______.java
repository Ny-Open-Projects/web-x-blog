// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc27_solution322 { // 定义类型
  static int removeElement(int[] nums, int val) { // 定义函数/方法 removeElement
    int left = 0, right = nums.length - 1; // 把 0, 右边界 赋值为 数组.长度 减 1 存入 左边界
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      if (nums[left] == val) {
        nums[left] = nums[right];
        right--;
      } // 若 数组[左边界] 等于 值) { 数组[左边界] 赋值为 数组[右边界]; 右边界 减一 ; }
      else left++; // 否则
    }
    return left; // 返回 左边界
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] nums = {1, 2, 3}; // 把 {1, 2, 3}; 写入 int[] nums
    int k = removeElement(nums, 1); // 把 removeElement(数组, 1) 存入 下标 k
    if (k != 2) throw new RuntimeException("FAILED k=" + k);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
