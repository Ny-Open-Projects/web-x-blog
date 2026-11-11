// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347297
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc503_solution1 { // 定义类型
  static int[] nextGreaterElements(int[] nums) { // 定义函数/方法 nextGreaterElements
    int n = nums.length; // 把 数组.长度 存入 元素个数
    int[] result = new int[n]; // 把 new int[元素个数]; 写入 int[] result
    Arrays.fill(result, -1); // Arrays.fill(结果, 减 1);
    Deque<Integer> stack = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> stack
    for (int i = 0; i < 2 * n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 2 乘 元素个数 就继续
      int num = nums[i % n]; // 把 数组[下标 i 对…取模 元素个数] 存入 num
      while (!stack.isEmpty()
          && nums[stack.peek()] < num) { // 循环，直到不满足「取反 栈.isEmpty() 且 数组[栈.peek()] 小于 num」
        int idx = stack.pop(); // 把 栈 弹出 ) 存入 idx
        result[idx] = num; // 把 num; 写入 result[idx]
      }
      if (i < n) stack.push(i); // 若 下标 i 小于 元素个数) 栈 追加 下标 i);
    }
    return result; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[] r =
        nextGreaterElements(
            new int[] {1, 2, 1}); // 把 nextGreaterElements(new int[]{1, 2, 1}); 写入 int[] r
    if (!Arrays.equals(r, new int[] {2, -1, 2}))
      throw new RuntimeException("FAILED " + Arrays.toString(r));
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
