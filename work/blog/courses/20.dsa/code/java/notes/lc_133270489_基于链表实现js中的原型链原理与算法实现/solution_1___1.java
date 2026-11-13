// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
package com.webfault.dsa; // 引入依赖

class lc133270489_solution11 { // 定义类型
  // 模拟 JS 对象：拥有自己的属性 dict 与指向父原型的 __proto__
  static class Proto { // static class Proto {
    String name; // String name;
    java.util.Map<String, String> props = new java.util.HashMap<>();
    Proto proto; // Proto proto;

    Proto(String name, Proto parent) {
      this.name = name;
      this.proto = parent;
    }

    void set(String k, String v) {
      props.put(k, v);
    } // void set(String 下标 k, String 值) { props.put(下标 k, 值); }
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
    Proto functionProto = new Proto("Function.prototype", objectProto);
    Proto arrayProto = new Proto("Array.prototype", objectProto);
    Proto obj = new Proto("obj", objectProto); // 把 new Proto(「obj」, objectProto); 写入 Proto obj
    Proto func =
        new Proto("func", functionProto); // 把 new Proto(「func」, functionProto); 写入 Proto func
    Proto arr = new Proto("arr", arrayProto); // 把 new Proto(「数组」, arrayProto); 写入 Proto arr
    boolean[] r = { // 把 { 写入 boolean[] r
      instanceOf(obj, objectProto),
      instanceOf(func, functionProto),
      instanceOf(func, objectProto),
      instanceOf(arr, arrayProto),
      instanceOf(arr, objectProto),
    };
    for (boolean b : r) { // for (boolean b : 右指针) {
      if (!b) { // 若 取反 b
        System.out.println("FAIL"); // 打印输出
        throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
      }
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
