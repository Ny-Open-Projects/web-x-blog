// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
package com.webfault.dsa; // 引入依赖

class BitS1 { // 定义类型
  static int onesCount(int x) { // 定义函数/方法 onesCount
    int c = 0; // 把 0 存入 字符
    while (x > 0) { // 循环，直到不满足「x 超过 0」
      c += x & 1; // 字符累加 x 按位与 1
      x >>= 1; // 把 1; 写入 x >>
    }
    return c; // 返回 字符
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] got = { // 把 { 写入 int[] got
      BitS1.onesCount(1), BitS1.onesCount(7), BitS1.onesCount(0), BitS1.onesCount(15),
    };
    int[] want = {1, 3, 0, 4}; // 把 { 1, 3, 0, 4 }; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++)
      if (got[i] != want[i]) {
        ok = false;
        System.out.println("FAIL onesCount(" + i + ")=" + got[i]);
      } // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
