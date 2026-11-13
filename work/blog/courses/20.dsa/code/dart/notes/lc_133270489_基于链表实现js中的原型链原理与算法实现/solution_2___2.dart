// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
// LeetCode 133270489. 原型链原理 — Dart 版（方案2：get 沿原型链查找属性）
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

void main() {
  // 程序入口：跑内嵌自测用例
  final objectProto = Proto(
    'Object.prototype',
  ); // 把 Proto('Object.prototype') 存入 objectProto
  objectProto.set('x', 'x'); // objectProto.set('x', 'x');
  final functionProto = Proto(
    'Function.prototype',
    objectProto,
  ); // 把 Proto('Function.prototype', objectProto) 存入 functionProto
  functionProto.set('y', 'y'); // functionProto.set('y', 'y');
  final arrayProto = Proto(
    'Array.prototype',
    objectProto,
  ); // 把 Proto('Array.prototype', objectProto) 存入 arrayProto
  arrayProto.set('z', 'z'); // arrayProto.set('z', 'z');
  final obj = Proto('obj', objectProto); // 把 Proto('obj', objectProto) 存入 obj
  final func = Proto(
    'func',
    functionProto,
  ); // 把 Proto('func', functionProto) 存入 func
  final arr = Proto('arr', arrayProto); // 把 Proto('数组', arrayProto) 存入 数组

  assert(obj.get('x') == 'x', 'case 0 failed'); // 断言校验
  assert(func.get('y') == 'y', 'case 1 failed'); // 断言校验
  assert(arr.get('z') == 'z', 'case 2 failed'); // 断言校验
  print('PASS'); // 全部用例通过，输出 PASS
}
