// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class RadixS3 { // 定义类型
  static void radixSort(int[] arr) { // 定义函数/方法 radixSort
    if (arr.length < 2) return; // 若 数组.长度 小于 2) return;
    int maxVal = arr[0], minVal = arr[0]; // 把 数组[0], minVal 赋值为 数组[0] 存入 maxVal
    for (int x : arr) {
      if (x > maxVal) maxVal = x;
      if (x < minVal) minVal = x;
    }
    int offset = minVal < 0 ? -minVal : 0; // 把 minVal 小于 0 ? 减 minVal : 0 存入 offset
    int[] adjusted = new int[arr.length]; // 把 new int[数组.长度]; 写入 int[] adjusted
    for (int i = 0; i < arr.length; i++)
      adjusted[i] = arr[i] + offset; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    int maxAdj = adjusted[0]; // 把 adjusted[0] 存入 maxAdj
    for (int x : adjusted)
      if (x > maxAdj) maxAdj = x; // 把 x; 写入 for (int x : adjusted) if (x > maxAdj) maxAdj
    int radix = 1; // 把 1 存入 radix
    int[] tmp = new int[arr.length]; // 把 new int[数组.长度]; 写入 int[] tmp
    while (maxAdj >= radix) { // 循环，直到不满足「maxAdj 不低于 radix」
      int[] bucket = new int[10]; // 把 new int[10]; 写入 int[] bucket
      for (int num : adjusted)
        bucket[
            (num / radix) % 10]++; // for (int num : adjusted) bucket[(num 除以 radix) 对…取模 10] 加一 ;
      for (int i = 1; i < 10; i++) bucket[i] += bucket[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 10 就继续
      for (int i = arr.length - 1; i >= 0; i--) { // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 不低于 0 就继续
        int d = (adjusted[i] / radix) % 10; // 把 (adjusted[下标 i] 除以 radix) 对…取模 10 存入 d
        tmp[bucket[d] - 1] = adjusted[i]; // 把 adjusted[下标 i]; 写入 tmp[bucket[d] - 1]
        bucket[d]--; // bucket[d] 减一 ;
      }
      for (int i = 0; i < arr.length; i++)
        adjusted[i] = tmp[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      radix *= 10; // 把 10; 写入 radix *
    }
    for (int i = 0; i < arr.length; i++)
      arr[i] = adjusted[i] - offset; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {
        {100, 34, 1002, 1234, 66, 137, 49, 102, 9, 108, 102, 101, 104, 109, 102},
        {9, 34, 49, 66, 100, 101, 102, 102, 102, 104, 108, 109, 137, 1002, 1234}
      },
      {{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
      {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}},
      {{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}, {1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9}},
      {{}, {}},
      {{1}, {1}},
      {
        {-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20},
        {-100, -30, -20, -9, -2, 0, 0, 1, 1, 1, 3, 3, 4, 5, 9, 9, 20, 88, 88, 99, 100}
      },
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] in = c[0].clone(); // 把 字符[0].clone(); 写入 int[] in
      RadixS3.radixSort(in); // RadixS3.radixSort(in);
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
