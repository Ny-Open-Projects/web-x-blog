// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116019
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static int minSubArrayLen(int target, int[] nums) { // 定义函数/方法 minSubArrayLen
    int l = 0, best = nums.length + 1, sum = 0; // 把 0, 当前最优 赋值为 数组.长度 加 1, 累计和 赋值为 0 存入 左指针
    for (int r = 0; r < nums.length; r++) { // 让 右指针 从 0 开始计数，右指针 小于 数组.长度 就继续
      sum += nums[r]; // 累计和累加 数组[右指针]
      while (sum >= target) { // 循环，直到不满足「累计和 不低于 目标值」
        if (r - l + 1 < best) best = r - l + 1; // 若 右指针 减 左指针 加 1 小于 当前最优) 当前最优 赋值为 右指针 减 左指针 加 1;
        sum -= nums[l++]; // 累计和累减 数组[左指针 加一 ]
      }
    }
    return best == nums.length + 1 ? 0 : best; // 返回 当前最优 等于 数组.长度 加 1 ? 0 : 当前最优
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] t = {7, 4, 11};
    int[][] n = {{2, 3, 1, 2, 4, 3}, {1, 4, 4}, {1, 1, 1, 1, 1, 1, 1, 1}};
    int[] ws = {2, 1, 0};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < t.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 另一字符串.长度 就继续
      int got = minSubArrayLen(t[i], n[i]); // 把 minSubArrayLen(另一字符串[下标 i], 元素个数[下标 i]) 存入 got
      if (got != ws[i]) {
        ok = false;
        System.out.println("FAIL " + got + " want " + ws[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
