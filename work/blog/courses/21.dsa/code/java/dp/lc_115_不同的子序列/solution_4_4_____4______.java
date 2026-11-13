// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
package com.webfault.dsa; // 引入依赖

class lc115_solution444 { // 定义类型
  // numDistinct 忠实翻译 python ref solution_4_4_____4______.py（从前往后二维 DP）
  static long numDistinct(String s, String t) { // 定义函数/方法 numDistinct
    int sLen = s.length(), tLen = t.length(); // 把 字符串.长度(), tLen 赋值为 另一字符串.长度() 存入 sLen
    long[][] dp = new long[sLen + 1][tLen + 1]; // 把 new long[sLen 加 1][tLen 加 1]; 写入 long[][] dp
    for (int i = 0; i <= sLen; i++) { // 让 下标 i 从 0 开始计数，下标 i 不超过 sLen 就继续
      dp[i][0] = 1; // 把 1; 写入 dp[i][0]
    }
    for (int i = 1; i <= sLen; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 sLen 就继续
      for (int j = 1; j <= tLen; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 tLen 就继续
        if (s.charAt(i - 1) == t.charAt(j - 1)) { // 若 字符串 取字符 下标 i 减 1) 等于 另一字符串 取字符 下标 j 减 1
          dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
        } else { // 否则
          dp[i][j] = dp[i - 1][j]; // 把 DP 表[下标 i 减 1][下标 j]; 写入 dp[i][j]
        }
      }
    }
    return dp[sLen][tLen]; // 返回 DP 表[sLen][tLen]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][] cases = { // 把 { 写入 String[][] cases
      {"rabbbit", "rabbit", "3"},
      {"babgbag", "bag", "5"},
      {"", "", "1"},
      {"a", "", "1"},
      {"", "a", "0"},
      {"aaa", "aa", "3"},
      {"aabbcc", "abc", "8"},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (String[] c : cases) { // for (String[] 字符 : cases) {
      long got = numDistinct(c[0], c[1]); // 把 numDistinct(字符[0], 字符[1]); 写入 long got
      long want = Long.parseLong(c[2]); // 把 Long.parseLong(字符[2]); 写入 long want
      if (got != want) { // 若 got 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL solve(\"" + c[0] + "\",\"" + c[1] + "\")=" + got + " want " + want); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
