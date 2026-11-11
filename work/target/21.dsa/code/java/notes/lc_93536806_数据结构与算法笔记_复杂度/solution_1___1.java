// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static int linearSearch(int[] arr, int target) { // 定义函数/方法 linearSearch
    for (int i = 0; i < arr.length; i++)
      if (arr[i] == target) return i; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args){
    int[] arr = {3, 1, 4, 1, 5, 9, 2, 6}; // 把 {3,1,4,1,5,9,2,6}; 写入 int[] arr
    if (!(linearSearch(arr, 5) == 4
        && linearSearch(arr, 7)
            == -1)) { // 若 取反 (linearSearch(数组,5) 等于 4 且 linearSearch(数组,7) 等于 减 1
      System.out.println("FAIL");
      throw new RuntimeException("FAILED"); // 打印输出
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
