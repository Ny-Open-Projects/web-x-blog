// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
package com.webfault.dsa; // 引入依赖

class lc107450699_solution33 { // 定义类型
  static String solveCrime() { // 定义函数/方法 solveCrime
    char[] names = {
      'A', 'B', 'C', 'D', 'E', 'F'
    }; // 把 {'A', 'B', 'C', 'D', 'E', 'F'}; 写入 char[] names
    for (int a = 0; a < 2; a++) // 让 数组 从 0 开始计数，数组 小于 2 就继续
    for (int b = 0; b < 2; b++) // 让 b 从 0 开始计数，b 小于 2 就继续
      for (int c = 0; c < 2; c++) // 让 字符 从 0 开始计数，字符 小于 2 就继续
        for (int d = 0; d < 2; d++) // 让 d 从 0 开始计数，d 小于 2 就继续
          for (int e = 0; e < 2; e++) // 让 e 从 0 开始计数，e 小于 2 就继续
            for (int f = 0; f < 2; f++) { // 让 f 从 0 开始计数，f 小于 2 就继续
                if (((a == 1 || b == 1)
                    && ((a == 1 && e == 1) || (a == 1 && f == 1) || (e == 1 && f == 1))
                    && !(a == 1 && d == 1)
                    && ((b == 1 && c == 1) || (b == 0 && c == 0))
                    && ((c == 1 && d == 0) || (c == 0 && d == 1))
                    && (d == 1 || (d == 0 && e == 0)))) { // 把 赋值为 1 或 (d 等于 0 且 e 等于 0)))) { 写入 (d
                  StringBuilder sb =
                      new StringBuilder(); // 把 new StringBuilder(); 写入 StringBuilder sb
                  int[] vals = {a, b, c, d, e, f}; // 把 {数组, b, 字符, d, e, f}; 写入 int[] vals
                  for (int i = 0; i < 6; i++)
                    if (vals[i] == 1) sb.append(names[i]); // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
                  return sb.toString(); // 返回 sb.toString()
                }
              }
    return ""; // 返回 「」
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String r = solveCrime(); // 把 solveCrime() 存入 右指针
    if (!r.equals("ABCF")) { // 若 取反 右指针.equals(「ABCF」
      System.out.println("FAIL " + r); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
