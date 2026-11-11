// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
// 图搜索之BFS详解 — Dart 版（方案1）
List<int> bfsOrder(List<List<int>> graph, int start) {
  // 定义函数/方法 bfsOrder
  final n = graph.length; // 把 graph.长度 存入 元素个数
  final visited = List<bool>.filled(
    n,
    false,
  ); // 把 List 小于 bool 超过 .filled(元素个数, false) 存入 已访问集合
  final order = <int>[]; // 把 小于 int 超过 [] 存入 order
  final queue = <int>[start]; // 把 小于 int 超过 [起点] 存入 队列
  var head = 0; // 把 0 存入 头节点
  visited[start] = true; // 把 true; 写入 visited[start]
  while (head < queue.length) {
    // 循环，直到不满足「头节点 小于 队列.长度」
    final c = queue[head++]; // 把 队列[头节点 加一 ] 存入 字符
    order.add(c); // order 追加 字符);
    for (final nx in graph[c]) {
      // for (final nx in graph[字符]) {
      if (!visited[nx]) {
        // 若 取反 已访问集合[nx]
        visited[nx] = true; // 把 true; 写入 visited[nx]
        queue.add(nx); // 队列 追加 nx);
      }
    }
  }
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
  if (bfsOrder(g, 0).toString() != '[0, 1, 2, 3, 4, 5]') throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
