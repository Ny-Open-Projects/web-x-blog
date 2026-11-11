// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public int myAtoi(String s) { // 定义函数/方法 myAtoi
    s = s.trim(); // 把 字符串.trim(); 写入 字符串
    if (s.isEmpty()) return 0; // 若 字符串.isEmpty()，直接返回 0
    int i = 0, sign = 1; // 把 0, sign 赋值为 1 存入 下标 i
    if (s.charAt(0) == '+') i++; // 若 字符串 取字符 0) 等于 ' 加 ') 下标 i 加一 ;
    else if (s.charAt(0) == '-') {
      sign = -1;
      i++;
    } // 否则，若 字符串 取字符 0) 等于 ' 减 ') { sign 赋值为 减 1; 下标 i 加一 ; }
    int res = 0; // 把 0 存入 结果
    int INT_MAX = Integer.MAX_VALUE; // 把 Integer.MAX_VALUE 存入 INT_MAX
    while (i < s.length()
        && Character.isDigit(
            s.charAt(i))) { // 循环，直到不满足「下标 i 小于 字符串.长度() 且 Character.isDigit(字符串 取字符 下标 i」
      int digit = s.charAt(i) - '0'; // 把 字符串 取字符 下标 i) 减 '0' 存入 digit
      if (res > INT_MAX / 10
          || (res == INT_MAX / 10
              && digit > 7)) { // 若 结果 超过 INT_MAX 除以 10 或 (结果 等于 INT_MAX 除以 10 且 digit 超过 7
        return sign == 1
            ? INT_MAX
            : Integer.MIN_VALUE; // 返回 sign 等于 1 ? INT_MAX : Integer.MIN_VALUE
      }
      res = res * 10 + digit; // 把 结果 乘 10 加 digit; 写入 结果
      i++; // 下标 i 加一
    }
    return sign * res; // 返回 sign 乘 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Solution s = new Solution(); // 把 new Solution(); 写入 Solution s
    String[] ins = {
      "   -42", "4193 with words", "words and 987", "-91283472332"
    }; // 把 {「 减 42」, 「 减 42」, 「 减 42」, 「 减 42」}; 写入 String[] ins
    int[] wants = {-42, 4193, 0, -2147483648}; // 把 { 减 42, 4193, 0, 减 2147483648}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      int got = s.myAtoi(ins[i]); // 把 字符串.myAtoi(ins[下标 i]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL " + ins[i] + "=" + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
