// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
package com.webfault.dsa; // 引入依赖

class lc116567013_solution22 { // 定义类型
  // Brute-Force 模式匹配（双循环对齐）
  static int matchV2(String P, String T) { // 定义函数/方法 matchV2
    int n = T.length(), m = P.length(); // 把 T.长度(), 映射表 赋值为 P.长度() 存入 元素个数
    for (int i = 0; i <= n - m; i++) { // 让 下标 i 从 0 开始计数，下标 i 不超过 元素个数 减 映射表 就继续
      int j = 0; // 把 0 存入 下标 j
      while (j < m && T.charAt(i + j) == P.charAt(j)) j++;
      if (j == m) return i; // 若 下标 j 等于 映射表，直接返回 下标 i
    }
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String T =
        "now is the time for all good people to come"; // 把 「now is the time for all good people to
                                                       // come」 存入 T
    if (matchV2("people", T) != 29) {
      System.out.println("FAIL people");
      throw new RuntimeException("FAILED");
    }
    if (matchV2("time", T) != 11) {
      System.out.println("FAIL time");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
