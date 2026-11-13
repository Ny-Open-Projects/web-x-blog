// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Dart 版（方案3：get 查找 + instanceOf 判定）
class Proto {
  // 定义类型
  String name; // String name;
  Map<String, String> props = {}; // 把 {}; 写入 Map<String, String> props
  Proto? parent; // Proto? parent;
  Proto(this.name, [this.parent]); // Proto(this.name, [this.parent]);

  void set(String key, String value) {
    // 定义函数/方法 set
    props[key] = value; // 把 value; 写入 props[key]
  }

  bool has(String key) {
    // 定义函数/方法 has
    Proto? cur = this; // 把 this; 写入 Proto? cur
    while (cur != null) {
      // 循环，直到不满足「当前值 不等于 null」
      if (cur.props.containsKey(key))
        return true; // 若 当前值.props.containsKey(key)，直接返回 true
      cur = cur.parent; // 把 当前值.parent 存入 当前值
    }
    return false; // 返回 false
  }

  String? get(String key) {
    // String? get(String key) {
    Proto? cur = this; // 把 this; 写入 Proto? cur
    while (cur != null) {
      // 循环，直到不满足「当前值 不等于 null」
      if (cur.props.containsKey(key))
        return cur
            .props[key]; // 若 当前值.props.containsKey(key)，直接返回 当前值.props[key]
      cur = cur.parent; // 把 当前值.parent 存入 当前值
    }
    return null; // 返回 null
  }
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
  objectProto.set('a', 'aaa'); // objectProto.set('数组', 'aaa');
  final functionProto = Proto(
    'Function.prototype',
    objectProto,
  ); // 把 Proto('Function.prototype', objectProto) 存入 functionProto
  functionProto.set('b', 'bbb'); // functionProto.set('b', 'bbb');
  final obj = Proto('obj', objectProto); // 把 Proto('obj', objectProto) 存入 obj
  final func = Proto(
    'func',
    functionProto,
  ); // 把 Proto('func', functionProto) 存入 func

  assert(obj.get('a') == 'aaa', 'case 0 failed'); // 断言校验
  assert(!obj.has('b'), 'case 1 failed'); // 断言校验
  assert(func.get('a') == 'aaa', 'case 2 failed'); // 断言校验
  assert(func.get('b') == 'bbb', 'case 3 failed'); // 断言校验
  assert(instanceOf(func, objectProto), 'case 4 failed'); // 断言校验
  print('PASS'); // 全部用例通过，输出 PASS
}
