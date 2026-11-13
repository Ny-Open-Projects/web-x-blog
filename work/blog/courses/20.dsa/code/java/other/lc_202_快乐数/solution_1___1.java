// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355335
package com.webfault.dsa; // 引入依赖

class HappyS1 { // 定义类型
  static int bitSquareSum(int n) { // 定义函数/方法 bitSquareSum
    int total = 0; // 把 0 存入 总和
    while (n != 0) { // 循环，直到不满足「元素个数 不等于 0」
      int digit = n % 10; // 把 元素个数 对…取模 10 存入 digit
      total += digit * digit; // 总和累加 digit 乘 digit
      n /= 10; // 把 10; 写入 n /
    }
    return total; // 返回 总和
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] got = { // 把 { 写入 int[] got
      HappyS1.bitSquareSum(1),
      HappyS1.bitSquareSum(19),
      HappyS1.bitSquareSum(0),
      HappyS1.bitSquareSum(123),
    };
    int[] want = {1, 82, 0, 14}; // 把 { 1, 82, 0, 14 }; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < got.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 就继续
      if (got[i] != want[i]) { // 若 got[下标 i] 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL bitSquareSum idx " + i + " got " + got[i] + " want " + want[i]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
