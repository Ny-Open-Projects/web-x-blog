// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc134053461_solution11 { // 定义类型
  // 侏儒排序
  static int[] gnomeSort(int[] arr) { // 定义函数/方法 gnomeSort
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
    return arr; // 返回 数组
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] r =
        gnomeSort(new int[] {5, 4, 3, 2, 1}); // 把 gnomeSort(new int[]{5, 4, 3, 2, 1}); 写入 int[] r
    int[] expect = {1, 2, 3, 4, 5}; // 把 {1, 2, 3, 4, 5}; 写入 int[] expect
    if (!Arrays.equals(r, expect)) { // 若 取反 Arrays.equals(右指针, expect
      System.out.println("FAIL " + Arrays.toString(r)); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
