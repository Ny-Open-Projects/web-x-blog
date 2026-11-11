// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

/**
 * LeetCode 26. 删除有序数组中的重复项 忠实翻译自 python/queue/lc_26_删除有序数组中的重复项/solution_2_1_____1_____.py
 * slow/fast 双指针，返回 slow + 1
 */
class Main { // 定义类型
  int removeDuplicates(int[] nums) { // 定义函数/方法 removeDuplicates
    if (nums.length == 0) { // 若 数组.长度 等于 0
      return 0; // 返回 0
    }
    int slow = 0; // 把 0 存入 慢指针
    for (int fast = 1; fast < nums.length; fast++) { // 让 快指针 从 1 开始计数，快指针 小于 数组.长度 就继续
      if (nums[fast] != nums[slow]) { // 若 数组[快指针] 不等于 数组[慢指针]
        slow++; // 慢指针 加一
        nums[slow] = nums[fast]; // 把 数组[快指针]; 写入 nums[slow]
      }
    }
    return slow + 1; // 返回 慢指针 加 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    int[][] inputs = { // 把 { 写入 int[][] inputs
      {1, 1, 2},
      {0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
      {},
      {1},
      {1, 1, 1},
      {1, 2, 3},
    };
    int[] wants = {2, 5, 0, 1, 1, 3}; // 把 {2, 5, 0, 1, 1, 3}; 写入 int[] wants
    int[][] wantPrefix = { // 把 { 写入 int[][] wantPrefix
      {1, 2},
      {0, 1, 2, 3, 4},
      {},
      {1},
      {1},
      {1, 2, 3},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < inputs.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 inputs.长度 就继续
      int[] nums = inputs[ci].clone(); // 把 inputs[ci].clone(); 写入 int[] nums
      int k = s.removeDuplicates(nums); // 把 字符串.removeDuplicates(数组) 存入 下标 k
      int[] pre = Arrays.copyOf(nums, k); // 把 Arrays.copyOf(数组, 下标 k); 写入 int[] pre
      if (k != wants[ci]
          || !Arrays.equals(
              pre, wantPrefix[ci])) { // 若 下标 k 不等于 wants[ci] 或 取反 Arrays.equals(前缀和, wantPrefix[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL case "
                + ci
                + " k="
                + k // 打印输出
                + " prefix="
                + Arrays.toString(pre) // 把 " 加 Arrays.toString(前缀和) 写入 + " prefix
                + " want k="
                + wants[ci]
                + " prefix="
                + Arrays.toString(wantPrefix[ci]));
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
