// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144821546
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static int findLengthOfLCIS(int[] nums) { // 定义函数/方法 findLengthOfLCIS
    if (nums.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    int best = 1, cur = 1; // 把 1, 当前值 赋值为 1 存入 当前最优
    for (int i = 1; i < nums.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] > nums[i - 1]) cur++;
      else cur = 1; // 若 数组[下标 i] 超过 数组[下标 i 减 1]) 当前值 加一 ; else 当前值 赋值为 1;
      if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
    }
    return best; // 返回 当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{1, 3, 5, 4, 7}, {2, 2, 2, 2, 2}, {1, 3, 5}};
    int[] wants = {3, 1, 3};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      int got = findLengthOfLCIS(ins[i]); // 把 findLengthOfLCIS(ins[下标 i]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
