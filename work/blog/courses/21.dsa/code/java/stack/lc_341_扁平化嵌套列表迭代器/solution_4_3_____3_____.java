// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345560
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc341_solution433 { // 定义类型
  static List<Integer> flatArray(List<Integer> arr) { // 定义函数/方法 flatArray
    Deque<Integer> stack = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> stack
    for (int i = arr.size() - 1; i >= 0; i--)
      stack.push(arr.get(i)); // 让 下标 i 从 数组.大小() 减 1 开始计数，下标 i 不低于 0 就继续
    List<Integer> ret = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> ret
    while (!stack.isEmpty()) ret.add(stack.pop()); // 循环，直到不满足「取反 栈.isEmpty()) ret 追加 栈 弹出 ));」
    return ret; // 返回 ret
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<Integer> out =
        flatArray(
            Arrays.asList(1, 2, 3)); // 把 flatArray(Arrays.asList(1, 2, 3)); 写入 List<Integer> out
    if (!out.equals(Arrays.asList(1, 2, 3))) throw new RuntimeException("FAILED " + out);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
