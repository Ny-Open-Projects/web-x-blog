// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
package com.webfault.dsa; // 引入依赖

class lc313_solution33 { // 定义类型
  // nthSuperUglyNumber 忠实翻译 python ref solution_3___3.py（多指针 DP，手动 min 循环）
  public static long nthSuperUglyNumber(int n, int[] primes) {
    long[] dp = new long[n + 1]; // 把 new long[元素个数 加 1]; 写入 long[] dp
    int m = primes.length; // 把 primes.长度 存入 映射表
    int[] pointers = new int[m]; // 把 new int[映射表]; 写入 int[] pointers
    long[] nums = new long[m]; // 把 new long[映射表]; 写入 long[] nums
    for (int j = 0; j < m; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 映射表 就继续
      nums[j] = 1; // 把 1; 写入 nums[j]
    }
    for (int i = 1; i <= n; i++) { // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
      long minNum = Long.MAX_VALUE; // 把 Long.MAX_VALUE; 写入 long minNum
      for (int j = 0; j < m; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 映射表 就继续
        minNum = Math.min(minNum, nums[j]); // 把 Math.取较小值 minNum, 数组[下标 j]); 写入 minNum
      }
      dp[i] = minNum; // 把 minNum; 写入 dp[i]
      for (int j = 0; j < m; j++) { // 让 下标 j 从 0 开始计数，下标 j 小于 映射表 就继续
        if (nums[j] == minNum) { // 若 数组[下标 j] 等于 minNum
          pointers[j]++; // pointers[下标 j] 加一 ;
          nums[j] =
              dp[pointers[j]] * primes[j]; // 把 DP 表[pointers[下标 j]] 乘 primes[下标 j]; 写入 nums[j]
        }
      }
    }
    return dp[n]; // 返回 DP 表[元素个数]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // want 由 python ref solution_3___3.py 实跑得到
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
