// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

/**
 * LeetCode 696. 计数二进制子串 忠实翻译自 python/string/lc_696_计数二进制子串/solution_10___10.py
 * 分组法：先按连续相同字符分组，再累加相邻组长度的较小值
 */
class Main { // 定义类型
  static int countBinarySubstrings(String s) { // 定义函数/方法 countBinarySubstrings
    List<Integer> groups = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> groups
    int i = 0, n = s.length(); // 把 0, 元素个数 赋值为 字符串.长度() 存入 下标 i
    while (i < n) { // 循环，直到不满足「下标 i 小于 元素个数」
      char ch = s.charAt(i); // 逐字符处理
      int cnt = 0; // 把 0 存入 计数
      while (i < n && s.charAt(i) == ch) { // 循环，直到不满足「下标 i 小于 元素个数 且 字符串 取字符 下标 i) 等于 字符」
        cnt++; // 计数 加一
        i++; // 下标 i 加一
      }
      groups.add(cnt); // groups 追加 计数);
    }
    int ans = 0; // 把 0 存入 答案
    for (int j = 1; j < groups.size(); j++) { // 让 下标 j 从 1 开始计数，下标 j 小于 groups.大小() 就继续
      ans +=
          Math.min(
              groups.get(j - 1),
              groups.get(j)); // 答案累加 Math.取较小值 groups 查找 下标 j 减 1), groups 查找 下标 j))
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[] inputs = {"00110011", "10101", "abc", "", "0", "000111", "00110", "111000", "10"};
    int[] wants = {6, 4, 2, 0, 0, 3, 3, 3, 1}; // 把 {6, 4, 2, 0, 0, 3, 3, 3, 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < inputs.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 inputs.长度 就继续
      int got = countBinarySubstrings(inputs[ci]); // 把 countBinarySubstrings(inputs[ci]) 存入 got
      if (got != wants[ci]) { // 若 got 不等于 wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL countBinarySubstrings(" + inputs[ci] + ")=" + got + " want " + wants[ci]); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
