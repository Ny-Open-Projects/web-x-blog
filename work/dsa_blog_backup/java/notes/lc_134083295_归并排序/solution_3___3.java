// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

/**
 * 归并排序 忠实翻译自 python/notes/lc_134083295_归并排序/solution_3___3.py 运行即自检：失败抛 RuntimeException（非 0
 * 退出），通过打印 PASS
 */
class Main { // 定义类型

  static void mergeSort(int[] nums) { // 定义函数/方法 mergeSort
    int[] ordered = msFn(nums); // 把 msFn(数组); 写入 int[] ordered
    System.arraycopy(
        ordered, 0, nums, 0, nums.length); // System.arraycopy(ordered, 0, 数组, 0, 数组.长度);
  }

  static int[] msFn(int[] arr) { // 定义函数/方法 msFn
    if (arr.length < 2) { // 若 数组.长度 小于 2
      return arr; // 返回 数组
    }
    int mid = arr.length / 2; // 把 数组.长度 除以 2 存入 中点
    int[] left = Arrays.copyOfRange(arr, 0, mid); // 把 Arrays.copyOfRange(数组, 0, 中点); 写入 int[] left
    int[] right =
        Arrays.copyOfRange(
            arr, mid, arr.length); // 把 Arrays.copyOfRange(数组, 中点, 数组.长度); 写入 int[] right
    int[] orderedLeft = msFn(left); // 把 msFn(左边界); 写入 int[] orderedLeft
    int[] orderedRight = msFn(right); // 把 msFn(右边界); 写入 int[] orderedRight
    int[] res =
        new int
            [orderedLeft.length
                + orderedRight.length]; // 把 new int[orderedLeft.长度 加 orderedRight.长度]; 写入 int[] res
    int a = 0, b = 0, k = 0; // 把 0, b 赋值为 0, 下标 k 赋值为 0 存入 数组
    while (a < orderedLeft.length
        && b < orderedRight.length) { // 循环，直到不满足「数组 小于 orderedLeft.长度 且 b 小于 orderedRight.长度」
      if (orderedLeft[a] <= orderedRight[b]) { // 若 orderedLeft[数组] 不超过 orderedRight[b]
        res[k++] = orderedLeft[a++]; // 把 orderedLeft[数组 加一 ]; 写入 res[k++]
      } else { // 否则
        res[k++] = orderedRight[b++]; // 把 orderedRight[b 加一 ]; 写入 res[k++]
      }
    }
    while (a < orderedLeft.length) { // 循环，直到不满足「数组 小于 orderedLeft.长度」
      res[k++] = orderedLeft[a++]; // 把 orderedLeft[数组 加一 ]; 写入 res[k++]
    }
    while (b < orderedRight.length) { // 循环，直到不满足「b 小于 orderedRight.长度」
      res[k++] = orderedRight[b++]; // 把 orderedRight[b 加一 ]; 写入 res[k++]
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] inputs = { // 把 { 写入 int[][] inputs
      {5, 4, 3, 2, 1},
      {},
      {1},
      {3, 1, 2, 1, 3},
      {-3, 0, 5, -10, 8},
      {2, 2, 2},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3, 4, 5},
      {},
      {1},
      {1, 1, 2, 3, 3},
      {-10, -3, 0, 5, 8},
      {2, 2, 2},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < inputs.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 inputs.长度 就继续
      int[] nums = inputs[ci].clone(); // 把 inputs[ci].clone(); 写入 int[] nums
      mergeSort(nums); // mergeSort(数组);
      if (!Arrays.equals(nums, wants[ci])) { // 若 取反 Arrays.equals(数组, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL mergeSort("
                + Arrays.toString(inputs[ci])
                + ")="
                + Arrays.toString(nums) // 打印输出
                + " want "
                + Arrays.toString(wants[ci])); // 加 「 want 」 加 Arrays.toString(wants[ci]));
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
