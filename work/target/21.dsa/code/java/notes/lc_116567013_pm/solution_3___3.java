// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
package com.webfault.dsa; // 引入依赖

class lc116567013_solution33 { // 定义类型
  // KMP 模式匹配
  static int[] buildNext(String P) { // 定义函数/方法 buildNext
    int m = P.length(); // 把 P.长度() 存入 映射表
    int[] N = new int[m]; // 把 new int[映射表]; 写入 int[] N
    N[0] = -1; // 把 减 1; 写入 N[0]
    int j = 0, t = -1; // 把 0, 另一字符串 赋值为 减 1 存入 下标 j
    while (j < m - 1) { // 循环，直到不满足「下标 j 小于 映射表 减 1」
      if (t < 0 || P.charAt(j) == P.charAt(t)) { // 若 另一字符串 小于 0 或 P 取字符 下标 j) 等于 P 取字符 另一字符串
        j++; // 下标 j 加一
        t++; // 另一字符串 加一
        N[j] = t; // 把 另一字符串; 写入 N[j]
      } else { // 否则
        t = N[t]; // 把 N[另一字符串]; 写入 另一字符串
      }
    }
    return N; // 返回 N
  }

  static int kmpMatch(String P, String T) { // 定义函数/方法 kmpMatch
    int[] N = buildNext(P); // 把 buildNext(P); 写入 int[] N
    int n = T.length(),
        m = P.length(),
        i = 0,
        j = 0; // 把 T.长度(), 映射表 赋值为 P.长度(), 下标 i 赋值为 0, 下标 j 赋值为 0 存入 元素个数
    while (j < m && i < n) { // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
      if (j < 0 || T.charAt(i) == P.charAt(j)) { // 若 下标 j 小于 0 或 T 取字符 下标 i) 等于 P 取字符 下标 j
        i++; // 下标 i 加一
        j++; // 下标 j 加一
      } else { // 否则
        j = N[j]; // 把 N[下标 j]; 写入 下标 j
      }
    }
    return (j == m) ? (i - j) : -1; // 返回 (下标 j 等于 映射表) ? (下标 i 减 下标 j) : 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String T =
        "now is the time for all good people to come"; // 把 「now is the time for all good people to
                                                       // come」 存入 T
    if (kmpMatch("people", T) != 29) {
      System.out.println("FAIL people");
      throw new RuntimeException("FAILED");
    }
    if (kmpMatch("all", T) != 20) {
      System.out.println("FAIL all");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
