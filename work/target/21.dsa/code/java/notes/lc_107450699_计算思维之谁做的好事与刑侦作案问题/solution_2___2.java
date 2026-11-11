// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
package com.webfault.dsa; // 引入依赖

class lc107450699_solution22 { // 定义类型
  // 思路：用数字表示人 (0=A,1=B,2=C,3=D)
  static char whoDidGood() { // 定义函数/方法 whoDidGood
    for (int k = 0; k < 4; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 4 就继续
      int s = (k != 0 ? 1 : 0) + (k == 2 ? 1 : 0) + (k == 3 ? 1 : 0) + (k != 3 ? 1 : 0);
      if (s == 3) return (char) ('A' + k); // 若 字符串 等于 3，直接返回 (char) ('A' 加 下标 k)
    }
    return '?'; // 返回 '?'
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    char r = whoDidGood(); // 把 whoDidGood(); 写入 char r
    if (r != 'C') { // 若 右指针 不等于 'C'
      System.out.println("FAIL " + r); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
