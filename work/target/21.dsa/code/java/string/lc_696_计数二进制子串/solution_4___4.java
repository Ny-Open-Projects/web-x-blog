// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
package com.webfault.dsa; // 引入依赖

/**
 * LeetCode 696. 计数二进制子串 忠实翻译自 python/string/lc_696_计数二进制子串/solution_4___4.py prev/curr
 * 线性扫描：遇到字符切换时累加 min(prev, curr)
 */
class Main { // 定义类型
  static int countBinarySubstrings2(String s) { // 定义函数/方法 countBinarySubstrings2
    int prev = 0, curr = 1; // 把 0, 当前值 赋值为 1 存入 前一个
    int res = 0; // 把 0 存入 结果
    for (int i = 1; i < s.length(); i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 字符串.长度() 就继续
      if (s.charAt(i) != s.charAt(i - 1)) { // 若 字符串 取字符 下标 i) 不等于 字符串 取字符 下标 i 减 1
        res += Math.min(prev, curr); // 结果累加 Math.取较小值 前一个, 当前值)
        prev = curr; // 把 当前值; 写入 前一个
        curr = 1; // 把 1; 写入 当前值
      } else { // 否则
        curr++; // 当前值 加一
      }
    }
    return res + Math.min(prev, curr); // 返回 结果 加 Math.取较小值 前一个, 当前值)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[] inputs = {"00110011", "10101", "abc", "", "0", "000111", "00110", "111000", "10"};
    int[] wants = {6, 4, 2, 0, 0, 3, 3, 3, 1}; // 把 {6, 4, 2, 0, 0, 3, 3, 3, 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < inputs.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 inputs.长度 就继续
      int got = countBinarySubstrings2(inputs[ci]); // 把 countBinarySubstrings2(inputs[ci]) 存入 got
      if (got != wants[ci]) { // 若 got 不等于 wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL countBinarySubstrings2("
                + inputs[ci]
                + ")="
                + got
                + " want "
                + wants[ci]); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
