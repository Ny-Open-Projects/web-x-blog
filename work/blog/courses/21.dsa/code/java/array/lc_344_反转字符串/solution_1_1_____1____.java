// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116781
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型

  static void reverseString(String[] s) { // 定义函数/方法 reverseString
    int left = 0, right = s.length - 1; // 把 0, 右边界 赋值为 字符串.长度 减 1 存入 左边界
    while (left <= right) { // 循环，直到不满足「左边界 不超过 右边界」
      String tmp = s[left]; // 把 字符串[左边界] 存入 临时变量
      s[left] = s[right]; // 把 字符串[右边界]; 写入 s[left]
      s[right] = tmp; // 把 临时变量; 写入 s[right]
      left++; // 左边界 加一
      right--; // 右边界 减一
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][][] cases = { // 把 { 写入 String[][][] cases
      {{"h", "e", "l", "l", "o"}, {"o", "l", "l", "e", "h"}},
      {{"H", "a", "n", "n", "a", "h"}, {"h", "a", "n", "n", "a", "H"}},
    };
    for (int k = 0; k < cases.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 cases.长度 就继续
      String[] input = cases[k][0]; // 把 cases[下标 k][0]; 写入 String[] input
      String[] expected = cases[k][1]; // 把 cases[下标 k][1]; 写入 String[] expected
      reverseString(input); // reverseString(input);
      if (!java.util.Arrays.equals(
          input, expected)) { // 若 取反 java.util.Arrays.equals(input, expected
        System.out.println("FAIL at case " + k); // 打印输出
        throw new RuntimeException(
            "self-check failed"); // throw new RuntimeException(「self 减 check failed」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
