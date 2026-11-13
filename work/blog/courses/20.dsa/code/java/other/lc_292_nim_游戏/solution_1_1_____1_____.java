// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355568
package com.webfault.dsa; // 引入依赖

class NimS1 { // 定义类型
  static boolean canWinNim(int n) { // 定义函数/方法 canWinNim
    return n % 4 != 0; // 返回 元素个数 对…取模 4 不等于 0
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean[] got = { // 把 { 写入 boolean[] got
      NimS1.canWinNim(1), NimS1.canWinNim(4), NimS1.canWinNim(2),
    };
    boolean[] want = {true, false, true}; // 把 { true, false, true }; 写入 boolean[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
