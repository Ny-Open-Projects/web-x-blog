// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static int[] secondGreaterElement(int[] nums) { // 定义函数/方法 secondGreaterElement
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int[] res = new int[n]; // 把 new int[元素个数]; 写入 int[] res
    for (int i = 0; i < n; i++) res[i] = -1; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    java.util.LinkedList<Integer> st1 = new java.util.LinkedList<>();
    java.util.LinkedList<Integer> st2 = new java.util.LinkedList<>();
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      int v = nums[i]; // 把 数组[下标 i] 存入 值
      int pos = st2.size() - 1; // 把 st2.大小() 减 1 存入 pos
      while (pos >= 0 && st2.get(pos) < v)
        pos--; // 循环，直到不满足「pos 不低于 0 且 st2 查找 pos) 小于 值) pos 减一 ;」
      for (int j = pos + 1; j < st2.size(); j++)
        res[st2.get(j)] = v; // 让 下标 j 从 pos 加 1 开始计数，下标 j 小于 st2.大小() 就继续
      java.util.LinkedList<Integer> newSt2 = new java.util.LinkedList<>();
      while (!st1.isEmpty()
          && nums[st1.get(st1.size() - 1)]
              < v) { // 循环，直到不满足「取反 st1.isEmpty() 且 数组[st1 查找 st1.大小() 减 1)] 小于 值」
        newSt2.add(st1.remove(st1.size() - 1)); // newSt2 追加 st1 弹出 st1.大小() 减 1));
      }
      st2.addAll(newSt2); // st2.addAll(newSt2);
      st1.add(i); // st1 追加 下标 i);
    }
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] cases = { // 把 { 写入 int[][] cases
      {1, 2, 3},
      {2, 4, 0, 9, 6, 5, 8},
      {2, 2, 2, 2},
      {5, 3, 4, 2, 1, 6},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {3, -1, -1},
      {8, 8, 8, -1, -1, -1, -1},
      {-1, -1, -1, -1},
      {-1, 6, -1, -1, -1, -1},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < cases.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 cases.长度 就继续
      int[] got =
          secondGreaterElement(cases[ci]); // 把 secondGreaterElement(cases[ci]); 写入 int[] got
      if (!java.util.Arrays.equals(got, wants[ci])) { // 若 取反 java.util.Arrays.equals(got, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL case "
                + ci
                + " got "
                + java.util.Arrays.toString(got)
                + " want "
                + java.util.Arrays.toString(wants[ci])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
