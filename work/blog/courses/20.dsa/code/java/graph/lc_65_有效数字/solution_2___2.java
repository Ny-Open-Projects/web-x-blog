// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc65_solution22 { // 定义类型
  public boolean isNumber(String s) { // 定义判定函数 isNumber
    String t = s.trim(); // 把 字符串.trim() 存入 另一字符串
    if (t.isEmpty()) return false; // 若 另一字符串.isEmpty()，直接返回 false
    boolean hasDot = false, hasE = false, hasDigit = false;
    for (int i = 0; i < t.length(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 另一字符串.长度() 就继续
      char c = t.charAt(i); // 逐字符处理
      if (c == '.') { // 若 字符 等于 '.'
        if (hasDot || hasE) return false; // 若 hasDot 或 hasE，直接返回 false
        hasDot = true; // 把 true; 写入 hasDot
      } else if (c == 'e' || c == 'E') { // 否则，若 字符 等于 'e' 或 字符 等于 'E'
        if (hasE || !hasDigit) return false; // 若 hasE 或 取反 hasDigit，直接返回 false
        hasE = true; // 把 true; 写入 hasE
        hasDigit = false; // 把 false; 写入 hasDigit
      } else if (c == '+' || c == '-') { // 否则，若 字符 等于 ' 加 ' 或 字符 等于 ' 减 '
        if (i > 0 && t.charAt(i - 1) != 'e' && t.charAt(i - 1) != 'E') return false;
      } else if (Character.isDigit(c)) { // 否则，若 Character.isDigit(字符
        hasDigit = true; // 把 true; 写入 hasDigit
      } else { // 否则
        return false; // 返回 false
      }
    }
    return hasDigit; // 返回 hasDigit
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc65_solution22 s = new lc65_solution22(); // 把 new lc65_solution22(); 写入 lc65_solution22 s
    String[] tests = {
      "0", "abc", "2.5", "1e10", ".", "e9", " ", "4e", "++1", "2.", "1.2.3", "+5", "46.e3", "1e",
      "-1.", "3e+2"
    };
    boolean[] wants = {
      true, false, true, true, false, false, false, false, false, true, false, true, true, false,
      true, true
    };
    for (int i = 0; i < tests.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 tests.长度 就继续
      if (s.isNumber(tests[i]) != wants[i]) { // 若 字符串.isNumber(tests[下标 i]) 不等于 wants[下标 i]
        System.out.println("FAIL isNumber(" + tests[i] + ") want " + wants[i]); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
