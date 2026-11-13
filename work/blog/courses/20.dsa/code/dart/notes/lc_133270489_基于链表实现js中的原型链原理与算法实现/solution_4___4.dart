// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Dart 版（方案4：null/undefined 边界：instanceOf 均返回 false）
class Obj {
  // 定义类型
  Obj? __proto__; // Obj? __proto__;
}

class Ctor {
  // 定义类型
  Obj? prototype; // Obj? prototype;
}

bool instanceOf(Obj? a, Ctor b) {
  // 定义函数/方法 instanceOf
  Obj? p = a; // 把 数组; 写入 Obj? p
  while (p != null) {
    // 循环，直到不满足「节点 不等于 null」
    if (identical(p, b.prototype))
      return true; // 若 identical(节点, b.prototype)，直接返回 true
    p = p.__proto__; // 把 节点.__proto__ 存入 节点
  }
  return false; // 返回 false
}

void main() {
  // 程序入口：跑内嵌自测用例
  final ctor = Ctor(); // 把 Ctor() 存入 ctor
  // Dart 中 null 对应 JS 的 null/undefined
  if (instanceOf(null, ctor)) throw StateError('null case failed');
  if (instanceOf(null, ctor)) throw StateError('undefined case failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
