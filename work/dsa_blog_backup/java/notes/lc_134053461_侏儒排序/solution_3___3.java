// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class GnomeS3 { // 定义类型
  static void gnomeSort(int[] arr) { // 定义函数/方法 gnomeSort
    int length = arr.length; // 把 数组.长度 存入 长度
    int i = 1; // 把 1 存入 下标 i
    while (i < length) { // 循环，直到不满足「下标 i 小于 长度」
      if (i < 1 || arr[i - 1] <= arr[i]) { // 若 下标 i 小于 1 或 数组[下标 i 减 1] 不超过 数组[下标 i]
        i++; // 下标 i 加一
      } else { // 否则
        int t = arr[i - 1];
        arr[i - 1] = arr[i];
        arr[i] = t;
        i--; // 下标 i 减一
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{3, 1, 4, 1, 5, 9, 2, 6}, {1, 1, 2, 3, 4, 5, 6, 9}},
      {{1}, {1}},
      {{2, 1}, {1, 2}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] in = c[0].clone(); // 把 字符[0].clone(); 写入 int[] in
      gnomeSort(in); // gnomeSort(in);
      if (!Arrays.equals(in, c[1])) { // 若 取反 Arrays.equals(in, 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL "
                + Arrays.toString(c[0])
                + " -> "
                + Arrays.toString(in)
                + " want "
                + Arrays.toString(c[1])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
