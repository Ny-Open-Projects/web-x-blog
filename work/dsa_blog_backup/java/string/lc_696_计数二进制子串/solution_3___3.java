// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

/**
 * LeetCode 696. 计数二进制子串 忠实翻译自 python/string/lc_696_计数二进制子串/solution_3___3.py
 * 计数分组法：顺序统计每组长度，累加相邻组较小值
 */
class Main { // 定义类型
  static int countBinarySubstrings(String s) { // 定义函数/方法 countBinarySubstrings
    List<Integer> groups = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> groups
    int count = 1; // 把 1 存入 计数
    for (int i = 1; i < s.length(); i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 字符串.长度() 就继续
      if (s.charAt(i) == s.charAt(i - 1)) { // 若 字符串 取字符 下标 i) 等于 字符串 取字符 下标 i 减 1
        count++; // 计数 加一
      } else { // 否则
        groups.add(count); // groups 追加 计数);
        count = 1; // 把 1; 写入 计数
      }
    }
    groups.add(count); // groups 追加 计数);
    int sum = 0; // 把 0 存入 累计和
    for (int i = 0; i < groups.size() - 1; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 groups.大小() 减 1 就继续
      sum +=
          Math.min(
              groups.get(i),
              groups.get(i + 1)); // 累计和累加 Math.取较小值 groups 查找 下标 i), groups 查找 下标 i 加 1))
    }
    return sum; // 返回 累计和
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
