// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc133270489_solution33 { // 定义类型
  static class Proto { // static class Proto {
    String name; // String name;
    Map<String, String> props =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<String, String> props
    Proto proto; // Proto proto;

    Proto(String name, Proto parent) {
      this.name = name;
      this.proto = parent;
    }

    void set(String k, String v) {
      props.put(k, v);
    } // void set(String 下标 k, String 值) { props.put(下标 k, 值); }

    String get(String k) { // 定义函数/方法 get
      Proto cur = this; // 把 this; 写入 Proto cur
      while (cur != null) { // 循环，直到不满足「当前值 不等于 null」
        if (cur.props.containsKey(k))
          return cur.props.get(k); // 若 当前值.props.containsKey(下标 k)，直接返回 当前值.props 查找 下标 k)
        cur = cur.proto; // 把 当前值.proto; 写入 当前值
      }
      return null; // 返回 null
    }
  }

  static boolean instanceOf(Proto obj, Proto prototype) { // 定义函数/方法 instanceOf
    Proto p = obj; // 把 obj; 写入 Proto p
    while (p != null) { // 循环，直到不满足「节点 不等于 null」
      if (p == prototype) return true; // 若 节点 等于 prototype，直接返回 true
      p = p.proto; // 把 节点.proto; 写入 节点
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Proto objectProto =
        new Proto(
            "Object.prototype",
            null); // 把 new Proto(「Object.prototype」, null); 写入 Proto objectProto
    objectProto.set("a", "aaa"); // objectProto.set(「数组」, 「数组」);
    Proto functionProto = new Proto("Function.prototype", objectProto);
    functionProto.set("b", "bbb"); // functionProto.set(「b」, 「b」);
    Proto obj = new Proto("obj", objectProto); // 把 new Proto(「obj」, objectProto); 写入 Proto obj
    Proto func =
        new Proto("func", functionProto); // 把 new Proto(「func」, functionProto); 写入 Proto func
    if (!"aaa".equals(obj.get("a"))) {
      System.out.println("FAIL a");
      throw new RuntimeException("FAILED");
    }
    if (obj.get("b") != null) {
      System.out.println("FAIL b-should-be-null");
      throw new RuntimeException("FAILED");
    }
    if (!"aaa".equals(func.get("a"))) {
      System.out.println("FAIL func-a");
      throw new RuntimeException("FAILED");
    }
    if (!"bbb".equals(func.get("b"))) {
      System.out.println("FAIL func-b");
      throw new RuntimeException("FAILED");
    }
    if (!instanceOf(func, objectProto)) {
      System.out.println("FAIL instanceof");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
