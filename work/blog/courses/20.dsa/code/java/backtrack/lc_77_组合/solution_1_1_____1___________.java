// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240015
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Lc77 { // 定义类型
  List<List<Integer>> combine(int n, int k) { // 定义函数/方法 combine
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    backtrack(1, n, k, new ArrayList<Integer>(), result);
    return result; // 返回 结果
  }

  void backtrack(
      int start,
      int n,
      int k,
      List<Integer> path,
      List<List<Integer>> result) { // 定义函数/方法 backtrack
    if (path.size() == k) { // 若 当前路径.大小() 等于 下标 k
      result.add(new ArrayList<Integer>(path)); // 结果 追加 new ArrayList 小于 Integer 超过 (当前路径));
      return; // return;
    }
    for (int i = start; i <= n; i++) { // 让 下标 i 从 起点 开始计数，下标 i 不超过 元素个数 就继续
      path.add(i); // 当前路径 追加 下标 i);
      backtrack(i + 1, n, k, path, result); // backtrack(下标 i 加 1, 元素个数, 下标 k, 当前路径, 结果);
      path.remove(path.size() - 1); // 当前路径 弹出 当前路径.大小() 减 1);
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Lc77 s = new Lc77(); // 把 new Lc77(); 写入 Lc77 s
    boolean ok = true; // 把 true; 写入 boolean ok
    List<List<Integer>> r1 = s.combine(1, 1); // 把 字符串.combine(1, 1); 写入 List<List<Integer>> r1
    if (!(r1.size() == 1 && r1.get(0).equals(Arrays.asList(1)))) {
      ok = false;
      System.out.println("FAIL1 " + r1);
    }
    List<List<Integer>> r2 = s.combine(4, 2); // 把 字符串.combine(4, 2); 写入 List<List<Integer>> r2
    if (r2.size() != 6) {
      ok = false;
      System.out.println("FAIL2 size " + r2.size());
    }
    List<List<Integer>> r3 = s.combine(3, 3); // 把 字符串.combine(3, 3); 写入 List<List<Integer>> r3
    if (!(r3.size() == 1 && r3.get(0).equals(Arrays.asList(1, 2, 3)))) {
      ok = false;
      System.out.println("FAIL3 " + r3);
    }
    List<List<Integer>> r4 = s.combine(2, 1); // 把 字符串.combine(2, 1); 写入 List<List<Integer>> r4
    if (r4.size() != 2) {
      ok = false;
      System.out.println("FAIL4 size " + r4.size());
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
