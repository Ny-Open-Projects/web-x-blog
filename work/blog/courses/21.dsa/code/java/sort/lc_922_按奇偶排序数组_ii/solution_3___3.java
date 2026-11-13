// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  static int[] sortArrayByParityII(int[] nums) { // 定义函数/方法 sortArrayByParityII
    int n = nums.length;
    int[] res = new int[n];
    int e = 0, o = 1;
    for (int v : nums) {
      if (v % 2 == 0) {
        res[e] = v;
        e += 2;
      } else {
        res[o] = v;
        o += 2;
      }
    }
    return res; // 返回 结果
  }

  static boolean validParity(int[] a, int[] src) { // 定义函数/方法 validParity
    if (a.length != src.length) return false; // 若 数组.长度 不等于 src.长度，直接返回 false
    Map<Integer, Integer> ca = new HashMap<>(), cb = new HashMap<>();
    for (int v : a)
      ca.put(v, ca.getOrDefault(v, 0) + 1); // for (int 值 : 数组) ca.put(值, ca.getOrDefault(值,0) 加 1);
    for (int v : src)
      cb.put(
          v, cb.getOrDefault(v, 0) + 1); // for (int 值 : src) cb.put(值, cb.getOrDefault(值,0) 加 1);
    if (!ca.equals(cb)) return false; // 若 取反 ca.equals(cb)，直接返回 false
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (i % 2 == 0 && a[i] % 2 != 0)
        return false; // 若 下标 i 对…取模 2 等于 0 且 数组[下标 i] 对…取模 2 不等于 0，直接返回 false
      if (i % 2 == 1 && a[i] % 2 == 0)
        return false; // 若 下标 i 对…取模 2 等于 1 且 数组[下标 i] 对…取模 2 等于 0，直接返回 false
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {
      {4, 2, 5, 7}, {2, 3}, {1, 2, 3, 4}
    }; // 把 {{4,2,5,7},{2,3},{1,2,3,4}}; 写入 int[][] ins
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int[] c : ins) {
      if (!validParity(sortArrayByParityII(c), c)) {
        ok = false;
        System.out.println("FAIL " + Arrays.toString(c));
      }
    } // 打印输出
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
