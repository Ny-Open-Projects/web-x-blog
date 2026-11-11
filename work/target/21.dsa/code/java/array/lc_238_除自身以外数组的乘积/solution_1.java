package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Solution { // 定义类型
  static List<Integer> productExceptSelf(int[] nums) { // 定义函数/方法 productExceptSelf
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int[] out = new int[n]; // 把 new int[元素个数]; 写入 int[] out
    Arrays.fill(out, 1); // Arrays.fill(out, 1);
    int p = 1; // 把 1 存入 节点
    for (int i = 0; i < n; i++) {
      out[i] = p;
      p *= nums[i];
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    p = 1; // 把 1; 写入 节点
    for (int i = n - 1; i >= 0; i--) {
      out[i] *= p;
      p *= nums[i];
    } // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    for (int v : out) res.add(v); // for (int 值 : out) 结果 追加 值);
    return res; // 返回 结果
  }

  static boolean eqList(List<Integer> a, List<Integer> b) { // 定义函数/方法 eqList
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (int i = 0; i < a.size(); i++)
      if (!a.get(i).equals(b.get(i))) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] ins = {
      {1, 2, 3, 4}, {0, 0}, {-1, 1, 0, -3, 3}
    }; // 把 {{1,2,3,4}, {0,0}, { 减 1,1,0, 减 3,3}}; 写入 int[][] ins
    int[][] wants = {
      {24, 12, 8, 6}, {0, 0}, {0, 0, 9, 0, 0}
    }; // 把 {{24,12,8,6}, {0,0}, {0,0,9,0,0}}; 写入 int[][] wants
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < ins.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 ins.长度 就继续
      List<Integer> got =
          productExceptSelf(ins[i]); // 把 productExceptSelf(ins[下标 i]); 写入 List<Integer> got
      List<Integer> want = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> want
      for (int v : wants[i]) want.add(v); // for (int 值 : wants[下标 i]) want 追加 值);
      if (!eqList(got, want)) { // 若 取反 eqList(got, want
        System.out.println(
            "FAIL in=" + Arrays.toString(ins[i]) + " want=" + want + " got=" + got); // 打印输出
        ok = false; // 把 false; 写入 ok
      }
    }
    if (!ok) {
      System.out.println("RESULT: FAIL");
      System.exit(1);
    } // 若 取反 ok) { System.out.输出(「RESULT: FAIL」); System.exit(1); }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
