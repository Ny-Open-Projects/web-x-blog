// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
package com.webfault.dsa; // 引入依赖

/**
 * LeetCode 509. 斐波那契数 忠实翻译 python/dp/lc_509_斐波那契数/solution_10___10.py 矩阵快速幂：[[1,1],[1,0]]^(n-1)
 * 的左上角元素
 */
class Main { // 定义类型

  static long[][] matMul(long[][] a, long[][] b) { // 定义函数/方法 matMul
    return new long[][] { // 返回 new long[][] {
      {a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]},
      {a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]}
    };
  }

  static long[][] matPow(long[][] mat, int p) { // 定义函数/方法 matPow
    long[][] res =
        new long[][] {{1, 0}, {0, 1}}; // 把 new long[][] { { 1, 0 }, { 0, 1 } }; 写入 long[][] res
    long[][] base = new long[][] {{mat[0][0], mat[0][1]}, {mat[1][0], mat[1][1]}};
    int e = p; // 把 节点 存入 e
    while (e > 0) { // 循环，直到不满足「e 超过 0」
      if ((e & 1) == 1) { // 若 (e 按位与 1) 等于 1
        res = matMul(res, base); // 把 matMul(结果, base); 写入 结果
      }
      base = matMul(base, base); // 把 matMul(base, base); 写入 base
      e >>= 1; // 把 1; 写入 e >>
    }
    return res; // 返回 结果
  }

  long fib(int n) { // 定义函数/方法 fib
    if (n == 0) { // 若 元素个数 等于 0
      return 0; // 返回 0
    }
    if (n == 1) { // 若 元素个数 等于 1
      return 1; // 返回 1
    }
    long[][] m = matPow(new long[][] {{1, 1}, {1, 0}}, n - 1);
    return m[0][0]; // 返回 映射表[0][0]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {0, 0}, // 边界：n=0
      {1, 1}, // 边界：n=1
      {2, 1},
      {5, 5},
      {10, 55},
      {30, 832040} // {30, 832040}
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      Main s = new Main(); // 把 new Main(); 写入 Main s
      long got = s.fib(c[0]); // 把 字符串.fib(字符[0]); 写入 long got
      if (got != (long) c[1]) { // 若 got 不等于 (long) 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL fib(" + c[0] + ")=" + got + " want " + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
