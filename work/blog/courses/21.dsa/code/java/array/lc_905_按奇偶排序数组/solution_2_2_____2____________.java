// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145588341
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc905_solution222 { // 定义类型
  public int[] sortArrayByParity(int[] nums) { // 定义函数/方法 sortArrayByParity
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int[] res = new int[n]; // 把 new int[元素个数]; 写入 int[] res
    int left = 0, right = n - 1; // 把 0, 右边界 赋值为 元素个数 减 1 存入 左边界
    for (int num : nums) { // for (int num : 数组) {
      if (num % 2 == 0) { // 若 num 对…取模 2 等于 0
        res[left++] = num; // 把 num; 写入 res[left++]
      } else { // 否则
        res[right--] = num; // 把 num; 写入 res[right--]
      }
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc905_solution222 s =
        new lc905_solution222(); // 把 new lc905_solution222(); 写入 lc905_solution222 s
    int[] r =
        s.sortArrayByParity(
            new int[] {1, 2, 3}); // 把 字符串.sortArrayByParity(new int[]{1, 2, 3}); 写入 int[] r
    if (!(r[0] == 2 && r[1] == 3 && r[2] == 1)) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
