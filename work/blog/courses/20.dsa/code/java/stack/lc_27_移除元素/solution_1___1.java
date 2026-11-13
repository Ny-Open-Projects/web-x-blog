// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114689
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc27_solution11 { // 定义类型
  static int removeElement(int[] nums, int val) { // 定义函数/方法 removeElement
    int left = 0; // 把 0 存入 左边界
    for (int right = 0; right < nums.length; right++) { // 让 右边界 从 0 开始计数，右边界 小于 数组.长度 就继续
      if (nums[right] != val) {
        nums[left] = nums[right];
        left++;
      } // 若 数组[右边界] 不等于 值) { 数组[左边界] 赋值为 数组[右边界]; 左边界 加一 ; }
    }
    return left; // 返回 左边界
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] nums = {3, 2, 2, 3}; // 把 {3, 2, 2, 3}; 写入 int[] nums
    int k = removeElement(nums, 3); // 把 removeElement(数组, 3) 存入 下标 k
    int[] head = Arrays.copyOf(nums, k); // 把 Arrays.copyOf(数组, 下标 k); 写入 int[] head
    if (k != 2 || !Arrays.equals(head, new int[] {2, 2}))
      throw new RuntimeException("FAILED k=" + k + " head=" + Arrays.toString(head));
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
