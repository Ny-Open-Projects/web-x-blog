// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ParityS2 { // 定义类型
  static int[] sortArrayByParityII(int[] nums) { // 定义函数/方法 sortArrayByParityII
    int[] ans = new int[nums.length]; // 把 new int[数组.长度]; 写入 int[] ans
    int i = 0, j = 1; // 把 0, 下标 j 赋值为 1 存入 下标 i
    for (int x : nums) { // for (int x : 数组) {
      if ((x & 1) == 0) {
        ans[i] = x;
        i += 2;
      } // 若 (x 按位与 1) 等于 0) { 答案[下标 i] 赋值为 x; 下标 i 累加 2; }
      else {
        ans[j] = x;
        j += 2;
      } // 否则
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{4, 2, 5, 7}, {4, 5, 2, 7}},
      {{2, 3}, {2, 3}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got =
          ParityS2.sortArrayByParityII(
              c[0].clone()); // 把 ParityS2.sortArrayByParityII(字符[0].clone()); 写入 int[] got
      if (!Arrays.equals(got, c[1])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(c[0]) + " -> " + Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
