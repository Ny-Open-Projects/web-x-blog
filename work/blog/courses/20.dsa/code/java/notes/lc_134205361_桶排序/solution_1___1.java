// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lcBucketGet { // 定义类型
  int getIndex(int[] arr, int k) { // 定义函数/方法 getIndex
    if (arr.length == 0) return -1; // 若 数组.长度 等于 0，直接返回 减 1
    int min_val = arr[0], max_val = arr[0]; // 把 数组[0], max_val 赋值为 数组[0] 存入 min_val
    for (int x : arr) {
      if (x < min_val) min_val = x;
      if (x > max_val) max_val = x;
    }
    int bucket_size = Math.max(1, (max_val - min_val) / arr.length + 1);
    int bucket_count =
        (max_val - min_val) / bucket_size
            + 1; // 把 (max_val 减 min_val) 除以 bucket_size 加 1 存入 bucket_count
    ArrayList<ArrayList<Integer>> buckets = new ArrayList<>();
    for (int i = 0; i < bucket_count; i++)
      buckets.add(new ArrayList<>()); // 让 下标 i 从 0 开始计数，下标 i 小于 bucket_count 就继续
    for (int num : arr) { // for (int num : 数组) {
      int idx = (num - min_val) / bucket_size; // 把 (num 减 min_val) 除以 bucket_size 存入 idx
      buckets.get(idx).add(num); // buckets 查找 idx) 追加 num);
    }
    for (ArrayList<Integer> b : buckets) Collections.sort(b); // 排序
    for (ArrayList<Integer> b : buckets) { // for (ArrayList 小于 Integer 超过 b : buckets) {
      for (int num : b) { // for (int num : b) {
        k -= 1; // 下标 k累减 1
        if (k == 0) return num; // 若 下标 k 等于 0，直接返回 num
      }
    }
    return -1; // 返回 减 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lcBucketGet s = new lcBucketGet(); // 把 new lcBucketGet(); 写入 lcBucketGet s
    int[][][] cases = {{{1, 2, 3}}, {{3, 1, 2}}, {{5, 3, 1, 2, 4}}};
    int[] ks = {1, 2, 3}; // 把 {1, 2, 3}; 写入 int[] ks
    int[] wants = {1, 2, 3}; // 把 {1, 2, 3}; 写入 int[] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < wants.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 wants.长度 就继续
      int got = s.getIndex(cases[i][0], ks[i]); // 把 字符串.getIndex(cases[下标 i][0], ks[下标 i]) 存入 got
      if (got != wants[i]) {
        ok = false;
        System.out.println("FAIL case " + i + " got " + got + " want " + wants[i]);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
