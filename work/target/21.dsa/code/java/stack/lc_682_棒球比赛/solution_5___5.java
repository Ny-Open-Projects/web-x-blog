// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
package com.webfault.dsa; // 引入依赖

class Lc682 { // 定义类型
  int calPoints(String[] operations) { // 定义函数/方法 calPoints
    java.util.ArrayList<Integer> stack = new java.util.ArrayList<Integer>();
    for (String op : operations) { // for (String op : operations) {
      if (op.equals("C")) { // 若 op.equals(「C」
        stack.remove(stack.size() - 1); // 栈 弹出 栈.大小() 减 1);
      } else if (op.equals("D")) { // 否则，若 op.equals(「D」
        stack.add(stack.get(stack.size() - 1) * 2); // 栈 追加 栈 查找 栈.大小() 减 1) 乘 2);
      } else if (op.equals("+")) { // 否则，若 op.equals(「 加 」
        int n = stack.size(); // 把 栈.大小() 存入 元素个数
        stack.add(stack.get(n - 1) + stack.get(n - 2)); // 栈 追加 栈 查找 元素个数 减 1) 加 栈 查找 元素个数 减 2));
      } else { // 否则
        stack.add(Integer.parseInt(op)); // 栈 追加 Integer.转整数(op));
      }
    }
    int sum = 0; // 把 0 存入 累计和
    for (int v : stack) sum += v; // 把 值; 写入 for (int v : stack) sum +
    return sum; // 返回 累计和
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc682 s = new Lc682(); // 把 new Lc682(); 写入 Lc682 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (s.calPoints(new String[] {"5", "2", "C", "D", "+"}) != 30) {
      ok = false;
      System.out.println("FAIL1");
    }
    if (s.calPoints(new String[] {"5", "-2", "4", "C", "D", "9", "+", "+"}) != 27) {
      ok = false;
      System.out.println("FAIL2");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
