// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
package com.webfault.dsa; // 引入依赖

class Main { // 定义类型
  static int maximumGap(int[] nums) { // 定义函数/方法 maximumGap
    if (nums.length < 2) return 0; // 若 数组.长度 小于 2，直接返回 0
    int minv = nums[0], maxv = nums[0]; // 把 数组[0], 最大值 赋值为 数组[0] 存入 最小值
    for (int v : nums) {
      if (v < minv) minv = v;
      if (v > maxv) maxv = v;
    }
    if (minv == maxv) return 0; // 若 最小值 等于 最大值，直接返回 0
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int bs = (maxv - minv) / (n - 1);
    if (bs < 1) bs = 1; // 把 (最大值 减 最小值) 除以 (元素个数 减 1); if (bs 小于 1) bs 赋值为 1 存入 bs
    int bc = (maxv - minv) / bs + 1; // 把 (最大值 减 最小值) 除以 bs 加 1 存入 bc
    int[] bMin = new int[bc];
    int[] bMax = new int[bc];
    boolean[] has = new boolean[bc];
    for (int v : nums) { // for (int 值 : 数组) {
      int idx = (v - minv) / bs; // 把 (值 减 最小值) 除以 bs 存入 idx
      if (!has[idx]) {
        bMin[idx] = v;
        bMax[idx] = v;
        has[idx] = true;
      } else {
        if (v < bMin[idx]) bMin[idx] = v;
        if (v > bMax[idx]) bMax[idx] = v;
      } // 否则
    }
    int ans = 0, prev = minv; // 把 0, 前一个 赋值为 最小值 存入 答案
    for (int i = 0; i < bc; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 bc 就继续
      if (!has[i]) continue; // 若 取反 has[下标 i]) continue;
      if (bMin[i] - prev > ans)
        ans = bMin[i] - prev; // 若 bMin[下标 i] 减 前一个 超过 答案) 答案 赋值为 bMin[下标 i] 减 前一个;
      prev = bMax[i]; // 把 bMax[下标 i]; 写入 前一个
    }
    return ans; // 返回 答案
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {{3, 6, 9, 1}, {10}, {1, 10000000}};
    int[] ws = {3, 0, 9999999};
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      int got = maximumGap(ins[i]); // 把 maximumGap(ins[下标 i]) 存入 got
      if (got != ws[i]) {
        ok = false;
        System.out.println("FAIL " + got + " want " + ws[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
