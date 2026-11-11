// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型

  static int[] secondGreaterElement(int[] nums) { // 定义函数/方法 secondGreaterElement
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int[] res = new int[n]; // 把 new int[元素个数]; 写入 int[] res
    for (int i = 0; i < n; i++) res[i] = -1; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    java.util.LinkedList<Integer> stack = new java.util.LinkedList<>();
    java.util.ArrayList<int[]> pq = new java.util.ArrayList<>();
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      while (!pq.isEmpty()
          && pq.get(0)[0] < nums[i]) { // 循环，直到不满足「取反 优先队列.isEmpty() 且 优先队列 查找 0)[0] 小于 数组[下标 i]」
        int[] e = pq.remove(0); // 把 优先队列 弹出 0); 写入 int[] e
        res[e[1]] = nums[i]; // 把 数组[下标 i]; 写入 res[e[1]]
      }
      while (!stack.isEmpty()
          && nums[stack.get(stack.size() - 1)]
              < nums[i]) { // 循环，直到不满足「取反 栈.isEmpty() 且 数组[栈 查找 栈.大小() 减 1)] 小于 数组[下标 i]」
        int idx = stack.remove(stack.size() - 1); // 把 栈 弹出 栈.大小() 减 1) 存入 idx
        pq.add(new int[] {nums[idx], idx}); // 优先队列 追加 new int[]{数组[idx], idx});
        pq.sort((a, b) -> Integer.compare(a[0], b[0])); // 排序
      }
      stack.add(i); // 栈 追加 下标 i);
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
      {9, 6, 6, -1, -1, -1, -1},
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
