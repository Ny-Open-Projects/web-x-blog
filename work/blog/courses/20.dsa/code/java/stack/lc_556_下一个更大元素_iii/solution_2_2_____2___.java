// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
package com.webfault.dsa; // 引入依赖

class lc556_solution222 { // 定义类型
  static int nextGreaterElement(int n) { // 定义函数/方法 nextGreaterElement
    final int MAX = 2147483647; // 32 位上限
    int[] digits = new int[12]; // 逐位拆解
    int len = 0;
    if (n == 0) digits[len++] = 0;
    int x = n;
    while (x > 0) {
      digits[len++] = x % 10;
      x /= 10;
    }
    for (int i = 0; i < len / 2; i++) {
      int t = digits[i];
      digits[i] = digits[len - 1 - i];
      digits[len - 1 - i] = t;
    }
    int i = len - 2; // 从右找第一个降序位
    while (i >= 0 && digits[i] >= digits[i + 1]) i--;
    if (i < 0) return -1; // 整体降序，无更大排列
    int j = len - 1; // 从右找第一个大于 digits[i] 的位
    while (digits[j] <= digits[i]) j--;
    int t = digits[i];
    digits[i] = digits[j];
    digits[j] = t; // 交换
    for (int a = i + 1, b = len - 1; a < b; a++, b--) {
      t = digits[a];
      digits[a] = digits[b];
      digits[b] = t;
    } // 后缀升序
    long result = 0; // 重拼数字
    for (int k = 0; k < len; k++) result = result * 10 + digits[k];
    return result > MAX ? -1 : (int) result;
  }

  public static void main(String[] args) { // 程序入口：跑内嵌自测用例
    int[][] cases = {
      {12, 21}, {21, -1}, {2147483647, -1}, {12443322, 13222344}, {10, -1}, {230241, 230412}
    };
    boolean ok = true;
    for (int[] c : cases) {
      int got = nextGreaterElement(c[0]);
      if (got != c[1]) {
        ok = false;
        System.out.println("FAIL " + c[0] + "=" + got + " want " + c[1]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED");
    System.out.println("PASS");
  }
}
