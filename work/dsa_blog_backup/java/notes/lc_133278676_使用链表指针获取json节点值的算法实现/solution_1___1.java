// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖
import java.util.LinkedHashMap; // 引入依赖
import java.util.List; // 引入依赖
import java.util.Map; // 引入依赖

/** 忠实翻译 python/notes/lc_133278676_.../solution_1___1.py 方案1：使用指针（游标）逐层下钻，键缺失或节点非 Map 时返回 null。 */
class Lc133278676S1 { // 定义类型
  @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
  static Object getValue(Object data, List<String> path) { // 定义函数/方法 getValue
    Object node = data; // 把 data; 写入 Object node
    for (String key : path) { // for (String key : 当前路径) {
      if (!(node instanceof Map) || !((Map<String, Object>) node).containsKey(key)) {
        return null; // 返回 null
      }
      node =
          ((Map<String, Object>) node)
              .get(key); // 把 ((Map 小于 String, Object 超过 ) 节点) 查找 key); 写入 节点
    }
    return node; // 返回 节点
  }

  static Map<String, Object> buildData() { // static Map 小于 String, Object 超过 buildData() {
    Map<String, Object> c =
        new LinkedHashMap<>(); // 把 new LinkedHashMap 小于 超过 (); 写入 Map<String, Object> c
    c.put("c", 1); // 字符.put(「字符」, 1);
    Map<String, Object> b =
        new LinkedHashMap<>(); // 把 new LinkedHashMap 小于 超过 (); 写入 Map<String, Object> b
    b.put("b", c); // b.put(「b」, 字符);
    Map<String, Object> d =
        new LinkedHashMap<>(); // 把 new LinkedHashMap 小于 超过 (); 写入 Map<String, Object> d
    d.put("e", 2); // d.put(「e」, 2);
    Map<String, Object> data =
        new LinkedHashMap<>(); // 把 new LinkedHashMap 小于 超过 (); 写入 Map<String, Object> data
    data.put("a", b); // data.put(「数组」, b);
    data.put("d", d); // data.put(「d」, d);
    return data; // 返回 data
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Map<String, Object> data = buildData(); // 把 buildData(); 写入 Map<String, Object> data
    Object v1 = getValue(data, Arrays.asList("a", "b", "c"));
    Object v2 =
        getValue(
            data,
            Arrays.asList("d", "e")); // 把 getValue(data, Arrays.asList(「d」, 「d」)); 写入 Object v2
    Object v3 =
        getValue(
            data,
            Arrays.asList("a", "x")); // 把 getValue(data, Arrays.asList(「数组」, 「数组」)); 写入 Object v3
    boolean ok =
        Integer.valueOf(1).equals(v1) // 把 Integer.valueOf(1).equals(v1) 写入 boolean ok
            && Integer.valueOf(2).equals(v2) // 且 Integer.valueOf(2).equals(v2)
            && v3 == null; // 把 赋值为 null; 写入 && v3
    if (!ok) { // 若 取反 ok
      System.out.println("FAIL got " + v1 + " " + v2 + " " + v3 + " want 1 2 null"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
