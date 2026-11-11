// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc105893757_solution44 { // 定义类型
  // 用“反复取最小值”的方式对栈排序（选择排序思想），得到升序列表
  static int getMin(Deque<Integer> stack) { // 定义函数/方法 getMin
    if (stack.size() == 1) return stack.removeLast(); // 若 栈.大小() 等于 1，直接返回 栈.removeLast()
    int top = stack.removeLast(); // 把 栈.removeLast() 存入 top
    int restMin = getMin(stack); // 把 getMin(栈) 存入 restMin
    if (top < restMin) { // 若 top 小于 restMin
      stack.addLast(restMin); // 栈.addLast(restMin);
      return top; // 返回 top
    } else { // 否则
      stack.addLast(top); // 栈.addLast(top);
      return restMin; // 返回 restMin
    }
  }

  static List<Integer> sortStackMin(List<Integer> input) { // 定义函数/方法 sortStackMin
    Deque<Integer> stack =
        new ArrayDeque<>(input); // 把 new ArrayDeque 小于 超过 (input); 写入 Deque<Integer> stack
    List<Integer> res = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> res
    while (!stack.isEmpty()) res.add(getMin(stack)); // 循环，直到不满足「取反 栈.isEmpty()) 结果 追加 getMin(栈));」
    return res; // 返回 结果
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<Integer> res = sortStackMin(Arrays.asList(3, 1, 4, 2));
    List<Integer> expect =
        Arrays.asList(1, 2, 3, 4); // 把 Arrays.asList(1, 2, 3, 4); 写入 List<Integer> expect
    if (!res.equals(expect)) { // 若 取反 结果.equals(expect
      System.out.println("FAIL " + res); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
