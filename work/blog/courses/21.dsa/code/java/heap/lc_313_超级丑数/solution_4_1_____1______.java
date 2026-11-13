// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
package com.webfault.dsa; // 引入依赖

import java.util.PriorityQueue; // 引入依赖

class lc313_solution411 { // 定义类型
  // nthSuperUglyNumber 忠实翻译 python ref solution_4_1_____1______.py（最小堆，弹出时跳过重复值）
  static long nthSuperUglyNumber(int n, int[] primes) { // 定义函数/方法 nthSuperUglyNumber
    long[] ugly = new long[n]; // 把 new long[元素个数]; 写入 long[] ugly
    for (int x = 0; x < n; x++) { // 让 x 从 0 开始计数，x 小于 元素个数 就继续
      ugly[x] = 1; // python: ugly = [1] * n
    }
    int[] p = new int[primes.length]; // 把 new int[primes.长度]; 写入 int[] p
    // python heapq 元组 (val, j) 字典序比较
    PriorityQueue<long[]> heap =
        new PriorityQueue<>(
            (a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
    for (int j = 0; j < primes.length; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 primes.长度 就继续
      heap.offer(new long[] {primes[j], j}); // 堆.offer(new long[]{primes[下标 j], 下标 j});
    }
    for (int i = 1; i < n; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 就继续
      long[] top = heap.poll(); // 把 堆.poll(); 写入 long[] top
      long val = top[0]; // 把 top[0]; 写入 long val
      int j = (int) top[1]; // 把 (int) top[1] 存入 下标 j
      while (val == ugly[i - 1]) { // 循环，直到不满足「值 等于 ugly[下标 i 减 1]」
        p[j]++; // 节点[下标 j] 加一 ;
        heap.offer(
            new long[] {
              ugly[p[j]] * primes[j], j
            }); // 堆.offer(new long[]{ugly[节点[下标 j]] 乘 primes[下标 j], 下标 j});
        top = heap.poll(); // 把 堆.poll(); 写入 top
        val = top[0]; // 把 top[0]; 写入 值
        j = (int) top[1]; // 把 (int) top[1]; 写入 下标 j
      }
      ugly[i] = val; // 把 值; 写入 ugly[i]
      p[j]++; // 节点[下标 j] 加一 ;
      heap.offer(
          new long[] {
            ugly[p[j]] * primes[j], j
          }); // 堆.offer(new long[]{ugly[节点[下标 j]] 乘 primes[下标 j], 下标 j});
    }
    return ugly[n - 1]; // 返回 ugly[元素个数 减 1]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // want 由 python ref solution_4_1_____1______.py 实跑得到
    Object[][] cases = { // 把 { 写入 Object[][] cases
      {12, new int[] {2, 7, 13, 19}, 32L},
      {10, new int[] {2, 3, 5}, 12L},
      {1, new int[] {2}, 1L},
      {2, new int[] {2}, 2L},
      {6, new int[] {2, 3, 5}, 6L},
      {7, new int[] {3, 5, 7}, 21L},
      {5, new int[] {2, 3}, 6L},
      {17, new int[] {2, 3, 5}, 27L},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      long got = nthSuperUglyNumber((Integer) c[0], (int[]) c[1]);
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
