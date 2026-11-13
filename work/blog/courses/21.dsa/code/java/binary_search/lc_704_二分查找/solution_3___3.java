// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc704_solution33 { // 定义类型
  public int search(int[] nums, int target) { // 定义函数/方法 search
    int low = 0, high = nums.length - 1; // 把 0, high 赋值为 数组.长度 减 1 存入 low
    while (low <= high) { // 循环，直到不满足「low 不超过 high」
      int mid = (low + high) >>> 1; // 把 (low 加 high) 超过 超过 超过 1 存入 中点
      if (nums[mid] == target) { // 若 数组[中点] 等于 目标值
        return mid; // 返回 中点
      } else if (nums[mid] < target) { // 否则，若 数组[中点] 小于 目标值
        low = mid + 1; // 把 中点 加 1; 写入 low
      } else { // 否则
        high = mid - 1; // 把 中点 减 1; 写入 high
      }
    }
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc704_solution33 s = new lc704_solution33(); // 把 new lc704_solution33(); 写入 lc704_solution33 s
    int[][] numsList = {{1, 2, 3}, {-1, 0, 3, 5, 9, 12}, {1, 2, 3}};
    int[] targets = {1, 9, 4}; // 把 {1, 9, 4}; 写入 int[] targets
    int[] wants = {0, 4, -1}; // 把 {0, 4, 减 1}; 写入 int[] wants
    for (int i = 0; i < targets.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 targets.长度 就继续
      int got =
          s.search(numsList[i], targets[i]); // 把 字符串.search(numsList[下标 i], targets[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        System.out.println("FAIL search case " + i + " got " + got + " want " + wants[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
