// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ParityS4 { // 定义类型
  static int[] sortArrayByParityII(int[] nums) { // 定义函数/方法 sortArrayByParityII
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int j = 1; // 把 1 存入 下标 j
    for (int i = 0; i < n; i += 2) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if ((nums[i] & 1) == 1) { // 若 (数组[下标 i] 按位与 1) 等于 1
        while ((nums[j] & 1) == 1) j += 2; // 循环，直到不满足「(数组[下标 j] 按位与 1) 等于 1) 下标 j 累加 2;」
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
      }
    }
    return nums; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{4, 2, 5, 7}, {4, 5, 2, 7}},
      {{2, 3}, {2, 3}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got =
          ParityS4.sortArrayByParityII(
              c[0].clone()); // 把 ParityS4.sortArrayByParityII(字符[0].clone()); 写入 int[] got
      if (!Arrays.equals(got, c[1])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(c[0]) + " -> " + Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
