// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

class lc313_solution22 { // 定义类型
  // nthSuperUglyNumber 忠实翻译 python ref solution_2___2.py（暴力枚举）
  // 注意：该 pyref 在 n>=2 时（i=2, j=0）会触发 i%0（ZeroDivisionError / ArithmeticException），
  // 仅 n=1 可正常工作，故用例只能覆盖 n=1。
  public long nthSuperUglyNumber(int n, int[] primes) { // 定义函数/方法 nthSuperUglyNumber
    List<Long> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Long> res
    res.add(1L); // 结果 追加 1L);
    int i = 2; // 把 2 存入 下标 i
    while (res.size() < n) { // 循环，直到不满足「结果.大小() 小于 元素个数」
      int l = 0; // 把 0 存入 左指针
      for (int j = 0; j < i; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
        if (i % j == 0
            && !containsPrime(primes, j)) { // 若 下标 i 对…取模 下标 j 等于 0 且 取反 containsPrime(primes, 下标 j
          break; // 跳出循环
        }
        l++; // 左指针 加一
      }
      if (l == 0) { // 若 左指针 等于 0
        if (containsPrime(primes, i)) { // 若 containsPrime(primes, 下标 i
          res.add((long) i); // 结果 追加 (long) 下标 i);
        }
      } else { // 否则
        res.add((long) i); // 结果 追加 (long) 下标 i);
      }
      i++; // 下标 i 加一
    }
    return res.get(n - 1); // 返回 结果 查找 元素个数 减 1)
  }

  private static boolean containsPrime(
      int[] primes, int x) { // private static boolean containsPrime(int[] primes, int x) {
    for (int p : primes) { // for (int 节点 : primes) {
      if (p == x) { // 若 节点 等于 x
        return true; // 返回 true
      }
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc313_solution22 s = new lc313_solution22(); // 把 new lc313_solution22(); 写入 lc313_solution22 s
    // want 由 python ref solution_2___2.py 实跑得到（仅 n=1 可用）
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {1, new int[] {}, 1L},
      {1, new int[] {2, 3, 5}, 1L},
      {1, new int[] {7}, 1L},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      long got = s.nthSuperUglyNumber((Integer) c[0], (int[]) c[1]);
      long want = (Long) c[2]; // 把 (Long) 字符[2]; 写入 long want
      if (got != want) { // 若 got 不等于 want
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL got " + got + " want " + want); // 打印输出
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
