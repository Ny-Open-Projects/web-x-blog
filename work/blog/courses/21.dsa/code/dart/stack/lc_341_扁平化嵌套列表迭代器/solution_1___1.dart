// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145078849
// LeetCode 341. 扁平化嵌套列表迭代器 — Dart 版（方案1）
class NI {
  // 定义类型
  final int? intVal; // final int? intVal;
  final List<NI>? items; // final List 小于 NI 超过 ? items;
  NI.int_(this.intVal)
    : items = null; // 把 null; 写入 NI.int_(this.intVal) : items
  NI.list(this.items)
    : intVal = null; // 把 null; 写入 NI.list(this.items) : intVal
  bool get isInt => intVal != null;
}

List<int> flatten(List<NI> nested) {
  // 定义函数/方法 flatten
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  void go(List<NI> items) {
    // 定义函数/方法 go
    for (final it in items) {
      // for (final it in items) {
      if (it.isInt) {
        out.add(it.intVal!);
      } else {
        go(it.items!);
      }
    }
  }

  go(nested); // go(nested);
  return out; // 返回 out
}

void main() {
  // 程序入口：跑内嵌自测用例
  final nested = [
    NI.int_(1),
    NI.int_(2),
    NI.list([NI.int_(3), NI.int_(4)]),
  ];
  if (flatten(nested).toString() != '[1, 2, 3, 4]') throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
