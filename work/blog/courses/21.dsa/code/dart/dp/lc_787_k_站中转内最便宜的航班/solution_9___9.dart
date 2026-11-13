// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133472893
// LeetCode 787. K站中转内最便宜的航班 — Dart 版（方案9）
int findCheapestPrice(int n, List<List<int>> flights, int src, int dst, int k) {
  // 定义函数/方法 findCheapestPrice
  final INF = 0x3f3f3f3f; // 把 0x3f3f3f3f 存入 INF
  final dist = List<int>.filled(
    n,
    INF,
  ); // 把 List 小于 int 超过 .filled(元素个数, INF) 存入 dist
  dist[src] = 0; // 把 0; 写入 dist[src]
  for (var t = 0; t <= k; t++) {
    // 让 另一字符串 从 0 开始计数，另一字符串 不超过 下标 k 就继续
    final nd = List<int>.from(dist); // 把 List 小于 int 超过 .from(dist) 存入 nd
    for (final f in flights) {
      // for (final f in flights) {
      final u = f[0],
          v = f[1],
          w = f[2]; // 把 f[0], 值 赋值为 f[1], 权重 赋值为 f[2] 存入 节点 u
      if (dist[u] != INF && dist[u] + w < nd[v]) nd[v] = dist[u] + w;
    }
    for (var i = 0; i < n; i++)
      dist[i] = nd[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
  }
  return dist[dst] == INF
      ? -1
      : dist[dst]; // 返回 dist[dst] 等于 INF ? 减 1 : dist[dst]
}

void main() {
  // 程序入口：跑内嵌自测用例
  final f = [
    [0, 1, 100],
    [1, 2, 100],
    [2, 0, 100],
    [1, 3, 600],
    [2, 3, 200],
  ]; // 把 [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]] 存入 f
  if (findCheapestPrice(4, f, 0, 3, 1) != 700) throw StateError('c1');
  if (findCheapestPrice(4, f, 0, 0, 1) != 0) throw StateError('c2');
  if (findCheapestPrice(4, f, 0, 3, 2) != 400) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
