// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class BitS2 { // 定义类型
  static int[] sortByBits(int[] arr) { // 定义函数/方法 sortByBits
    int[] bit = new int[10001]; // 把 new int[10001]; 写入 int[] bit
    for (int i = 1; i < 10001; i++)
      bit[i] = bit[i >> 1] + (i & 1); // 让 下标 i 从 1 开始计数，下标 i 小于 10001 就继续
    Integer[] idx = new Integer[arr.length]; // 把 new Integer[数组.长度]; 写入 Integer[] idx
    for (int i = 0; i < arr.length; i++) idx[i] = i; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    Arrays.sort(
        idx,
        (a, b) -> { // 排序
          if (bit[arr[a]] != bit[arr[b]])
            return bit[arr[a]]
                - bit[arr[b]]; // 若 bit[数组[数组]] 不等于 bit[数组[b]]，直接返回 bit[数组[数组]] 减 bit[数组[b]]
          return arr[a] - arr[b]; // 返回 数组[数组] 减 数组[b]
        }); // });
    int[] result = new int[arr.length]; // 把 new int[数组.长度]; 写入 int[] result
    for (int i = 0; i < idx.length; i++)
      result[i] = arr[idx[i]]; // 让 下标 i 从 0 开始计数，下标 i 小于 idx.长度 就继续
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{1, 2, 3}, {1, 2, 3}},
      {{0, 2, 1, 4}, {0, 1, 2, 4}},
      {{0, 1, 2, 3, 4, 5, 6, 7, 8}, {0, 1, 2, 4, 8, 3, 5, 6, 7}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got = BitS2.sortByBits(c[0].clone()); // 把 BitS2.sortByBits(字符[0].clone()); 写入 int[] got
      if (!Arrays.equals(got, c[1])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(c[0]) + " -> " + Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
