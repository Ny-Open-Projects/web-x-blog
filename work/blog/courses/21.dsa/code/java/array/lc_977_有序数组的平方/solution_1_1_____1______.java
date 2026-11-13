// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc977_solution111 { // 定义类型
  public int[] sortedSquares(int[] nums) { // 定义函数/方法 sortedSquares
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int[] ans = new int[n]; // 把 new int[元素个数]; 写入 int[] ans
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      ans[i] = nums[i] * nums[i]; // 把 数组[下标 i] 乘 数组[下标 i]; 写入 ans[i]
    }
    Arrays.sort(ans); // 排序
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc977_solution111 s =
        new lc977_solution111(); // 把 new lc977_solution111(); 写入 lc977_solution111 s
    int[] r =
        s.sortedSquares(new int[] {1, 2, 3}); // 把 字符串.sortedSquares(new int[]{1, 2, 3}); 写入 int[] r
    if (!(r[0] == 1 && r[1] == 4 && r[2] == 9)) throw new RuntimeException("FAILED");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
