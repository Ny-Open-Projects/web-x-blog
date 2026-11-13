// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347105
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc496_solution1 { // 定义类型
  int[] nextGreaterElement(int[] nums1, int[] nums2) { // 定义函数/方法 nextGreaterElement
    Deque<Integer> stack = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> stack
    Map<Integer, Integer> greaterMap =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<Integer, Integer> greaterMap
    for (int num : nums2) { // for (int num : 数组2) {
      while (!stack.isEmpty() && stack.peek() < num) { // 循环，直到不满足「取反 栈.isEmpty() 且 栈.peek() 小于 num」
        greaterMap.put(stack.pop(), num); // 弹出栈顶元素
      }
      stack.push(num); // 把 num 压入栈/数组尾部
    }
    int[] result = new int[nums1.length]; // 把 new int[数组1.长度]; 写入 int[] result
    for (int i = 0; i < nums1.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组1.长度 就继续
      result[i] =
          greaterMap.getOrDefault(
              nums1[i], -1); // 把 greaterMap.getOrDefault(数组1[下标 i], 减 1); 写入 result[i]
    }
    return result; // 返回 结果
  }

  static boolean eqArr(int[] a, int[] b) { // 定义函数/方法 eqArr
    if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (int i = 0; i < a.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i] != b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
    }
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc496_solution1 s = new lc496_solution1(); // 把 new lc496_solution1(); 写入 lc496_solution1 s
    int[][][] inputs = { // 把 { 写入 int[][][] inputs
      {{4, 1, 2}, {1, 3, 4, 2}},
      {{2, 4}, {1, 2, 3, 4}},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {-1, 3, -1},
      {3, -1},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < inputs.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 inputs.长度 就继续
      int[] got = s.nextGreaterElement(inputs[i][0], inputs[i][1]);
      if (!eqArr(got, wants[i])) { // 若 取反 eqArr(got, wants[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL case"
                + i
                + " got="
                + Arrays.toString(got)
                + " want="
                + Arrays.toString(wants[i])); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
