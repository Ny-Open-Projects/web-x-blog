// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc112548608_solution11 { // 定义类型
  static boolean invalid(int[] st) { // 定义函数/方法 invalid
    int h = st[0],
        s = st[2],
        w = st[1],
        v = st[3]; // 把 st[0], 字符串 赋值为 st[2], 权重 赋值为 st[1], 值 赋值为 st[3] 存入 h
    if (h != s && s == w) return true; // 若 h 不等于 字符串 且 字符串 等于 权重，直接返回 true
    if (h != s && s == v) return true; // 若 h 不等于 字符串 且 字符串 等于 值，直接返回 true
    return false; // 返回 false
  }

  static Map<String, Integer> itemIndex = new HashMap<>();
  static List<String> path =
      new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 static List<String> path
  static Set<String> visited =
      new HashSet<>(); // 把 new HashSet 小于 超过 (); 写入 static Set<String> visited

  static boolean go(int[] st) { // 定义函数/方法 go
    if (st[0] == 1 && st[1] == 1 && st[2] == 1 && st[3] == 1) return true;
    String key =
        st[0] + "," + st[1] + "," + st[2] + ","
            + st[3]; // 把 st[0] 加 「,」 加 st[1] 加 「,」 加 st[2] 加 「,」 加 st[3] 存入 key
    if (visited.contains(key)) return false; // 若 已访问集合 是否包含 key)，直接返回 false
    visited.add(key); // 已访问集合 追加 key);
    for (String role : new String[] {"-", "W", "S", "V"}) {
      int[] ns = st.clone(); // 把 st.clone(); 写入 int[] ns
      ns[0] = 1 - ns[0]; // 把 1 减 ns[0]; 写入 ns[0]
      if (!role.equals("-")) { // 若 取反 role.equals(「 减 」
        int idx = itemIndex.get(role); // 把 itemIndex 查找 role) 存入 idx
        if (st[0] != st[idx]) continue; // 若 st[0] 不等于 st[idx]) continue;
        ns[idx] = 1 - ns[idx]; // 把 1 减 ns[idx]; 写入 ns[idx]
      }
      if (invalid(ns)) continue; // 若 invalid(ns)) continue;
      if (go(ns)) { // 若 go(ns
        path.add(role); // 当前路径 追加 role);
        return true; // 返回 true
      }
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    itemIndex.put("W", 1); // itemIndex.put(「W」, 1);
    itemIndex.put("S", 2); // itemIndex.put(「S」, 2);
    itemIndex.put("V", 3); // itemIndex.put(「V」, 3);
    go(new int[] {0, 0, 0, 0}); // go(new int[]{0, 0, 0, 0});
    Collections.reverse(path); // 反转
    List<String> steps = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<String> steps
    for (String r : path) steps.add("H" + (r.equals("-") ? "" : r));
    String plan = String.join(" ", steps); // 把 String.join(「 」, steps) 存入 plan
    if (!plan.equals("HS H HW HS HV H HS")) { // 若 取反 plan.equals(「HS H HW HS HV H HS」
      System.out.println("FAIL " + plan); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
