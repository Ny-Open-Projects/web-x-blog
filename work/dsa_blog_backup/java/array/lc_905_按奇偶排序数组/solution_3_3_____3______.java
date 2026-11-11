// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc905_solution333 { // 定义类型
  public int[] sortArrayByParity(int[] nums) { // 定义函数/方法 sortArrayByParity
    int left = 0, right = nums.length - 1; // 把 0, 右边界 赋值为 数组.长度 减 1 存入 左边界
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
      while (left < right && nums[left] % 2 == 0) { // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 对…取模 2 等于 0」
        left++; // 左边界 加一
      }
      while (left < right && nums[right] % 2 == 1) { // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 对…取模 2 等于 1」
        right--; // 右边界 减一
      }
      if (left < right) { // 若 左边界 小于 右边界
        int temp = nums[left]; // 把 数组[左边界] 存入 临时变量
        nums[left] = nums[right]; // 把 数组[右边界]; 写入 nums[left]
        nums[right] = temp; // 把 临时变量; 写入 nums[right]
        left++; // 左边界 加一
        right--; // 右边界 减一
      }
    }
    return nums; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc905_solution333 s =
        new lc905_solution333(); // 把 new lc905_solution333(); 写入 lc905_solution333 s
    int[] r =
        s.sortArrayByParity(
            new int[] {1, 2, 3}); // 把 字符串.sortArrayByParity(new int[]{1, 2, 3}); 写入 int[] r
    if (!(r[0] == 2 && r[1] == 1 && r[2] == 3)) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
