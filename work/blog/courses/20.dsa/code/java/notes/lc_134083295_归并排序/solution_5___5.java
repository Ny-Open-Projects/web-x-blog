// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

/**
 * 归并排序 忠实翻译自 python/notes/lc_134083295_归并排序/solution_5___5.py 运行即自检：失败抛 RuntimeException（非 0
 * 退出），通过打印 PASS
 */
class Main { // 定义类型

  static int[] mergeSort(int[] nums) { // 定义函数/方法 mergeSort
    if (nums.length <= 1) { // 若 数组.长度 不超过 1
      return nums; // 返回 数组
    }
    int mid = nums.length / 2; // 把 数组.长度 除以 2 存入 中点
    int[] left =
        mergeSort(
            Arrays.copyOfRange(
                nums, 0, mid)); // 把 mergeSort(Arrays.copyOfRange(数组, 0, 中点)); 写入 int[] left
    int[] right = mergeSort(Arrays.copyOfRange(nums, mid, nums.length));
    return merge(left, right); // 返回 merge(左边界, 右边界)
  }

  static int[] merge(int[] left, int[] right) { // 定义函数/方法 merge
    int[] result =
        new int[left.length + right.length]; // 把 new int[左边界.长度 加 右边界.长度]; 写入 int[] result
    int i = 0, j = 0, k = 0; // 把 0, 下标 j 赋值为 0, 下标 k 赋值为 0 存入 下标 i
    while (i < left.length && j < right.length) { // 循环，直到不满足「下标 i 小于 左边界.长度 且 下标 j 小于 右边界.长度」
      if (left[i] <= right[j]) { // 若 左边界[下标 i] 不超过 右边界[下标 j]
        result[k++] = left[i++]; // 把 左边界[下标 i 加一 ]; 写入 result[k++]
      } else { // 否则
        result[k++] = right[j++]; // 把 右边界[下标 j 加一 ]; 写入 result[k++]
      }
    }
    while (i < left.length) { // 循环，直到不满足「下标 i 小于 左边界.长度」
      result[k++] = left[i++]; // 把 左边界[下标 i 加一 ]; 写入 result[k++]
    }
    while (j < right.length) { // 循环，直到不满足「下标 j 小于 右边界.长度」
      result[k++] = right[j++]; // 把 右边界[下标 j 加一 ]; 写入 result[k++]
    }
    return result; // 返回 结果
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
      int[] got = mergeSort(inputs[ci]); // 把 mergeSort(inputs[ci]); 写入 int[] got
      if (!Arrays.equals(got, wants[ci])) { // 若 取反 Arrays.equals(got, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL mergeSort("
                + Arrays.toString(inputs[ci])
                + ")="
                + Arrays.toString(got) // 打印输出
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
