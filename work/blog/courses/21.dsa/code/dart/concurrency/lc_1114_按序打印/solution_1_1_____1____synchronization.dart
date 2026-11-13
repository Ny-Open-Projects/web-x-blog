// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
// LeetCode 1114. 按序打印 — Dart 版（方案1）
String printInOrder() {
  // 定义函数/方法 printInOrder
  final out = <String>[]; // 把 小于 String 超过 [] 存入 out
  var step = 1; // 把 1 存入 步数
  void first() {
    // 定义函数/方法 first
    out.add('first'); // out 追加 'first');
    step = 2; // 把 2 存入 步数
  }

  void second() {
    // 定义函数/方法 second
    while (step < 2) {} // 循环，直到不满足「步数 小于 2) {}」
    out.add('second'); // out 追加 'second');
    step = 3; // 把 3 存入 步数
  }

  void third() {
    // 定义函数/方法 third
    while (step < 3) {} // 循环，直到不满足「步数 小于 3) {}」
    out.add('third'); // out 追加 'third');
  }

  first(); // first();
  second(); // second();
  third(); // third();
  return out.join(); // 返回 out.join()
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (printInOrder() != 'firstsecondthird') throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
