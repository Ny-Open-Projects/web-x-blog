// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145115578
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc167_solution222 { // 定义类型
  public int[] twoSum(int[] numbers, int target) { // 定义函数/方法 twoSum
    int left = 0, right = numbers.length - 1; // 把 0, 右边界 赋值为 numbers.长度 减 1 存入 左边界
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
      int sum = numbers[left] + numbers[right]; // 把 numbers[左边界] 加 numbers[右边界] 存入 累计和
      if (sum == target)
        return new int[] {left + 1, right + 1}; // 若 累计和 等于 目标值，直接返回 new int[]{左边界 加 1, 右边界 加 1}
      else if (sum < target) left++; // 否则，若 累计和 小于 目标值) 左边界 加一 ;
      else right--; // 否则
    }
    return new int[] {-1, -1}; // 返回 new int[]{ 减 1, 减 1}
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc167_solution222 s =
        new lc167_solution222(); // 把 new lc167_solution222(); 写入 lc167_solution222 s
    int[] r =
        s.twoSum(
            new int[] {2, 7, 11, 15}, 9); // 把 字符串.twoSum(new int[]{2, 7, 11, 15}, 9); 写入 int[] r
    if (!(r[0] == 1 && r[1] == 2)) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
