// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc905_solution111 { // 定义类型
  public int[] sortArrayByParity(int[] nums) { // 定义函数/方法 sortArrayByParity
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int index = 0; // 把 0 存入 index
    int[] res = new int[n]; // 把 new int[元素个数]; 写入 int[] res
    for (int num : nums) { // for (int num : 数组) {
      if (num % 2 == 0) { // 若 num 对…取模 2 等于 0
        res[index++] = num; // 把 num; 写入 res[index++]
      }
    }
    for (int num : nums) { // for (int num : 数组) {
      if (num % 2 == 1) { // 若 num 对…取模 2 等于 1
        res[index++] = num; // 把 num; 写入 res[index++]
      }
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc905_solution111 s =
        new lc905_solution111(); // 把 new lc905_solution111(); 写入 lc905_solution111 s
    int[] r =
        s.sortArrayByParity(
            new int[] {1, 2, 3}); // 把 字符串.sortArrayByParity(new int[]{1, 2, 3}); 写入 int[] r
    if (!(r[0] == 2 && r[1] == 1 && r[2] == 3)) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
