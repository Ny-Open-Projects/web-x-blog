// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc105893757_solution33 { // 定义类型
  // 用递归对栈排序（栈底最小，栈顶最大）
  static void sortedInsert(Deque<Integer> stack, int val) { // 定义函数/方法 sortedInsert
    if (stack.isEmpty() || val > stack.peekLast()) { // 若 栈.isEmpty() 或 值 超过 栈.peekLast(
      stack.addLast(val); // 栈.addLast(值);
    } else { // 否则
      int tmp = stack.removeLast(); // 把 栈.removeLast() 存入 临时变量
      sortedInsert(stack, val); // sortedInsert(栈, 值);
      stack.addLast(tmp); // 栈.addLast(临时变量);
    }
  }

  static void sortStackRecursive(Deque<Integer> stack) { // 定义函数/方法 sortStackRecursive
    if (!stack.isEmpty()) { // 若 取反 栈.isEmpty(
      int top = stack.removeLast(); // 把 栈.removeLast() 存入 top
      sortStackRecursive(stack); // sortStackRecursive(栈);
      sortedInsert(stack, top); // sortedInsert(栈, top);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Deque<Integer> s = new ArrayDeque<>(Arrays.asList(1, 3, 2, 4));
    sortStackRecursive(s); // sortStackRecursive(字符串);
    List<Integer> res = new ArrayList<>(s); // 把 new ArrayList 小于 超过 (字符串); 写入 List<Integer> res
    List<Integer> expect =
        Arrays.asList(1, 2, 3, 4); // 把 Arrays.asList(1, 2, 3, 4); 写入 List<Integer> expect
    if (!res.equals(expect)) { // 若 取反 结果.equals(expect
      System.out.println("FAIL " + res); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
