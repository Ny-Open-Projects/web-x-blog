// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
package com.webfault.dsa; // 引入依赖

class lc133270489_solution44 { // 定义类型
  // 基于链表表示 JS 原型链：判断 A 的原型链中是否包含 B.prototype
  static class Obj { // static class Obj {
    Obj proto; // Obj proto;
    Obj prototype; // Obj prototype;
  }

  static boolean instanceOf(Obj A, Obj B) { // 定义函数/方法 instanceOf
    Obj p = A; // 把 A; 写入 Obj p
    while (p != null) { // 循环，直到不满足「节点 不等于 null」
      if (p == B.prototype) return true; // 若 节点 等于 B.prototype，直接返回 true
      p = p.proto; // 把 节点.proto; 写入 节点
    }
    return false; // 返回 false
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    // 对应 Python: instanceOf(None, None) -> 链首为 None 直接跳过循环，返回 False
    boolean r = instanceOf(null, null); // 把 instanceOf(null, null); 写入 boolean r
    if (r) { // 若 右指针
      System.out.println("FAIL " + r); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
