// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc110240695_solution55 { // 定义类型
  // 二路归并排序
  static int[] mergeSort(int[] arr) { // 定义函数/方法 mergeSort
    if (arr.length <= 1) return arr.clone(); // 若 数组.长度 不超过 1，直接返回 数组.clone()
    int mid = arr.length / 2; // 把 数组.长度 除以 2 存入 中点
    int[] left =
        mergeSort(
            Arrays.copyOfRange(
                arr, 0, mid)); // 把 mergeSort(Arrays.copyOfRange(数组, 0, 中点)); 写入 int[] left
    int[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));
    return merge(left, right); // 返回 merge(左边界, 右边界)
  }

  static int[] merge(int[] left, int[] right) { // 定义函数/方法 merge
    int[] res = new int[left.length + right.length]; // 把 new int[左边界.长度 加 右边界.长度]; 写入 int[] res
    int i = 0, j = 0, k = 0; // 把 0, 下标 j 赋值为 0, 下标 k 赋值为 0 存入 下标 i
    while (i < left.length && j < right.length) { // 循环，直到不满足「下标 i 小于 左边界.长度 且 下标 j 小于 右边界.长度」
      if (left[i] < right[j])
        res[k++] = left[i++]; // 若 左边界[下标 i] 小于 右边界[下标 j]) 结果[下标 k 加一 ] 赋值为 左边界[下标 i 加一 ];
      else res[k++] = right[j++]; // 否则
    }
    while (i < left.length)
      res[k++] = left[i++]; // 循环，直到不满足「下标 i 小于 左边界.长度) 结果[下标 k 加一 ] 赋值为 左边界[下标 i 加一 ];」
    while (j < right.length)
      res[k++] = right[j++]; // 循环，直到不满足「下标 j 小于 右边界.长度) 结果[下标 k 加一 ] 赋值为 右边界[下标 j 加一 ];」
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] r =
        mergeSort(new int[] {3, 1, 4, 1, 5}); // 把 mergeSort(new int[]{3, 1, 4, 1, 5}); 写入 int[] r
    int[] expect = {1, 1, 3, 4, 5}; // 把 {1, 1, 3, 4, 5}; 写入 int[] expect
    if (!Arrays.equals(r, expect)) { // 若 取反 Arrays.equals(右指针, expect
      System.out.println("FAIL " + Arrays.toString(r)); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
