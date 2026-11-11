// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133322239
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class solution_3___3 { // 定义类型
  static int[] twoSum(int[] nums, int target) { // 定义函数/方法 twoSum
    int n = nums.length; // 把 数组.长度 存入 元素个数
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = i + 1; j < n; j++) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
        if (nums[i] + nums[j] == target) { // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值
          return new int[] {i, j}; // 返回 new int[]{下标 i, 下标 j}
        }
      }
    }
    return new int[] {}; // 返回 new int[]{}
  }

  static boolean eqArr(int[] a, int[] b) { // 定义函数/方法 eqArr
    if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    int[] x = a.clone(); // 把 数组.clone(); 写入 int[] x
    int[] y = b.clone(); // 把 b.clone(); 写入 int[] y
    Arrays.sort(x); // 排序
    Arrays.sort(y); // 排序
    return Arrays.equals(x, y); // 返回 Arrays.equals(x, y)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean fail = false; // 把 false; 写入 boolean fail
    fail |= !check(new int[] {2, 7, 11, 15}, 9, new int[] {0, 1});
    fail |= !check(new int[] {3, 2, 4}, 6, new int[] {1, 2});
    fail |=
        !check(
            new int[] {3, 3},
            6,
            new int[] {0, 1}); // 把 取反 check(new int[]{3, 3}, 6, new int[]{0, 1}); 写入 fail |
    if (fail) throw new RuntimeException("FAILED"); // 若 fail) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  static boolean check(int[] nums, int target, int[] want) { // 定义判定函数 check
    int[] got = twoSum(nums, target); // 把 twoSum(数组, 目标值); 写入 int[] got
    if (!eqArr(got, want)) { // 若 取反 eqArr(got, want
      System.out.println(
          "FAIL twoSum("
              + Arrays.toString(nums)
              + ","
              + target
              + ")="
              + Arrays.toString(got)
              + " want "
              + Arrays.toString(want)); // 打印输出
      return false; // 返回 false
    }
    return true; // 返回 true
  }
}
