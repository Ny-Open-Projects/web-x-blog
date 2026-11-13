// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134379497
package com.webfault.dsa; // 引入依赖

class lc164_solution { // 定义类型
  int maximumGap(int[] nums) { // 定义函数/方法 maximumGap
    int n = nums.length; // 把 数组.长度 存入 元素个数
    if (n < 2) return 0; // 若 元素个数 小于 2，直接返回 0
    int min_val = nums[0], max_val = nums[0]; // 把 数组[0], max_val 赋值为 数组[0] 存入 min_val
    for (int x : nums) {
      if (x < min_val) min_val = x;
      if (x > max_val) max_val = x;
    }
    if (min_val == max_val) return 0; // 若 min_val 等于 max_val，直接返回 0
    int d =
        Math.max(
            1,
            (max_val - min_val)
                / (n - 1)); // 把 Math.取较大值 1, (max_val 减 min_val) 除以 (元素个数 减 1)) 存入 d
    int bucket_size = (max_val - min_val) / d + 1; // 把 (max_val 减 min_val) 除以 d 加 1 存入 bucket_size
    int[][] buckets = new int[bucket_size][2]; // 把 new int[bucket_size][2]; 写入 int[][] buckets
    for (int i = 0; i < bucket_size; i++) {
      buckets[i][0] = -1;
      buckets[i][1] = -1;
    } // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_size 就继续
    for (int x : nums) { // for (int x : 数组) {
      int idx = (x - min_val) / d; // 把 (x 减 min_val) 除以 d 存入 idx
      if (buckets[idx][0] == -1) {
        buckets[idx][0] = x;
        buckets[idx][1] = x;
      } else {
        buckets[idx][0] = Math.min(buckets[idx][0], x);
        buckets[idx][1] = Math.max(buckets[idx][1], x);
      } // 否则
    }
    int max_gap = 0;
    int prev = -1; // 把 0; int 前一个 赋值为 减 1 存入 max_gap
    for (int i = 0; i < bucket_size; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_size 就继续
      if (buckets[i][0] == -1) continue; // 若 buckets[下标 i][0] 等于 减 1) continue;
      if (prev != -1) max_gap = Math.max(max_gap, buckets[i][0] - buckets[prev][1]);
      prev = i; // 把 下标 i; 写入 前一个
    }
    return max_gap; // 返回 max_gap
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc164_solution s = new lc164_solution(); // 把 new lc164_solution(); 写入 lc164_solution s
    int[][][] cases = {
      {{3, 6, 9, 1}}, {{10}}, {{1, 2, 3}}
    }; // 把 {{{3, 6, 9, 1}}, {{10}}, {{1, 2, 3}}}; 写入 int[][][] cases
    int[] wants = {3, 0, 1}; // 把 {3, 0, 1}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < wants.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 wants.长度 就继续
      int got = s.maximumGap(cases[i][0]); // 把 字符串.maximumGap(cases[下标 i][0]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
