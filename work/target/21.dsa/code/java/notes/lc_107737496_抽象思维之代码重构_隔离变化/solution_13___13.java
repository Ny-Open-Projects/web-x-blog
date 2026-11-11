// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package com.webfault.dsa; // 引入依赖

// 忠实翻译 python solution_13：扫描 text，若任一位置匹配 regexp 则返回 true
class Main { // 定义类型

  static boolean matchHere(String regexp, String text) { // 定义函数/方法 matchHere
    if (regexp.length() == 0) { // 若 regexp.长度() 等于 0
      return true; // 返回 true
    }
    if (regexp.length() >= 2
        && regexp.charAt(1) == '*') { // 若 regexp.长度() 不低于 2 且 regexp 取字符 1) 等于 ' 乘 '
      return matchStar(
          regexp.charAt(0),
          regexp.substring(2),
          text); // 返回 matchStar(regexp 取字符 0), regexp 截取 2), text)
    }
    if (regexp.charAt(0) == '$'
        && regexp.length() == 1) { // 若 regexp 取字符 0) 等于 '$' 且 regexp.长度() 等于 1
      return text.length() == 0; // 返回 text.长度() 等于 0
    }
    if (text.length() > 0 && (regexp.charAt(0) == '.' || regexp.charAt(0) == text.charAt(0))) {
      return matchHere(
          regexp.substring(1), text.substring(1)); // 返回 matchHere(regexp 截取 1), text 截取 1))
    }
    return false; // 返回 false
  }

  static boolean matchStar(char c, String regexp, String text) { // 定义函数/方法 matchStar
    int i = 0; // 把 0 存入 下标 i
    while (true) { // 循环，直到不满足「true」
      if (matchHere(regexp, text.substring(i))) { // 若 matchHere(regexp, text 截取 下标 i
        return true; // 返回 true
      }
      if (i >= text.length()) { // 若 下标 i 不低于 text.长度(
        break; // 跳出循环
      }
      if (text.charAt(i) != c && c != '.') { // 若 text 取字符 下标 i) 不等于 字符 且 字符 不等于 '.'
        break; // 跳出循环
      }
      i++; // 下标 i 加一
    }
    return false; // 返回 false
  }

  static boolean match(String regexp, String text) { // 定义函数/方法 match
    if (regexp.length() > 0
        && regexp.charAt(0) == '^') { // 若 regexp.长度() 超过 0 且 regexp 取字符 0) 等于 ' 按位异或 '
      return matchHere(regexp.substring(1), text); // 返回 matchHere(regexp 截取 1), text)
    }
    int i = 0; // 把 0 存入 下标 i
    while (true) { // 循环，直到不满足「true」
      if (matchHere(regexp, text.substring(i))) { // 若 matchHere(regexp, text 截取 下标 i
        return true; // 返回 true
      }
      if (i >= text.length()) { // 若 下标 i 不低于 text.长度(
        break; // 跳出循环
      }
      i++; // 下标 i 加一
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][] cases = { // 把 { 写入 String[][] cases
      {"abc", "xxabcxx", "true"},
      {"a.c", "axc", "true"},
      {"a*", "aaaa", "true"},
      {"^a", "ba", "false"},
      {"c$", "abc", "true"},
      {"a.*c", "aXYZc", "true"},
      {"ab*c", "ac", "true"},
      {"ab", "ba", "false"},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < cases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
      boolean got =
          match(
              cases[i][0], cases[i][1]); // 把 match(cases[下标 i][0], cases[下标 i][1]); 写入 boolean got
      boolean want =
          Boolean.parseBoolean(
              cases[i][2]); // 把 Boolean.parseBoolean(cases[下标 i][2]); 写入 boolean want
      if (got != want) { // 若 got 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL match(\""
                + cases[i][0]
                + "\",\""
                + cases[i][1]
                + "\")="
                + got
                + " want "
                + want); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
