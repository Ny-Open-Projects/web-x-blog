// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130455100
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static boolean canPlaceFlowers(int[] bed, int n) { // 定义函数/方法 canPlaceFlowers
    int m = bed.length; // 把 bed.长度 存入 映射表
    for (int i = 0; i < m; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
      if (bed[i] == 0 && (i == 0 || bed[i - 1] == 0) && (i == m - 1 || bed[i + 1] == 0)) {
        bed[i] = 1;
        n--; // 把 1; 元素个数 减一 ; 写入 bed[i]
      }
    }
    return n <= 0; // 返回 元素个数 不超过 0
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] a = {{1, 0, 0, 0, 1}, {1, 0, 0, 0, 1}, {0, 0, 1, 0, 0}};
    int[] ns = {1, 2, 1};
    boolean[] ws = {true, false, true};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      boolean got =
          canPlaceFlowers(a[i], ns[i]); // 把 canPlaceFlowers(数组[下标 i], ns[下标 i]); 写入 boolean got
      if (got != ws[i]) {
        ok = false;
        System.out.println("FAIL " + got + " want " + ws[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
