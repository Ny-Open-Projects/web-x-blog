// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
package com.webfault.dsa; // 引入依赖

class Lc621 { // 定义类型
  static int leastInterval(String[] tasks, int n) { // 定义函数/方法 leastInterval
    int[] freq = new int[26]; // 把 new int[26]; 写入 int[] freq
    for (String t : tasks) freq[t.charAt(0) - 'A']++; // 逐字符处理
    int maxFreq = 0; // 把 0 存入 maxFreq
    for (int f : freq)
      if (f > maxFreq) maxFreq = f; // 把 f; 写入 for (int f : freq) if (f > maxFreq) maxFreq
    int same = 0; // 把 0 存入 same
    for (int f : freq)
      if (f == maxFreq) same++; // 把 赋值为 maxFreq) same 加一 ; 写入 for (int f : freq) if (f
    return Math.max(
        (maxFreq - 1) * (n + 1) + same,
        tasks.length); // 返回 Math.取较大值 (maxFreq 减 1) 乘 (元素个数 加 1) 加 same, tasks.长度)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    String[][][] cases = { // 把 { 写入 String[][][] cases
      {{"A", "A", "A", "B", "B", "B"}, {"2"}, {"8"}},
      {{"A", "A", "A", "B", "B", "B", "B"}, {"3"}, {"13"}},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (String[][] c : cases) { // for (String[][] 字符 : cases) {
      String[] tasks = c[0]; // 把 字符[0]; 写入 String[] tasks
      int n = Integer.parseInt(c[1][0]); // 把 Integer.转整数(字符[1][0]) 存入 元素个数
      int want = Integer.parseInt(c[2][0]); // 把 Integer.转整数(字符[2][0]) 存入 want
      int got = leastInterval(tasks, n); // 把 leastInterval(tasks, 元素个数) 存入 got
      if (got != want) {
        ok = false;
        System.out.println(
            "FAIL leastInterval("
                + java.util.Arrays.toString(tasks)
                + ","
                + n
                + ")="
                + got
                + " want "
                + want);
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
