// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
package com.webfault.dsa; // 引入依赖

class Lc914 { // 定义类型
  static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
  }

  static boolean hasGroupsSizeX(int[] deck) { // 定义函数/方法 hasGroupsSizeX
    java.util.Map<Integer, Integer> count = new java.util.HashMap<>();
    for (int c : deck)
      count.put(
          c,
          count.getOrDefault(c, 0)
              + 1); // for (int 字符 : deck) 计数.put(字符, 计数.getOrDefault(字符, 0) 加 1);
    int n = deck.length; // 把 deck.长度 存入 元素个数
    for (int x = 2; x <= n; x++) { // 让 x 从 2 开始计数，x 不超过 元素个数 就继续
      if (n % x == 0) { // 若 元素个数 对…取模 x 等于 0
        boolean ok = true; // 把 true; 写入 boolean ok
        for (int v : count.values())
          if (v % x != 0) {
            ok = false;
            break;
          }
        if (ok) return true; // 若 ok，直接返回 true
      }
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    java.util.List<Object[]> cases = new java.util.ArrayList<>();
    cases.add(
        new Object[] {
          new int[] {1, 1, 2, 2, 2, 2}, true
        }); // cases 追加 new Object[]{ new int[]{1,1,2,2,2,2}, true });
    cases.add(
        new Object[] {
          new int[] {1, 1, 1, 2, 2, 2, 3, 3}, false
        }); // cases 追加 new Object[]{ new int[]{1,1,1,2,2,2,3,3}, false });
    boolean ok = true; // 把 true; 写入 boolean ok
    for (Object[] c : cases) { // for (Object[] 字符 : cases) {
      int[] deck = (int[]) c[0]; // 把 (int[]) 字符[0]; 写入 int[] deck
      boolean want = (boolean) c[1]; // 把 (boolean) 字符[1]; 写入 boolean want
      boolean got = hasGroupsSizeX(deck); // 把 hasGroupsSizeX(deck); 写入 boolean got
      if (got != want) {
        ok = false;
        System.out.println(
            "FAIL hasGroupsSizeX("
                + java.util.Arrays.toString(deck)
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
