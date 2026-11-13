// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc133270489_solution22 { // 定义类型
  static class Proto { // static class Proto {
    String name; // String name;
    Map<String, String> props =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 Map<String, String> props
    Proto proto; // Proto proto;

    Proto(String name) {
      this.name = name;
    } // 把 name; } 写入 Proto(String name) { this.name

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

  public static void main(String[] args) { // public static void main(String[] args) {
    Proto objectProto =
        new Proto("Object.prototype"); // 把 new Proto(「Object.prototype」); 写入 Proto objectProto
    objectProto.set("x", "x"); // objectProto.set(「x」, 「x」);
    Proto functionProto = new Proto("Function.prototype", objectProto);
    functionProto.set("y", "y"); // functionProto.set(「y」, 「y」);
    Proto arrayProto = new Proto("Array.prototype", objectProto);
    arrayProto.set("z", "z"); // arrayProto.set(「z」, 「z」);
    Proto obj = new Proto("obj", objectProto); // 把 new Proto(「obj」, objectProto); 写入 Proto obj
    Proto func =
        new Proto("func", functionProto); // 把 new Proto(「func」, functionProto); 写入 Proto func
    Proto arr = new Proto("arr", arrayProto); // 把 new Proto(「数组」, arrayProto); 写入 Proto arr
    if (!"x".equals(obj.get("x"))) {
      System.out.println("FAIL x");
      throw new RuntimeException("FAILED");
    }
    if (!"y".equals(func.get("y"))) {
      System.out.println("FAIL y");
      throw new RuntimeException("FAILED");
    }
    if (!"z".equals(arr.get("z"))) {
      System.out.println("FAIL z");
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
