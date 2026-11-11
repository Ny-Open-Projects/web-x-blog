package com.webfault.dsa; // 引入依赖

import java.math.BigInteger; // 引入依赖

class lc67_solution1 { // 定义类型
  // 二进制求和：使用 BigInteger 按二进制相加（忠实于 Python bin(int(a,2)+int(b,2))）
  static String addBinary(String a, String b) { // 定义函数/方法 addBinary
    BigInteger x = new BigInteger(a, 2); // 把 new BigInteger(数组, 2); 写入 BigInteger x
    BigInteger y = new BigInteger(b, 2); // 把 new BigInteger(b, 2); 写入 BigInteger y
    return x.add(y).toString(2); // 返回 x 追加 y).toString(2)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][] cases = { // 把 { 写入 String[][] cases
      {"11", "1", "100"},
      {"1010", "1011", "10101"},
      {"0", "0", "0"},
    };
    for (String[] c : cases) { // for (String[] 字符 : cases) {
      String got = addBinary(c[0], c[1]); // 把 addBinary(字符[0], 字符[1]) 存入 got
      if (!got.equals(c[2])) { // 若 取反 got.equals(字符[2]
        System.out.println(
            "FAIL: addBinary(" + c[0] + "," + c[1] + ")=" + got + " want " + c[2]); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
