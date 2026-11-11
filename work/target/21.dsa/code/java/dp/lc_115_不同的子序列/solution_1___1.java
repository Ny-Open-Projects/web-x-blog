// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
package com.webfault.dsa; // 引入依赖

class lc115_solution11 { // 定义类型
  // numDistinct 忠实翻译 python ref solution_1___1.py（从后往前 DP）
  public long numDistinct(String s, String t) { // 定义函数/方法 numDistinct
    int m = s.length(); // 把 字符串.长度() 存入 映射表
    int n = t.length(); // 把 另一字符串.长度() 存入 元素个数
    long[][] dp = new long[m + 1][n + 1]; // 把 new long[映射表 加 1][元素个数 加 1]; 写入 long[][] dp
    for (int i = 0; i <= m; i++) { // 让 下标 i 从 0 开始计数，下标 i 不超过 映射表 就继续
      dp[i][n] = 1; // 把 1; 写入 dp[i][n]
    }
    for (int i = m - 1; i >= 0; i--) { // 让 下标 i 从 映射表 减 1 开始计数，下标 i 不低于 0 就继续
      for (int j = n - 1; j >= 0; j--) { // 让 下标 j 从 元素个数 减 1 开始计数，下标 j 不低于 0 就继续
        if (s.charAt(i) == t.charAt(j)) { // 若 字符串 取字符 下标 i) 等于 另一字符串 取字符 下标 j
          dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j];
        } else { // 否则
          dp[i][j] = dp[i + 1][j]; // 把 DP 表[下标 i 加 1][下标 j]; 写入 dp[i][j]
        }
      }
    }
    return dp[0][0]; // 返回 DP 表[0][0]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc115_solution11 s = new lc115_solution11(); // 把 new lc115_solution11(); 写入 lc115_solution11 s
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
      long got = s.numDistinct(c[0], c[1]); // 把 字符串.numDistinct(字符[0], 字符[1]); 写入 long got
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
