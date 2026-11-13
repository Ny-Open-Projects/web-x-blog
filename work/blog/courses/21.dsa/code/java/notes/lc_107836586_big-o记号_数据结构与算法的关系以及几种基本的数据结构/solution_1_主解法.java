// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
package com.webfault.dsa; // 引入依赖

class lc107836586_solution1 { // 定义类型
  // 给定各次项系数（索引为次数），返回最高次非零项对应的 Big-O 记号。
  String classify(int[] coeffs) { // 定义函数/方法 classify
    for (int deg = coeffs.length - 1; deg >= 0; deg--) { // 让 deg 从 coeffs.长度 减 1 开始计数，deg 不低于 0 就继续
      if (coeffs[deg] != 0) { // 若 coeffs[deg] 不等于 0
        if (deg > 1)
          return "O(n^" + deg + ")"; // 若 deg 超过 1，直接返回 「O(元素个数 按位异或 」 加 deg 加 「O(元素个数 按位异或 」
        if (deg == 1) return "O(n)"; // 若 deg 等于 1，直接返回 「O(元素个数)」
        return "O(1)"; // 返回 「O(1)」
      }
    }
    return "O(1)"; // 返回 「O(1)」
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc107836586_solution1 s =
        new lc107836586_solution1(); // 把 new lc107836586_solution1(); 写入 lc107836586_solution1 s
    String[][] cases = { // 把 { 写入 String[][] cases
      {s.classify(new int[] {6, 20, 30, 35}), "O(n^3)"},
      {s.classify(new int[] {5}), "O(1)"},
      {s.classify(new int[] {0, 5}), "O(n)"},
      {s.classify(new int[] {0, 0, 7}), "O(n^2)"},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (String[] c : cases) { // for (String[] 字符 : cases) {
      if (!c[0].equals(c[1])) { // 若 取反 字符[0].equals(字符[1]
        ok = false; // 把 false; 写入 ok
        System.out.println("FAIL classify=" + c[0] + " want " + c[1]); // 打印输出
      }
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
