// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ShellS1 { // 定义类型
  static int[] shellSort(int[] nums) { // 定义函数/方法 shellSort
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int gap = n / 2; // 把 元素个数 除以 2 存入 gap
    while (gap > 0) { // 循环，直到不满足「gap 超过 0」
      for (int i = gap; i < n; i++) { // 让 下标 i 从 gap 开始计数，下标 i 小于 元素个数 就继续
        int temp = nums[i]; // 把 数组[下标 i] 存入 临时变量
        int j = i; // 把 下标 i 存入 下标 j
        while (j >= gap
            && nums[j - gap] > temp) { // 循环，直到不满足「下标 j 不低于 gap 且 数组[下标 j 减 gap] 超过 临时变量」
          nums[j] = nums[j - gap]; // 把 数组[下标 j 减 gap]; 写入 nums[j]
          j -= gap; // 下标 j累减 gap
        }
        nums[j] = temp; // 把 临时变量; 写入 nums[j]
      }
      gap /= 2; // 把 2; 写入 gap /
    }
    return nums; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{1, 2, 3}, {1, 2, 3}},
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{9, 12, 1, 3, -1, 22, 22, 31, 1, 0}, {-1, 0, 1, 1, 3, 9, 12, 22, 22, 31}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got =
          ShellS1.shellSort(c[0].clone()); // 把 ShellS1.shellSort(字符[0].clone()); 写入 int[] got
      if (!Arrays.equals(got, c[1])) { // 若 取反 Arrays.equals(got, 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL "
                + Arrays.toString(c[0])
                + " -> "
                + Arrays.toString(got)
                + " want "
                + Arrays.toString(c[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
