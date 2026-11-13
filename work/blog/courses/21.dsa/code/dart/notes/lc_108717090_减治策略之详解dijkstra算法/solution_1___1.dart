// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
// 减治策略之详解Dijkstra算法 — Dart 版（方案1）
List<int> dijkstraShortest(List<List<List<int>>> graph, int start) {
  // 定义函数/方法 dijkstraShortest
  final n = graph.length; // 把 graph.长度 存入 元素个数
  final dist = List<int>.filled(
    n,
    0x3f3f3f3f,
  ); // 把 List 小于 int 超过 .filled(元素个数, 0x3f3f3f3f) 存入 dist
  final visited = List<bool>.filled(
    n,
    false,
  ); // 把 List 小于 bool 超过 .filled(元素个数, false) 存入 已访问集合
  dist[start] = 0; // 把 0; 写入 dist[start]
  while (true) {
    // 循环，直到不满足「true」
    int u = -1; // 把 减 1 存入 节点 u
    for (var i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if (!visited[i] && (u < 0 || dist[i] < dist[u])) u = i;
    }
    if (u < 0 || dist[u] == 0x3f3f3f3f)
      break; // 若 节点 u 小于 0 或 dist[节点 u] 等于 0x3f3f3f3f) break;
    visited[u] = true; // 把 true; 写入 visited[u]
    for (final e in graph[u]) {
      // for (final e in graph[节点 u]) {
      final v = e[0], w = e[1]; // 把 e[0], 权重 赋值为 e[1] 存入 值
      if (dist[u] + w < dist[v])
        dist[v] =
            dist[u] +
            w; // 若 dist[节点 u] 加 权重 小于 dist[值]) dist[值] 赋值为 dist[节点 u] 加 权重;
    }
  }
  return dist; // 返回 dist
}

void main() {
  // 程序入口：跑内嵌自测用例
  final g = <List<List<int>>>[
    [
      [1, 10],
      [2, 3],
    ],
    [
      [2, 1],
      [3, 2],
    ],
    [
      [1, 4],
      [3, 8],
    ],
    [
      [4, 7],
    ],
    [], // []
  ];
  final d = dijkstraShortest(g, 0); // 把 dijkstraShortest(g, 0) 存入 d
  if (d[0] != 0 || d[1] != 7 || d[2] != 3 || d[3] != 9 || d[4] != 16)
    throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
