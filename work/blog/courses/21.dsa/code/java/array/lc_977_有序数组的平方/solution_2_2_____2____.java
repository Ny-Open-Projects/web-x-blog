// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

class Main { // 定义类型
  static int[] sortedSquares(int[] nums) { // 定义函数/方法 sortedSquares
    int n = nums.length;
    int[] res = new int[n];
    int i = 0, j = n - 1, k = n - 1;
    while (i <= j) { // 循环，直到不满足「下标 i 不超过 下标 j」
      int a = nums[i] * nums[i],
          b = nums[j] * nums[j]; // 把 数组[下标 i] 乘 数组[下标 i], b 赋值为 数组[下标 j] 乘 数组[下标 j] 存入 数组
      if (a > b) {
        res[k] = a;
        i++;
      } else {
        res[k] = b;
        j--;
      }
      k--; // 下标 k 减一
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{-4, -1, 0, 3, 10}, {1, 2, 3}, {-7, -3, 2, 3, 11}};
    int[][] ws = {
      {0, 1, 9, 16, 100}, {1, 4, 9}, {4, 9, 9, 49, 121}
    }; // 把 {{0,1,9,16,100},{1,4,9},{4,9,9,49,121}}; 写入 int[][] ws
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      int[] got = sortedSquares(ins[i]); // 把 sortedSquares(ins[下标 i]); 写入 int[] got
      if (!Arrays.equals(got, ws[i])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
