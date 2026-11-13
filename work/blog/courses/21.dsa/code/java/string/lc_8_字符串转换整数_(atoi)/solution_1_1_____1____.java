// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

class Solution { // 定义类型
  public int myAtoi(String str) { // 定义函数/方法 myAtoi
    class Automaton { // 定义类型
      String state = "start"; // 把 「起点」 存入 state
      int sign = 1; // 把 1 存入 sign
      long ans = 0; // 把 0; 写入 long ans
      String[][] table = { // 把 { 写入 String[][] table
        {"start", "signed", "in_number", "end"},
        {"end", "end", "in_number", "end"},
        {"end", "end", "in_number", "end"},
        {"end", "end", "end", "end"} // {「终点」,「终点」,「终点」,「终点」}
      };

      int getCol(char c) { // 定义函数/方法 getCol
        if (c == ' ') return 0; // 若 字符 等于 ' '，直接返回 0
        if (c == '+' || c == '-') return 1; // 若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '，直接返回 1
        if (Character.isDigit(c)) return 2; // 若 Character.isDigit(字符)，直接返回 2
        return 3; // 返回 3
      }

      int idx(String st) { // 定义函数/方法 idx
        if (st.equals("start")) return 0; // 若 st.equals(「起点」)，直接返回 0
        if (st.equals("signed")) return 1; // 若 st.equals(「signed」)，直接返回 1
        if (st.equals("in_number")) return 2; // 若 st.equals(「in_number」)，直接返回 2
        return 3; // 返回 3
      }

      void get(char c) { // 定义函数/方法 get
        state = table[idx(state)][getCol(c)]; // 把 table[idx(state)][getCol(字符)]; 写入 state
        if (state.equals("in_number")) { // 若 state.equals(「in_number」
          ans = ans * 10 + (c - '0'); // 把 答案 乘 10 加 (字符 减 '0'); 写入 答案
          if (sign == 1)
            ans = Math.min(ans, 2147483647L); // 若 sign 等于 1) 答案 赋值为 Math.取较小值 答案, 2147483647L);
          else ans = Math.min(ans, 2147483648L); // 否则
        } else if (state.equals("signed")) { // 否则，若 state.equals(「signed」
          sign = (c == '+') ? 1 : -1; // 把 (字符 等于 ' 加 ') ? 1 : 减 1; 写入 sign
        }
      }
    }
    Automaton a = new Automaton(); // 把 new Automaton(); 写入 Automaton a
    for (int i = 0; i < str.length(); i++)
      a.get(str.charAt(i)); // 让 下标 i 从 0 开始计数，下标 i 小于 str.长度() 就继续
    return (int) (a.sign * a.ans); // 返回 (int)(数组.sign 乘 数组.答案)
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
