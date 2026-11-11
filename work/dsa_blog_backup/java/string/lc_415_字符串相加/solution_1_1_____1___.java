// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public String addStrings(String num1, String num2) { // 定义函数/方法 addStrings
    int i = num1.length() - 1,
        j = num2.length() - 1,
        carry = 0; // 把 num1.长度() 减 1, 下标 j 赋值为 num2.长度() 减 1, carry 赋值为 0 存入 下标 i
    StringBuilder result = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder result
    while (i >= 0 || j >= 0 || carry != 0) { // 循环，直到不满足「下标 i 不低于 0 或 下标 j 不低于 0 或 carry 不等于 0」
      int total = carry; // 把 carry 存入 总和
      if (i >= 0) {
        total += num1.charAt(i) - '0';
        i--;
      } // 若 下标 i 不低于 0) { 总和 累加 num1 取字符 下标 i) 减 '0'; 下标 i 减一 ; }
      if (j >= 0) {
        total += num2.charAt(j) - '0';
        j--;
      } // 若 下标 j 不低于 0) { 总和 累加 num2 取字符 下标 j) 减 '0'; 下标 j 减一 ; }
      result.append(total % 10); // 把 总和 对…取模 10 追加到列表尾部
      carry = total / 10; // 把 总和 除以 10; 写入 carry
    }
    return result.reverse().toString(); // 返回 结果.reverse().toString()
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[][] ins = {
      {"11", "123"}, {"99", "1"}, {"0", "0"}
    }; // 把 {{「11」,「11」},{「11」,「11」},{「11」,「11」}}; 写入 String[][] ins
    String[] wants = {"134", "100", "0"}; // 把 {「134」,「134」,「134」}; 写入 String[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      String got =
          s.addStrings(ins[i][0], ins[i][1]); // 把 字符串.addStrings(ins[下标 i][0], ins[下标 i][1]) 存入 got
      if (!got.equals(wants[i])) {
        ok = false;
        System.out.println("FAIL " + ins[i][0] + "," + ins[i][1] + "=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
