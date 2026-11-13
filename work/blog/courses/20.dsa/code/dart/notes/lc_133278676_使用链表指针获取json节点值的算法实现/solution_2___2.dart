// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133278676
// LeetCode 133278676. 使用链表（指针链）获取 JSON 节点值 — Dart 版（方案A：安全遍历（单用例），缺失返回 null）
Object? getValue(Map<String, dynamic> data, List<String> path) {
  var node = data as Object?; // 把 data as Object? 存入 节点
  for (final key in path) {
    // for (final key in 当前路径) {
    if (node is! Map<String, dynamic> || !node.containsKey(key)) return null;
    node = node[key]; // 把 节点[key] 存入 节点
  }
  return node; // 返回 节点
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
  if (getValue(data, ['a', 'b', 'c']) != 1) throw StateError('p1 failed');
  if (getValue(data, ['a', 'z']) != null) throw StateError('p2 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
