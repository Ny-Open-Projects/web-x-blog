// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
package com.webfault.dsa; // 引入依赖

class lc116567013_solution11 { // 定义类型
  // Brute-Force 模式匹配（主串指针回退）
  static int matchV1(String P, String T) { // 定义函数/方法 matchV1
    int n = T.length(),
        m = P.length(),
        i = 0,
        j = 0; // 把 T.长度(), 映射表 赋值为 P.长度(), 下标 i 赋值为 0, 下标 j 赋值为 0 存入 元素个数
    while (j < m && i < n) { // 循环，直到不满足「下标 j 小于 映射表 且 下标 i 小于 元素个数」
      if (T.charAt(i) == P.charAt(j)) { // 若 T 取字符 下标 i) 等于 P 取字符 下标 j
        i++; // 下标 i 加一
        j++; // 下标 j 加一
      } else { // 否则
        i -= (j - 1); // 下标 i累减 (下标 j 减 1)
        j = 0; // 把 0; 写入 下标 j
      }
    }
    return (j == m) ? (i - j) : -1; // 返回 (下标 j 等于 映射表) ? (下标 i 减 下标 j) : 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String T =
        "now is the time for all good people to come"; // 把 「now is the time for all good people to
                                                       // come」 存入 T
    if (matchV1("people", T) != 29) {
      System.out.println("FAIL people");
      throw new RuntimeException("FAILED");
    }
    if (matchV1("good", T) != 24) {
      System.out.println("FAIL good");
      throw new RuntimeException("FAILED");
    }
    if (matchV1("xyz", T) != -1) {
      System.out.println("FAIL xyz");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
