// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc105893757_solution11 { // 定义类型
  // 有序栈：push 时借助辅助栈把元素插入到正确位置，使栈底->栈顶升序（栈顶最小）
  static class SortedStack { // static class SortedStack {
    ArrayList<Integer> data =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> data

    void push(int val) { // 定义函数/方法 push
      ArrayList<Integer> temp =
          new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> temp
      while (!data.isEmpty()
          && data.get(data.size() - 1)
              < val) { // 循环，直到不满足「取反 data.isEmpty() 且 data 查找 data.大小() 减 1) 小于 值」
        temp.add(data.remove(data.size() - 1)); // 临时变量 追加 data 弹出 data.大小() 减 1));
      }
      data.add(val); // data 追加 值);
      while (!temp.isEmpty()) { // 循环，直到不满足「取反 临时变量.isEmpty(」
        data.add(temp.remove(temp.size() - 1)); // data 追加 临时变量 弹出 临时变量.大小() 减 1));
      }
    }

    int pop() { // 定义函数/方法 pop
      return data.remove(data.size() - 1); // 返回 data 弹出 data.大小() 减 1)
    }

    boolean isEmpty() { // 定义判定函数 isEmpty
      return data.isEmpty(); // 返回 data.isEmpty()
    }

    ArrayList<Integer> sort() { // 定义函数/方法 sort
      ArrayList<Integer> c =
          new ArrayList<>(data); // 把 new ArrayList 小于 超过 (data); 写入 ArrayList<Integer> c
      Collections.sort(c); // 排序
      return c; // 返回 字符
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    SortedStack st = new SortedStack(); // 把 new SortedStack(); 写入 SortedStack st
    for (int v : new int[] {1, 3, 2, 4}) st.push(v); // 把 值 压入栈/数组尾部
    ArrayList<Integer> srt = st.sort(); // 排序
    ArrayList<Integer> popped =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ArrayList<Integer> popped
    while (!st.isEmpty()) popped.add(st.pop()); // 循环，直到不满足「取反 st.isEmpty()) popped 追加 st 弹出 ));」
    List<Integer> expect =
        Arrays.asList(1, 2, 3, 4); // 把 Arrays.asList(1, 2, 3, 4); 写入 List<Integer> expect
    if (!srt.equals(expect)) { // 若 取反 srt.equals(expect
      System.out.println("FAIL sort " + srt); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    if (!popped.equals(expect)) { // 若 取反 popped.equals(expect
      System.out.println("FAIL pop " + popped); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
