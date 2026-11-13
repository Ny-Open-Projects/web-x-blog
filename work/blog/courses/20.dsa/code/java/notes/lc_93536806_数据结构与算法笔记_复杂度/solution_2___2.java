// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static int binarySearch(int[] arr, int target) { // 定义函数/方法 binarySearch
    int left = 0, right = arr.length - 1; // 把 0, 右边界 赋值为 数组.长度 减 1 存入 左边界
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      int mid = left + (right - left) / 2; // 把 (左边界 加 右边界) 除以 2 存入 中点
      if (arr[mid] == target) return mid; // 若 数组[中点] 等于 目标值，直接返回 中点
      else if (arr[mid] < target) left = mid + 1; // 否则，若 数组[中点] 小于 目标值) 左边界 赋值为 中点 加 1;
      else right = mid - 1; // 否则
    }
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args){
    int[] arr = {1, 3, 5, 7, 9}; // 把 {1,3,5,7,9}; 写入 int[] arr
    if (!(binarySearch(arr, 5) == 2
        && binarySearch(arr, 4)
            == -1)) { // 若 取反 (binarySearch(数组,5) 等于 2 且 binarySearch(数组,4) 等于 减 1
      System.out.println("FAIL");
      throw new RuntimeException("FAILED"); // 打印输出
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
