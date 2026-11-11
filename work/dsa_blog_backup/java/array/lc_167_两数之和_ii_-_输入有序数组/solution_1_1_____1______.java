// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145115578
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc167_solution111 { // 定义类型
  public int[] twoSum(int[] numbers, int target) { // 定义函数/方法 twoSum
    int n = numbers.length; // 把 numbers.长度 存入 元素个数
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      int remain = target - numbers[i]; // 把 目标值 减 numbers[下标 i] 存入 remain
      int low = i + 1; // 把 下标 i 加 1 存入 low
      int high = n - 1; // 把 元素个数 减 1 存入 high
      while (low <= high) { // 循环，直到不满足「low 不超过 high」
        int m = low + (high - low) / 2; // 把 (low 加 high) 除以 2 存入 映射表
        if (numbers[m] == remain) { // 若 numbers[映射表] 等于 remain
          return new int[] {i + 1, m + 1}; // 返回 new int[]{下标 i 加 1, 映射表 加 1}
        } else if (numbers[m] < remain) { // 否则，若 numbers[映射表] 小于 remain
          low = m + 1; // 把 映射表 加 1; 写入 low
        } else { // 否则
          high = m - 1; // 把 映射表 减 1; 写入 high
        }
      }
    }
    return new int[] {-1, -1}; // 返回 new int[]{ 减 1, 减 1}
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc167_solution111 s =
        new lc167_solution111(); // 把 new lc167_solution111(); 写入 lc167_solution111 s
    int[] r1 =
        s.twoSum(
            new int[] {2, 7, 11, 15}, 9); // 把 字符串.twoSum(new int[]{2, 7, 11, 15}, 9); 写入 int[] r1
    if (!(r1[0] == 1 && r1[1] == 2)) throw new RuntimeException("FAILED");
    int[] r2 =
        s.twoSum(
            new int[] {2, 7, 11, 15}, 99); // 把 字符串.twoSum(new int[]{2, 7, 11, 15}, 99); 写入 int[] r2
    if (!(r2[0] == -1 && r2[1] == -1)) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
