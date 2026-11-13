// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355653
package com.webfault.dsa; // 引入依赖

class Pow3S1 { // 定义类型
  static boolean isPowerOfThree(int n) { // 定义判定函数 isPowerOfThree
    while (n != 0 && n % 3 == 0)
      n = n / 3; // 循环，直到不满足「元素个数 不等于 0 且 元素个数 对…取模 3 等于 0) 元素个数 赋值为 元素个数 除以 3;」
    return n == 1; // 返回 元素个数 等于 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean[] got = { // 把 { 写入 boolean[] got
      Pow3S1.isPowerOfThree(1),
      Pow3S1.isPowerOfThree(3),
      Pow3S1.isPowerOfThree(9),
      Pow3S1.isPowerOfThree(2),
      Pow3S1.isPowerOfThree(0),
    };
    boolean[] want = {
      true, true, true, false, false
    }; // 把 { true, true, true, false, false }; 写入 boolean[] want
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
