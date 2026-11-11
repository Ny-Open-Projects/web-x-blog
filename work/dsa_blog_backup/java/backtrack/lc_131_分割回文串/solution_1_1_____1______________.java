// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240399
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc131_solution111 { // 定义类型
  private char[] s; // private char[] 字符串;
  private int n; // private int 元素个数;
  private boolean[][] f; // private boolean[][] f;
  private List<List<String>> ret; // private List 小于 List 小于 String 超过 超过 ret;
  private List<String> ans; // private List 小于 String 超过 答案;

  public List<List<String>> partition(String str) { // 定义函数/方法 partition
    s = str.toCharArray(); // 把 str.toCharArray(); 写入 字符串
    n = s.length; // 把 字符串.长度; 写入 元素个数
    ret = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 ret
    ans = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 答案
    f = new boolean[n][n]; // 把 new boolean[元素个数][元素个数]; 写入 f
    for (int i = n - 1; i >= 0; i--) { // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
      for (int j = i; j < n; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
        f[i][j] = s[i] == s[j] && (j - i < 2 || f[i + 1][j - 1]);
      }
    }
    dfs(0); // dfs(0);
    return ret; // 返回 ret
  }

  private void dfs(int i) { // 定义函数/方法 dfs
    if (i == n) { // 若 下标 i 等于 元素个数
      ret.add(new ArrayList<>(ans)); // ret 追加 new ArrayList 小于 超过 (答案));
      return; // return;
    }
    for (int j = i; j < n; j++) { // 让 下标 j 从 下标 i 开始计数，下标 j 小于 元素个数 就继续
      if (f[i][j]) { // 若 f[下标 i][下标 j]
        ans.add(new String(s, i, j - i + 1)); // 答案 追加 new String(字符串, 下标 i, 下标 j 减 下标 i 加 1));
        dfs(j + 1); // dfs(下标 j 加 1);
        ans.remove(ans.size() - 1); // 答案 弹出 答案.大小() 减 1);
      }
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc131_solution111 inst =
        new lc131_solution111(); // 把 new lc131_solution111(); 写入 lc131_solution111 inst
    List<List<String>> r1 =
        inst.partition("abc"); // 把 inst.partition(「abc」); 写入 List<List<String>> r1
    List<List<String>> w1 = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> w1
    w1.add(Arrays.asList("a", "b", "c")); // w1 追加 Arrays.asList(「数组」, 「数组」, 「数组」));
    List<List<String>> r2 =
        inst.partition("aab"); // 把 inst.partition(「aab」); 写入 List<List<String>> r2
    List<List<String>> w2 = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<String>> w2
    w2.add(Arrays.asList("a", "a", "b")); // w2 追加 Arrays.asList(「数组」, 「数组」, 「数组」));
    w2.add(Arrays.asList("aa", "b")); // w2 追加 Arrays.asList(「aa」, 「aa」));
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!eq(r1, w1)) {
      ok = false;
      System.out.println("FAIL abc got " + r1);
    }
    if (!eq(r2, w2)) {
      ok = false;
      System.out.println("FAIL aab got " + r2);
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }

  private static boolean eq(List<List<String>> a, List<List<String>> b) {
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (int i = 0; i < a.size(); i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
      if (!a.get(i).equals(b.get(i)))
        return false; // 若 取反 数组 查找 下标 i).equals(b 查找 下标 i))，直接返回 false
    }
    return true; // 返回 true
  }
}
