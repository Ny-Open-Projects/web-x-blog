// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
package com.webfault.dsa; // 引入依赖

class lc115_solution222 { // 定义类型
  private String s, t; // private String 字符串, 另一字符串;
  private long[][] memo; // private long[][] 记忆化表;

  // numDistinct 忠实翻译 python ref solution_2_2_____2_________.py（lru_cache 记忆化递归）
  public long numDistinct(String s, String t) { // 定义函数/方法 numDistinct
    this.s = s; // 把 字符串; 写入 字符串
    this.t = t; // 把 另一字符串; 写入 另一字符串
    int sLen = s.length(), tLen = t.length(); // 把 字符串.长度(), tLen 赋值为 另一字符串.长度() 存入 sLen
    memo = new long[sLen][tLen]; // 把 new long[sLen][tLen]; 写入 记忆化表
    for (int i = 0; i < sLen; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 sLen 就继续
      for (int j = 0; j < tLen; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 tLen 就继续
        memo[i][j] = -1; // 把 减 1; 写入 memo[i][j]
      }
    }
    return helper(sLen - 1, tLen - 1); // 返回 helper(sLen 减 1, tLen 减 1)
  }

  private long helper(int i, int j) { // 定义函数/方法 helper
    if (j < 0) { // 若 下标 j 小于 0
      return 1; // 返回 1
    }
    if (i < 0) { // 若 下标 i 小于 0
      return 0; // 返回 0
    }
    if (memo[i][j] != -1) { // 若 记忆化表[下标 i][下标 j] 不等于 减 1
      return memo[i][j]; // 返回 记忆化表[下标 i][下标 j]
    }
    if (s.charAt(i) == t.charAt(j)) { // 若 字符串 取字符 下标 i) 等于 另一字符串 取字符 下标 j
      memo[i][j] = helper(i - 1, j) + helper(i - 1, j - 1);
    } else { // 否则
      memo[i][j] = helper(i - 1, j); // 把 helper(下标 i 减 1, 下标 j); 写入 memo[i][j]
    }
    return memo[i][j]; // 返回 记忆化表[下标 i][下标 j]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc115_solution222 s =
        new lc115_solution222(); // 把 new lc115_solution222(); 写入 lc115_solution222 s
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
