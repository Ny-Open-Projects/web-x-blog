// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖
import java.util.LinkedHashMap; // 引入依赖
import java.util.List; // 引入依赖
import java.util.Map; // 引入依赖

/** 忠实翻译 python/notes/lc_133278676_.../solution_2___2.py 方案2：直接逐层取值；键缺失时抛错（对应 python 的 KeyError）。 */
class Lc133278676S2 { // 定义类型
  @SuppressWarnings("unchecked") // @SuppressWarnings(「unchecked」)
  static Object getValue(Map<String, Object> data, List<String> path) { // 定义函数/方法 getValue
    Object result = data; // 把 data; 写入 Object result
    for (String k : path) { // for (String 下标 k : 当前路径) {
      if (!(result instanceof Map) || !((Map<String, Object>) result).containsKey(k)) {
        throw new RuntimeException(
            "KeyError: " + k); // throw new RuntimeException(「KeyError: 」 加 下标 k);
      }
      result =
          ((Map<String, Object>) result)
              .get(k); // 把 ((Map 小于 String, Object 超过 ) 结果) 查找 下标 k); 写入 结果
    }
    return result; // 返回 结果
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
    boolean threw = false; // 把 false; 写入 boolean threw
    try { // try {
      getValue(data, Arrays.asList("a", "x")); // getValue(data, Arrays.asList(「数组」, 「数组」));
    } catch (RuntimeException ex) { // } catch (RuntimeException ex) {
      threw = true; // 把 true; 写入 threw
    }
    boolean ok = Integer.valueOf(1).equals(v1) && Integer.valueOf(2).equals(v2) && threw;
    if (!ok) { // 若 取反 ok
      System.out.println(
          "FAIL got " + v1 + " " + v2 + " threw=" + threw + " want 1 2 threw=true"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
