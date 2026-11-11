// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
package com.webfault.dsa; // 引入依赖

class lc110240695_solution11 { // 定义类型
  // 暴力枚举所有区间
  static int maxSubArrayBf(int[] arr) { // 定义函数/方法 maxSubArrayBf
    int n = arr.length; // 把 数组.长度 存入 元素个数
    if (n == 0) return 0; // 若 元素个数 等于 0，直接返回 0
    int gs = arr[0]; // 把 数组[0] 存入 gs
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      for (int j = i; j < n; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
        int s = 0; // 把 0 存入 字符串
        for (int k = i; k <= j; k++) s += arr[k]; // 让 下标 k 从 下标 i 开始计数，下标 k 不超过 下标 j 就继续
        if (gs < s) gs = s; // 若 gs 小于 字符串) gs 赋值为 字符串;
      }
    }
    return gs; // 返回 gs
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int r = maxSubArrayBf(new int[] {-2, 1, -3, 4, -1, 2, 1});
    if (r != 6) { // 若 右指针 不等于 6
      System.out.println("FAIL " + r); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
