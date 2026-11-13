// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
// LeetCode 113951689. 动态规划之 LCS — Java 版（最长公共子序列：DP 填表 + 回溯构造）
package com.webfault.dsa; // 引入依赖

class Lcs { // 定义类型
  static int lcsLength(String a, String b) { // 定义函数/方法 lcsLength
    int m = a.length(), n = b.length(); // 把 数组.长度(), 元素个数 赋值为 b.长度() 存入 映射表
    int[][] dp = new int[m + 1][n + 1]; // 把 new int[映射表 加 1][元素个数 加 1]; 写入 int[][] dp
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
        if (a.charAt(i - 1) == b.charAt(j - 1)) { // 若 数组 取字符 下标 i 减 1) 等于 b 取字符 下标 j 减 1
          dp[i][j] = dp[i - 1][j - 1] + 1; // 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1; 写入 dp[i][j]
        } else { // 否则
          dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
      }
    }
    return dp[m][n]; // 返回 DP 表[映射表][元素个数]
  }

  static String lcsString(String a, String b) { // 定义函数/方法 lcsString
    int m = a.length(), n = b.length(); // 把 数组.长度(), 元素个数 赋值为 b.长度() 存入 映射表
    int[][] dp = new int[m + 1][n + 1]; // 把 new int[映射表 加 1][元素个数 加 1]; 写入 int[][] dp
    for (int i = 1; i <= m; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      for (int j = 1; j <= n; j++) { // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
        dp[i][j] =
            a.charAt(i - 1) == b.charAt(j - 1) // 逐字符处理
                ? dp[i - 1][j - 1] + 1 // ? DP 表[下标 i 减 1][下标 j 减 1] 加 1
                : Math.max(
                    dp[i - 1][j],
                    dp[i][j - 1]); // : Math.取较大值 DP 表[下标 i 减 1][下标 j], DP 表[下标 i][下标 j 减 1]);
      }
    }
    StringBuilder sb = new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
    int i = m, j = n; // 把 映射表, 下标 j 赋值为 元素个数 存入 下标 i
    while (i > 0 && j > 0) { // 循环，直到不满足「下标 i 超过 0 且 下标 j 超过 0」
      if (a.charAt(i - 1) == b.charAt(j - 1)) { // 若 数组 取字符 下标 i 减 1) 等于 b 取字符 下标 j 减 1
        sb.append(a.charAt(i - 1)); // 把 数组 取字符 下标 i 减 1 追加到列表尾部
        i--; // 下标 i 减一
        j--; // 下标 j 减一
      } else if (dp[i - 1][j]
          >= dp[i][j - 1]) { // 否则，若 DP 表[下标 i 减 1][下标 j] 不低于 DP 表[下标 i][下标 j 减 1]
        i--; // 下标 i 减一
      } else { // 否则
        j--; // 下标 j 减一
      }
    }
    return sb.reverse().toString(); // 返回 sb.reverse().toString()
  }

  static boolean isCommonSub(String a, String b, String s) { // 定义判定函数 isCommonSub
    int ia = 0, ib = 0; // 把 0, ib 赋值为 0 存入 ia
    for (char ch : s.toCharArray()) { // for (char 字符 : 字符串.toCharArray()) {
      while (ia < a.length() && a.charAt(ia) != ch)
        ia++; // 循环，直到不满足「ia 小于 数组.长度() 且 数组 取字符 ia) 不等于 字符) ia 加一 ;」
      while (ib < b.length() && b.charAt(ib) != ch)
        ib++; // 循环，直到不满足「ib 小于 b.长度() 且 b 取字符 ib) 不等于 字符) ib 加一 ;」
      if (ia >= a.length() || ib >= b.length())
        return false; // 若 ia 不低于 数组.长度() 或 ib 不低于 b.长度()，直接返回 false
      ia++; // ia 加一
      ib++; // ib 加一
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {"ABCBDAB", "BDCABA", 4},
      {"AGGTAB", "GXTXAYB", 4},
      {"abc", "abc", 3},
      {"", "abc", 0},
      {"abc", "xyz", 0},
    };
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      int got =
          lcsLength(
              (String) c[0], (String) c[1]); // 把 lcsLength((String) 字符[0], (String) 字符[1]) 存入 got
      if (got != (int) c[2]) { // 若 got 不等于 (int) 字符[2]
        System.out.println("case failed: got " + got + " want " + c[2]); // 打印输出
        return; // return;
      }
    }
    String[][] pairs = {{"ABCBDAB", "BDCABA"}, {"AGGTAB", "GXTXAYB"}};
    for (String[] p : pairs) { // for (String[] 节点 : pairs) {
      String s = lcsString(p[0], p[1]); // 把 lcsString(节点[0], 节点[1]) 存入 字符串
      if (s.length() != lcsLength(p[0], p[1]) || !isCommonSub(p[0], p[1], s)) {
        System.out.println("lcsString failed: " + s); // 打印输出
        return; // return;
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
