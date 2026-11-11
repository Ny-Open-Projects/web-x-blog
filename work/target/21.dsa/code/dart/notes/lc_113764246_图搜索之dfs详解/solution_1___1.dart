// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
// 图搜索之DFS详解 — Dart 版（方案1）
List<int> dfsOrder(List<List<int>> graph, int start) {
  // 定义函数/方法 dfsOrder
  final visited = List<bool>.filled(
    graph.length,
    false,
  ); // 把 List 小于 bool 超过 .filled(graph.长度, false) 存入 已访问集合
  final order = <int>[]; // 把 小于 int 超过 [] 存入 order
  void go(int c) {
    // 定义函数/方法 go
    visited[c] = true; // 把 true; 写入 visited[c]
    order.add(c); // order 追加 字符);
    for (final nx in graph[c]) {
      // for (final nx in graph[字符]) {
      if (!visited[nx]) go(nx); // 若 取反 已访问集合[nx]) go(nx);
    }
  }

  go(start); // go(起点);
  return order; // 返回 order
}

void main() {
  // 程序入口：跑内嵌自测用例
  final g = <List<int>>[
    <int>[1, 2],
    <int>[3, 4],
    <int>[5],
    <int>[],
    <int>[],
    <int>[], // 小于 int 超过 []
  ];
  if (dfsOrder(g, 0).toString() != '[0, 1, 3, 4, 2, 5]') throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
