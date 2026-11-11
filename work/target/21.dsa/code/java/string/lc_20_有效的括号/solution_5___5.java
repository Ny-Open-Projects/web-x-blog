// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public boolean isValid(String s) { // 定义判定函数 isValid
    while (s.contains("()")
        || s.contains("{}")
        || s.contains("[]")) { // 循环，直到不满足「字符串 是否包含 「()」) 或 字符串 是否包含 「()」) 或 字符串 是否包含 「()」」
      s = s.replace("()", "").replace("{}", "").replace("[]", "");
    }
    return s.isEmpty(); // 返回 字符串.isEmpty()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[] inputs = {"abc"}; // 把 {「abc」}; 写入 String[] inputs
    boolean[] wants = {false}; // 把 {false}; 写入 boolean[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < inputs.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 inputs.长度 就继续
      boolean got = s.isValid(inputs[i]); // 把 字符串.isValid(inputs[下标 i]); 写入 boolean got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL isValid(" + inputs[i] + ")=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
