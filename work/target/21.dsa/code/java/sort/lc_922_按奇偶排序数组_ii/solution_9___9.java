// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class ParityS9 { // 定义类型
  static int[] sortArrayByParityII(int[] nums) { // 定义函数/方法 sortArrayByParityII
    int[] res = new int[nums.length]; // 把 new int[数组.长度]; 写入 int[] res
    int e = 0, o = 1; // 把 0, o 赋值为 1 存入 e
    for (int x : nums) { // for (int x : 数组) {
      if (x % 2 == 0) {
        res[e] = x;
        e += 2;
      } // 若 x 对…取模 2 等于 0) { 结果[e] 赋值为 x; e 累加 2; }
      else {
        res[o] = x;
        o += 2;
      } // 否则
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{4, 2, 5, 7}, {4, 5, 2, 7}},
      {{2, 3}, {2, 3}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[][] c : cases) { // for (int[][] 字符 : cases) {
      int[] got =
          ParityS9.sortArrayByParityII(
              c[0].clone()); // 把 ParityS9.sortArrayByParityII(字符[0].clone()); 写入 int[] got
      if (!Arrays.equals(got, c[1])) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(c[0]) + " -> " + Arrays.toString(got));
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
