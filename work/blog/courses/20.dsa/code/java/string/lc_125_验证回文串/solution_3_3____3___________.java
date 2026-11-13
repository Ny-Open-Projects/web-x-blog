// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114949
package com.webfault.dsa; // 引入依赖

// LeetCode 125. 验证回文串（原字符串上直接判断）
// 忠实翻译 Python 参考实现：t = [c.lower() for c in s if c.isalnum()]; t == t[::-1]
class lc125_solution333 { // 定义类型
  boolean isPalindrome(String s) { // 定义判定函数 isPalindrome
    int left = 0; // 把 0 存入 左边界
    int right = s.length() - 1; // 把 字符串.长度() 减 1 存入 右边界
    while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
      if (!Character.isLetterOrDigit(
          s.charAt(left))) { // 若 取反 Character.isLetterOrDigit(字符串 取字符 左边界
        left++; // 左边界 加一
      } else if (!Character.isLetterOrDigit(
          s.charAt(right))) { // 否则，若 取反 Character.isLetterOrDigit(字符串 取字符 右边界
        right--; // 右边界 减一
      } else if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
        return false; // 返回 false
      } else { // 否则
        left++; // 左边界 加一
        right--; // 右边界 减一
      }
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 用例来自 _tools/correctness_check.py PROBLEMS["lc_125_验证回文串"]
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {"A man, a plan, a canal: Panama", true},
      {"race a car", false},
      {" ", true},
    };
    lc125_solution333 s =
        new lc125_solution333(); // 把 new lc125_solution333(); 写入 lc125_solution333 s
    boolean allOK = true; // 把 true; 写入 boolean allOK
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      boolean got =
          s.isPalindrome((String) c[0]); // 把 字符串.isPalindrome((String) 字符[0]); 写入 boolean got
      boolean want = (Boolean) c[1]; // 把 (Boolean) 字符[1]; 写入 boolean want
      if (got != want) { // 若 got 不等于 want
        allOK = false; // 把 false; 写入 allOK
        System.out.println("FAIL isPalindrome(" + c[0] + ") = " + got + ", want " + want); // 打印输出
      }
    }
    if (!allOK) { // 若 取反 allOK
      throw new RuntimeException(
          "some cases FAILED"); // throw new RuntimeException(「some cases FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
