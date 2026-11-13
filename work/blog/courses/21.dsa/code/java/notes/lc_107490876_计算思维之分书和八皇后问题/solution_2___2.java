// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Main { // 定义类型
  int[][] like = { // 把 { 写入 int[][] like
    {0, 0, 1, 1, 0},
    {1, 1, 0, 0, 1},
    {0, 1, 1, 0, 1},
    {0, 0, 0, 1, 0},
    {0, 1, 0, 0, 1},
  };
  List<int[]> results; // List 小于 int[] 超过 results;

  void tryAssign(int reader, int[] assigned) { // 定义函数/方法 tryAssign
    if (reader == 5) {
      results.add(assigned);
      return;
    } // 若 reader 等于 5) { results 追加 assigned); return; }
    for (int book = 0; book < 5; book++) { // 让 book 从 0 开始计数，book 小于 5 就继续
      if (like[reader][book] == 1
          && assigned[book] == -1) { // 若 like[reader][book] 等于 1 且 assigned[book] 等于 减 1
        int[] nxt = assigned.clone(); // 把 assigned.clone(); 写入 int[] nxt
        nxt[book] = reader; // 把 reader; 写入 nxt[book]
        tryAssign(reader + 1, nxt); // tryAssign(reader 加 1, nxt);
      }
    }
  }

  List<int[]> allocateBooks() { // 定义函数/方法 allocateBooks
    results = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 results
    tryAssign(
        0, new int[] {-1, -1, -1, -1, -1}); // tryAssign(0, new int[]{ 减 1, 减 1, 减 1, 减 1, 减 1});
    return results; // 返回 results
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Main s = new Main(); // 把 new Main(); 写入 Main s
    List<int[]> res = s.allocateBooks(); // 把 字符串.allocateBooks(); 写入 List<int[]> res
    boolean ok = true; // 把 true; 写入 boolean ok
    if (res.size() != 2) {
      ok = false;
      System.out.println("FAIL count=" + res.size());
    }
    Set<String> got = new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 Set<String> got
    for (int[] a : res)
      got.add(Arrays.toString(a)); // for (int[] 数组 : 结果) got 追加 Arrays.toString(数组));
    Set<String> want = new HashSet<>(Arrays.asList("[1, 2, 0, 3, 4]", "[1, 4, 0, 3, 2]"));
    if (!got.equals(want)) {
      ok = false;
      System.out.println("FAIL set=" + got);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
