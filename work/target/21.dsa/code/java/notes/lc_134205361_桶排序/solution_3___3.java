// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lcBucketSort { // 定义类型
  int[] bucketSort(int[] lst, int n) { // 定义函数/方法 bucketSort
    if (lst.length < 2) { // 若 lst.长度 小于 2
      int[] r = new int[lst.length]; // 把 new int[lst.长度]; 写入 int[] r
      for (int i = 0; i < lst.length; i++) r[i] = lst[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 lst.长度 就继续
      return r; // 返回 右指针
    }
    int min_val = lst[0], max_val = lst[0]; // 把 lst[0], max_val 赋值为 lst[0] 存入 min_val
    for (int x : lst) {
      if (x < min_val) min_val = x;
      if (x > max_val) max_val = x;
    }
    int dist = max_val - min_val; // 把 max_val 减 min_val 存入 dist
    if (dist == 0) {
      int[] r = new int[lst.length];
      for (int i = 0; i < lst.length; i++) r[i] = lst[i];
      return r;
    }
    ArrayList<ArrayList<Integer>> buckets = new ArrayList<>();
    for (int i = 0; i < n; i++) buckets.add(new ArrayList<>()); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    int width = (dist + 1) / n; // 把 (dist 加 1) 除以 元素个数 存入 width
    for (int current : lst) { // for (int current : lst) {
      int index = (current - min_val) / width; // 把 (current 减 min_val) 除以 width 存入 index
      if (index >= n) index = n - 1; // 若 index 不低于 元素个数) index 赋值为 元素个数 减 1;
      buckets.get(index).add(current); // buckets 查找 index) 追加 current);
    }
    for (ArrayList<Integer> b : buckets) Collections.sort(b); // 排序
    ArrayList<Integer> result =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> result
    for (ArrayList<Integer> b : buckets) for (int item : b) result.add(item);
    int[] out = new int[result.size()]; // 把 new int[结果.大小()]; 写入 int[] out
    for (int i = 0; i < result.size(); i++)
      out[i] = result.get(i); // 让 下标 i 从 0 开始计数，下标 i 小于 结果.大小() 就继续
    return out; // 返回 out
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lcBucketSort s = new lcBucketSort(); // 把 new lcBucketSort(); 写入 lcBucketSort s
    int[][][] cases = { // 把 { 写入 int[][][] cases
      {{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}},
      {{5, 4, 3, 2, 1}},
      {{}},
      {{1}},
      {{-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20}}
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9},
      {1, 2, 3, 4, 5},
      {},
      {1},
      {-100, -30, -20, -9, -2, 0, 0, 1, 1, 1, 3, 3, 4, 5, 9, 9, 20, 88, 88, 99, 100}
    };
    int[] ns = {5, 5, 5, 5, 5}; // 把 {5, 5, 5, 5, 5}; 写入 int[] ns
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < cases.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
      int[] got =
          s.bucketSort(
              cases[i][0], ns[i]); // 把 字符串.bucketSort(cases[下标 i][0], ns[下标 i]); 写入 int[] got
      if (got.length != wants[i].length) {
        ok = false;
        System.out.println("FAIL len " + i);
        continue;
      }
      for (int j = 0; j < got.length; j++)
        if (got[j] != wants[i][j]) {
          ok = false;
          System.out.println(
              "FAIL case " + i + " idx " + j + " got " + got[j] + " want " + wants[i][j]);
        } // 让 下标 j 从 0 开始计数，下标 j 小于 got.长度 就继续
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
