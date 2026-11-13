// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
package com.webfault.dsa; // 引入依赖

class RiverSafe { // 定义类型
  static boolean isSafe(int r, int g) { // 定义判定函数 isSafe
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][][] cases = {{{3, 3}}, {{3, 1}}, {{2, 2}}, {{1, 3}}, {{0, 0}}};
    boolean[] want = {
      true, true, true, false, true
    }; // 把 {true, true, true, false, true}; 写入 boolean[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < cases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
      boolean got = isSafe(cases[i][0][0], cases[i][0][1]);
      if (got != want[i]) { // 若 got 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL isSafe("
                + cases[i][0][0]
                + ","
                + cases[i][0][1]
                + ")="
                + got
                + " want "
                + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
