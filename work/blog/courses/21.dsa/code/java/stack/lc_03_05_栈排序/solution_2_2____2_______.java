// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
package com.webfault.dsa; // 引入依赖

class lc03_solution222 { // 定义类型
  static class SortedStack { // static class SortedStack {
    java.util.List<Integer> stk = new java.util.ArrayList<>();

    void push(int val) { // 定义函数/方法 push
      java.util.List<Integer> temp = new java.util.ArrayList<>();
      while (!stk.isEmpty()
          && stk.get(stk.size() - 1) > val) { // 循环，直到不满足「取反 栈.isEmpty() 且 栈 查找 栈.大小() 减 1) 超过 值」
        temp.add(stk.remove(stk.size() - 1)); // 临时变量 追加 栈 弹出 栈.大小() 减 1));
      }
      stk.add(val); // 栈 追加 值);
      while (!temp.isEmpty()) { // 循环，直到不满足「取反 临时变量.isEmpty(」
        stk.add(temp.remove(temp.size() - 1)); // 栈 追加 临时变量 弹出 临时变量.大小() 减 1));
      }
    }

    void pop() { // 定义函数/方法 pop
      if (!isEmpty()) stk.remove(stk.size() - 1); // 若 取反 isEmpty()) 栈 弹出 栈.大小() 减 1);
    }

    int peek() { // 定义函数/方法 peek
      if (isEmpty()) return -1; // 若 isEmpty()，直接返回 减 1
      return stk.get(stk.size() - 1); // 返回 栈 查找 栈.大小() 减 1)
    }

    boolean isEmpty() { // 定义判定函数 isEmpty
      return stk.isEmpty(); // 返回 栈.isEmpty()
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    SortedStack s = new SortedStack(); // 把 new SortedStack(); 写入 SortedStack s
    int[] in = {4, 2, 5, 1, 3}; // 把 {4, 2, 5, 1, 3}; 写入 int[] in
    for (int v : in) s.push(v); // 把 值 压入栈/数组尾部
    int[] want = {5, 4, 3, 2, 1}; // 把 {5, 4, 3, 2, 1}; 写入 int[] want
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int i = 0; i < want.length; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 want.长度 就继续
      int got = s.peek(); // 把 字符串.peek() 存入 got
      if (got != want[i]) { // 若 got 不等于 want[下标 i]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL step " + i + " got " + got + " want " + want[i]); // 打印输出
      }
      s.pop(); // 弹出栈顶元素
    }
    if (!s.isEmpty()) { // 若 取反 字符串.isEmpty(
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL stack not empty after pops"); // 打印输出
    }
    SortedStack e = new SortedStack(); // 把 new SortedStack(); 写入 SortedStack e
    if (e.peek() != -1) { // 若 e.peek() 不等于 减 1
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL empty peek want -1 got " + e.peek()); // 打印输出
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
