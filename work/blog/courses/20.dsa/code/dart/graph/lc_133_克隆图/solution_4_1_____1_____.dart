// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
// LeetCode 133. 克隆图 — Dart 版

class GNode {
  // 定义类型
  int val; // int 值;
  List<GNode> neighbors = []; // 把 []; 写入 List<GNode> neighbors
  GNode(this.val); // GNode(this.值);
}

/// 方案4（BFS，visited 以节点对象为键）
GNode? cloneGraph(GNode? node) {
  // GNode? cloneGraph(GNode? 节点) {
  if (node == null) return null; // 若 节点 等于 null，直接返回 null
  final visited = <GNode, GNode>{}; // Dart 默认按对象身份比较
  visited[node] = GNode(node.val); // 把 GNode(节点.值); 写入 visited[node]
  final q = <GNode>[node]; // 把 小于 GNode 超过 [节点] 存入 节点
  var head = 0; // 把 0 存入 头节点
  while (head < q.length) {
    // 循环，直到不满足「头节点 小于 节点.长度」
    final n = q[head++]; // 把 节点[头节点 加一 ] 存入 元素个数
    for (final ne in n.neighbors) {
      // for (final ne in 元素个数.neighbors) {
      if (!visited.containsKey(ne)) {
        // 若 取反 已访问集合.containsKey(ne
        q.add(ne); // 节点 追加 ne);
        visited[ne] = GNode(ne.val); // 把 GNode(ne.值); 写入 visited[ne]
      }
      visited[n]!.neighbors.add(
        visited[ne]!,
      ); // 已访问集合[元素个数]取反 .neighbors 追加 已访问集合[ne]取反 );
    }
  }
  return visited[node]; // 返回 已访问集合[节点]
}

GNode buildGraph(List<List<int>> adj) {
  // 定义函数/方法 buildGraph
  final nodes = <GNode>[GNode(0)]; // 占位，下标从 1 开始
  for (var i = 1; i <= adj.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 邻接表.长度 就继续
    nodes.add(GNode(i)); // nodes 追加 GNode(下标 i));
  }
  for (var idx = 1; idx <= adj.length; idx++) {
    // 让 idx 从 1 开始计数，idx 不超过 邻接表.长度 就继续
    for (final nb in adj[idx - 1]) {
      // for (final nb in 邻接表[idx 减 1]) {
      nodes[idx].neighbors.add(
        nodes[nb],
      ); // nodes[idx].neighbors 追加 nodes[nb]);
    }
  }
  return nodes[1]; // 返回 nodes[1]
}

/// 收集签名：每个节点的邻居值列表（排序后），按节点 val 键控
Map<int, List<int>> signature(GNode node) {
  // Map 小于 int, List 小于 int 超过 超过 signature(GNode 节点) {
  final vis = <int, List<int>>{}; // 把 小于 int, List 小于 int 超过 超过 {} 存入 vis
  void dfs(GNode n) {
    // 定义函数/方法 dfs
    if (vis.containsKey(n.val)) return; // 若 vis.containsKey(元素个数.值)) return;
    vis[n.val] = n.neighbors.map((x) => x.val).toList()..sort();
    for (final x in n.neighbors) {
      // for (final x in 元素个数.neighbors) {
      dfs(x); // dfs(x);
    }
  }

  dfs(node); // dfs(节点);
  return vis; // 返回 vis
}

void main() {
  // 程序入口：跑内嵌自测用例
  final root = buildGraph([
    [2, 4],
    [1, 3],
    [2, 4],
    [1, 3],
  ]); // ]);
  final cloned = cloneGraph(root); // 把 cloneGraph(根节点) 存入 cloned
  if (cloned == null) throw StateError('cloneGraph returned null');
  if (identical(cloned, root))
    throw StateError('not a deep copy (same object)');
  final sig = signature(cloned); // 把 signature(cloned) 存入 sig
  const expected = {
    // 把 { 存入 expected
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3],
  };
  for (final k in [1, 2, 3, 4]) {
    // for (final 下标 k in [1, 2, 3, 4]) {
    final a = sig[k]; // 把 sig[下标 k] 存入 数组
    final b = expected[k]!; // 把 expected[下标 k]取反 存入 b
    if (a == null || a.length != b.length) {
      // 若 数组 等于 null 或 数组.长度 不等于 b.长度
      throw StateError(
        'signature mismatch at $k',
      ); // throw StateError('signature mismatch at $下标 k');
    }
    for (var i = 0; i < b.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 b.长度 就继续
      if (a[i] != b[i]) throw StateError('signature mismatch at $k');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
