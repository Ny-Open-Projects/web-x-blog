package com.webfault.dsa; // 引入依赖

// LeetCode 58. 最后一个单词的长度。
// 忠实翻译 Python 参考实现 ref_lengthOfLastWord：len(s.split()[-1]) if s.split() else 0
class lc58_solution1 { // 定义类型
  int lengthOfLastWord(String s) { // 定义函数/方法 lengthOfLastWord
    int end = s.length() - 1; // 把 字符串.长度() 减 1 存入 终点
    while (end >= 0 && s.charAt(end) == ' ') { // 循环，直到不满足「终点 不低于 0 且 字符串 取字符 终点) 等于 ' '」
      end--; // 终点 减一
    }
    if (end < 0) { // 若 终点 小于 0
      return 0; // 返回 0
    }
    int start = end; // 把 终点 存入 起点
    while (start >= 0 && s.charAt(start) != ' ') { // 循环，直到不满足「起点 不低于 0 且 字符串 取字符 起点) 不等于 ' '」
      start--; // 起点 减一
    }
    return end - start; // 返回 终点 减 起点
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 用例来自 _tools/correctness_check.py PROBLEMS["lc_58_最后一个单词的长度"]
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {"Hello World", 5},
      {"   fly me   to   the moon  ", 4},
      {"luffy is still joyboy", 6},
    };
    lc58_solution1 s = new lc58_solution1(); // 把 new lc58_solution1(); 写入 lc58_solution1 s
    boolean allOK = true; // 把 true; 写入 boolean allOK
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      int got = s.lengthOfLastWord((String) c[0]); // 把 字符串.lengthOfLastWord((String) 字符[0]) 存入 got
      int want = (Integer) c[1]; // 把 (Integer) 字符[1] 存入 want
      if (got != want) { // 若 got 不等于 want
        allOK = false; // 把 false; 写入 allOK
        System.out.println(
            "FAIL lengthOfLastWord(" + c[0] + ") = " + got + ", want " + want); // 打印输出
      }
    }
    if (!allOK) { // 若 取反 allOK
      throw new RuntimeException(
          "some cases FAILED"); // throw new RuntimeException(「some cases FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
