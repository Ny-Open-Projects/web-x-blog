// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
// LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — Dart 版（方案B：逐键求值 / reduce 链式访问）
Object? getValueEval(Map<String, dynamic> data, List<String> path) {
  var cur = data as Object?; // 把 data as Object? 存入 当前值
  for (final k in path) {
    // for (final 下标 k in 当前路径) {
    cur =
        (cur
            as Map<
              String,
              dynamic
            >)[k]; // 把 (当前值 as Map 小于 String, dynamic 超过 )[下标 k] 存入 当前值
  }
  return cur; // 返回 当前值
}

Object? getValueChain(Map<String, dynamic> data, List<String> path) {
  return path.fold<Object?>(data, (acc, k) => (acc as Map<String, dynamic>)[k]);
}

void main() {
  // 程序入口：跑内嵌自测用例
  final data = <String, dynamic>{
    // 把 小于 String, dynamic 超过 { 存入 data
    'a': <String, dynamic>{
      'b': <String, dynamic>{'c': 1},
    },
    'd': <String, dynamic>{'e': 2},
  };
  if (getValueEval(data, ['a', 'b', 'c']) != 1) throw StateError('p1 failed');
  if (getValueChain(data, ['d', 'e']) != 2) throw StateError('p2 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
