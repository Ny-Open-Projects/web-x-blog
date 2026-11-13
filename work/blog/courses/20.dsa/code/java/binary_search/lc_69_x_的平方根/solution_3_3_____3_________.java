// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233215
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc69_solution333 { // 定义类型
  // x 的平方根：二分查找（(long)mid*mid 判溢出）
  // 忠实于 Python ref_mySqrt 的二分思想
  public int mySqrt(int x) { // 定义函数/方法 mySqrt
    int left = 0; // 把 0 存入 左边界
    int right = x; // 把 x 存入 右边界
    int ans = -1; // 把 减 1 存入 答案
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      int mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
      if ((long) mid * mid <= x) { // 若 (long) 中点 乘 中点 不超过 x
        ans = mid; // 把 中点; 写入 答案
        left = mid + 1; // 把 中点 加 1; 写入 左边界
      } else { // 否则
        right = mid - 1; // 把 中点 减 1; 写入 右边界
      }
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc69_solution333 s = new lc69_solution333(); // 把 new lc69_solution333(); 写入 lc69_solution333 s
    int[][] cases = {{4, 2}, {8, 2}, {16, 4}, {2147395599, 46339}};
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      int got = s.mySqrt(c[0]); // 把 字符串.mySqrt(字符[0]) 存入 got
      if (got != c[1]) { // 若 got 不等于 字符[1]
        System.out.println("FAIL: mySqrt(" + c[0] + ")=" + got + " want " + c[1]); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
