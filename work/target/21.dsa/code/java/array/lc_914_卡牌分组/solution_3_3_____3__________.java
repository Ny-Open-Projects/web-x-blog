// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130450957
package com.webfault.dsa; // 引入依赖

class Lc914 { // 定义类型
  static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
  }

  static boolean hasGroupsSizeX(int[] deck) { // 定义函数/方法 hasGroupsSizeX
    java.util.Map<Integer, Integer> tmp = new java.util.HashMap<>();
    for (int item : deck) tmp.put(item, tmp.getOrDefault(item, 0) + 1);
    java.util.List<Integer> result =
        new java.util.ArrayList<>(new java.util.HashSet<>(tmp.values()));
    while (result.size() > 1) { // 循环，直到不满足「结果.大小() 超过 1」
      int a = result.remove(0); // 把 结果 弹出 0) 存入 数组
      int b = result.remove(0); // 把 结果 弹出 0) 存入 b
      result.add(0, gcd(a, b)); // 结果 追加 0, gcd(数组, b));
    }
    if (result.isEmpty()) return false; // 若 结果.isEmpty()，直接返回 false
    return result.get(0) > 1; // 返回 结果 查找 0) 超过 1
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    java.util.List<Object[]> cases = new java.util.ArrayList<>();
    cases.add(
        new Object[] {
          new int[] {1, 1, 1, 2, 2, 2, 3, 3}, false
        }); // cases 追加 new Object[]{ new int[]{1,1,1,2,2,2,3,3}, false });
    cases.add(
        new Object[] {
          new int[] {1, 2, 3, 4, 4, 3, 2, 1}, true
        }); // cases 追加 new Object[]{ new int[]{1,2,3,4,4,3,2,1}, true });
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
