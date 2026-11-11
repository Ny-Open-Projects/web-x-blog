// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package com.webfault.dsa; // 引入依赖

// 下楼梯问题：每步可走 1/2/3 级（方案2，自底向上 DP / 递推计数）
class Main { // 定义类型
  static int climbStairsCount(int h) { // 定义函数/方法 climbStairsCount
    if (h < 0) return 0; // 若 h 小于 0，直接返回 0
    if (h == 0) return 1; // 若 h 等于 0，直接返回 1
    if (h == 1) return 1; // 若 h 等于 1，直接返回 1
    if (h == 2) return 2; // 若 h 等于 2，直接返回 2
    int[] dp = new int[h + 1]; // 把 new int[h 加 1]; 写入 int[] dp
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2; // 把 1; DP 表[1] 赋值为 1; DP 表[2] 赋值为 2; 写入 dp[0]
    for (int i = 3; i <= h; i++)
      dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]; // 让 下标 i 从 3 开始计数，下标 i 不超过 h 就继续
    return dp[h]; // 返回 DP 表[h]
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = {{4, 7}, {6, 24}, {10, 274}, {0, 1}, {1, 1}, {2, 2}, {3, 4}, {-1, 0}};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[] c : cases) { // for (int[] 字符 : cases) {
      int got = climbStairsCount(c[0]); // 把 climbStairsCount(字符[0]) 存入 got
      if (got != c[1]) { // 若 got 不等于 字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL climbStairsCount(" + c[0] + ")=" + got + " want " + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
