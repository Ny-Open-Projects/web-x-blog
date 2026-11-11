// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
package com.webfault.dsa; // 引入依赖

class lc110240695_solution44 { // 定义类型
  // Kadane 线性扫描 O(n)
  static int maxSubArray(int[] arr) { // 定义函数/方法 maxSubArray
    if (arr.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    int maxSum = arr[0]; // 把 数组[0] 存入 maxSum
    int cur = arr[0]; // 把 数组[0] 存入 当前值
    for (int i = 1; i < arr.length; i++) { // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
      cur = Math.max(arr[i], cur + arr[i]); // 把 Math.取较大值 数组[下标 i], 当前值 加 数组[下标 i]); 写入 当前值
      maxSum = Math.max(maxSum, cur); // 把 Math.取较大值 maxSum, 当前值); 写入 maxSum
    }
    return maxSum; // 返回 maxSum
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int r =
        maxSubArray(
            new int[] {
              -2, 1, -3, 4, -1, 2, 1
            }); // 把 maxSubArray(new int[]{ 减 2, 1, 减 3, 4, 减 1, 2, 1}) 存入 右指针
    if (r != 6) { // 若 右指针 不等于 6
      System.out.println("FAIL " + r); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
