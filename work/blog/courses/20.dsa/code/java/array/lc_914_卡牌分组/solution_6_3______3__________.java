// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
package com.webfault.dsa; // 引入依赖

class Lc914 { // 定义类型
  static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
  }

  static boolean hasGroupsSizeX(int[] deck) { // 定义函数/方法 hasGroupsSizeX
    if (deck.length < 2) return false; // 若 deck.长度 小于 2，直接返回 false
    int g = 0; // 把 0 存入 g
    java.util.Map<Integer, Integer> count = new java.util.HashMap<>();
    for (int c : deck)
      count.put(
          c,
          count.getOrDefault(c, 0)
              + 1); // for (int 字符 : deck) 计数.put(字符, 计数.getOrDefault(字符, 0) 加 1);
    for (int c : count.values()) g = gcd(g, c); // 把 gcd(g, 字符); 写入 for (int c : count.values()) g
    return g >= 2; // 返回 g 不低于 2
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    java.util.List<Object[]> cases = new java.util.ArrayList<>();
    cases.add(
        new Object[] {
          new int[] {1, 2, 3, 4, 4, 3, 2, 1}, true
        }); // cases 追加 new Object[]{ new int[]{1,2,3,4,4,3,2,1}, true });
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
