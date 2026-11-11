// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145029963
package com.webfault.dsa; // 引入依赖

// 只出现一次的数字：位运算解法（方案1）。
// 所有元素异或，成对数字抵消，剩下只出现一次的数字。忠实翻译自 Python 参考实现。
class lc136_solution111 { // 定义类型
  static int singleNumber(int[] nums) { // 定义函数/方法 singleNumber
    int res = 0; // 把 0 存入 结果
    for (int v : nums) res ^= v; // 把 值; 写入 for (int v : nums) res ^
    return res; // 返回 结果
  }

  static boolean selfCheck() { // 定义函数/方法 selfCheck
    // (args, expected) 取自 _tools/correctness_check.py 的 lc_136_只出现一次的数字 cases
    int[][] cases = { // 把 { 写入 int[][] cases
      {2, 2, 1},
      {4, 1, 2, 1, 2},
      {1},
    };
    int[] wants = {1, 4, 1}; // 把 {1, 4, 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int k = 0; k < cases.length; k++) { // 让 下标 k 从 0 开始计数，下标 k 小于 cases.长度 就继续
      int got = singleNumber(cases[k]); // 把 singleNumber(cases[下标 k]) 存入 got
      if (got != wants[k]) { // 若 got 不等于 wants[下标 k]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL case" + (k + 1) + ": got " + got + " want " + wants[k]); // 打印输出
      }
    }
    return ok; // 返回 ok
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    if (!selfCheck()) { // 若 取反 selfCheck(
      System.out.println("FAIL"); // 打印输出
      System.exit(1); // System.exit(1);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
