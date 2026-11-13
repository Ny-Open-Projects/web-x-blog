// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Dart 版（方案1：instanceOf 沿原型链判定）
class Proto {
  // 定义类型
  String name; // String name;
  Map<String, String> props = {}; // 把 {}; 写入 Map<String, String> props
  Proto? parent; // Proto? parent;
  Proto(this.name, [this.parent]); // Proto(this.name, [this.parent]);
}

bool instanceOf(Proto obj, Proto prototype) {
  // 定义函数/方法 instanceOf
  Proto? p = obj; // 把 obj; 写入 Proto? p
  while (p != null) {
    // 循环，直到不满足「节点 不等于 null」
    if (identical(p, prototype))
      return true; // 若 identical(节点, prototype)，直接返回 true
    p = p.parent; // 把 节点.parent 存入 节点
  }
  return false; // 返回 false
}

void main() {
  // 程序入口：跑内嵌自测用例
  final objectProto = Proto(
    'Object.prototype',
  ); // 把 Proto('Object.prototype') 存入 objectProto
  final functionProto = Proto(
    'Function.prototype',
    objectProto,
  ); // 把 Proto('Function.prototype', objectProto) 存入 functionProto
  final arrayProto = Proto(
    'Array.prototype',
    objectProto,
  ); // 把 Proto('Array.prototype', objectProto) 存入 arrayProto
  final obj = Proto('obj', objectProto); // 把 Proto('obj', objectProto) 存入 obj
  final func = Proto(
    'func',
    functionProto,
  ); // 把 Proto('func', functionProto) 存入 func
  final arr = Proto('arr', arrayProto); // 把 Proto('数组', arrayProto) 存入 数组

  assert(instanceOf(obj, objectProto), 'case 0 failed'); // 断言校验
  assert(instanceOf(func, functionProto), 'case 1 failed'); // 断言校验
  assert(instanceOf(func, objectProto), 'case 2 failed'); // 断言校验
  assert(instanceOf(arr, arrayProto), 'case 3 failed'); // 断言校验
  assert(instanceOf(arr, objectProto), 'case 4 failed'); // 断言校验
  print('PASS'); // 全部用例通过，输出 PASS
}
