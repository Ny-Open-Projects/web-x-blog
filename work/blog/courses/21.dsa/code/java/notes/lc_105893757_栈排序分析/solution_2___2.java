// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc105893757_solution22 { // 定义类型
  // 用两个栈对栈排序（升序，栈顶最大）
  static List<Integer> sortStackTwoStacks(List<Integer> stack) { // 定义函数/方法 sortStackTwoStacks
    Deque<Integer> st = new ArrayDeque<>(stack); // 把 new ArrayDeque 小于 超过 (栈); 写入 Deque<Integer> st
    Deque<Integer> aux = new ArrayDeque<>(); // 把 new ArrayDeque 小于 超过 (); 写入 Deque<Integer> aux
    while (!st.isEmpty()) { // 循环，直到不满足「取反 st.isEmpty(」
      int top = st.removeLast(); // 把 st.removeLast() 存入 top
      while (!aux.isEmpty()
          && aux.peekLast() > top) { // 循环，直到不满足「取反 aux.isEmpty() 且 aux.peekLast() 超过 top」
        st.addLast(aux.removeLast()); // st.addLast(aux.removeLast());
      }
      aux.addLast(top); // aux.addLast(top);
    }
    return new ArrayList<>(aux); // 返回 new ArrayList 小于 超过 (aux)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<Integer> res = sortStackTwoStacks(Arrays.asList(1, 3, 2, 4));
    List<Integer> expect =
        Arrays.asList(1, 2, 3, 4); // 把 Arrays.asList(1, 2, 3, 4); 写入 List<Integer> expect
    if (!res.equals(expect)) { // 若 取反 结果.equals(expect
      System.out.println("FAIL " + res); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
