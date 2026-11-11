// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374488
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public boolean areNumbersAscending(String s) { // 定义函数/方法 areNumbersAscending
    String[] words = s.split(" "); // 把 字符串.split(「 」); 写入 String[] words
    int prev = 0; // 把 0 存入 前一个
    for (String word : words) { // for (String 单词 : 单词列表) {
      if (Character.isDigit(word.charAt(0))) { // 若 Character.isDigit(单词 取字符 0
        int num = Integer.parseInt(word); // 把 Integer.转整数(单词) 存入 num
        if (num <= prev) return false; // 若 num 不超过 前一个，直接返回 false
        prev = num; // 把 num; 写入 前一个
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[] ins = {"abc", "a 1 b 2 c 3", "3 box 1"}; // 把 {「abc」, 「abc」, 「abc」}; 写入 String[] ins
    boolean[] wants = {true, true, false}; // 把 {true, true, false}; 写入 boolean[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      boolean got =
          s.areNumbersAscending(ins[i]); // 把 字符串.areNumbersAscending(ins[下标 i]); 写入 boolean got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL " + ins[i] + "=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
