package com.webfault.dsa; // 引入依赖

class lc268_solution1 { // 定义类型
  // 丢失的数字：高斯求和 - 总和差值
  // 忠实翻译 Python ref_missingNumber: n*(n+1)//2 - sum(nums)
  static int missingNumber(int[] nums) { // 定义函数/方法 missingNumber
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int sum = 0; // 把 0 存入 累计和
    for (int v : nums) sum += v; // 把 值; 写入 for (int v : nums) sum +
    return n * (n + 1) / 2 - sum; // 返回 元素个数 乘 (元素个数 加 1) 除以 2 减 累计和
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] inputs = {{3, 0, 1}, {0, 1}, {9, 6, 4, 2, 3, 5, 7, 0, 1}};
    int[] wants = {2, 2, 8}; // 把 {2, 2, 8}; 写入 int[] wants
    for (int i = 0; i < inputs.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 inputs.长度 就继续
      int got = missingNumber(inputs[i]); // 把 missingNumber(inputs[下标 i]) 存入 got
      if (got != wants[i]) { // 若 got 不等于 wants[下标 i]
        System.out.println(
            "FAIL: missingNumber("
                + java.util.Arrays.toString(inputs[i])
                + ")="
                + got
                + " want "
                + wants[i]); // 打印输出
        System.exit(1); // System.exit(1);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
