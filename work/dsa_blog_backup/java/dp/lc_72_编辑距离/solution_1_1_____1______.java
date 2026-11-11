// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848060
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc72_solution111 { // 定义类型
  public int minDistance(String word1, String word2) { // 定义函数/方法 minDistance
    int n = word1.length(); // 把 word1.长度() 存入 元素个数
    int m = word2.length(); // 把 word2.长度() 存入 映射表
    if (n * m == 0) { // 若 元素个数 乘 映射表 等于 0
      return n + m; // 返回 元素个数 加 映射表
    }
    int[][] D = new int[n + 1][m + 1]; // 把 new int[元素个数 加 1][映射表 加 1]; 写入 int[][] D
    for (int i = 0; i <= n; i++) { // 让 下标 i 从 0 开始计数，下标 i 不超过 元素个数 就继续
      D[i][0] = i; // 把 下标 i; 写入 D[i][0]
    }
    for (int j = 0; j <= m; j++) { // 让 下标 j 从 0 开始计数，下标 j 不超过 映射表 就继续
      D[0][j] = j; // 把 下标 j; 写入 D[0][j]
    }
    for (int i = 1; i < n + 1; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 加 1 就继续
      for (int j = 1; j < m + 1; j++) { // 让 下标 j 从 1 开始计数，下标 j 小于 映射表 加 1 就继续
        int left = D[i - 1][j] + 1; // 把 D[下标 i 减 1][下标 j] 加 1 存入 左边界
        int down = D[i][j - 1] + 1; // 把 D[下标 i][下标 j 减 1] 加 1 存入 down
        int left_down = D[i - 1][j - 1]; // 把 D[下标 i 减 1][下标 j 减 1] 存入 left_down
        if (word1.charAt(i - 1)
            != word2.charAt(j - 1)) { // 若 word1 取字符 下标 i 减 1) 不等于 word2 取字符 下标 j 减 1
          left_down += 1; // left_down累加 1
        }
        D[i][j] =
            Math.min(
                Math.min(left, down),
                left_down); // 把 Math.取较小值 Math.取较小值 左边界, down), left_down); 写入 D[i][j]
      }
    }
    return D[n][m]; // 返回 D[元素个数][映射表]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc72_solution111 s = new lc72_solution111(); // 把 new lc72_solution111(); 写入 lc72_solution111 s
    int got = s.minDistance("horse", "ros"); // 把 字符串.minDistance(「horse」, 「horse」) 存入 got
    if (got != 3) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
