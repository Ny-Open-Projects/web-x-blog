// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
// LeetCode 133651611. 图及其深度和广度优先遍历实现 — Dart 版（方案3）
class Graph {
  // 定义类型
  final Map<int, List<int>> _adjList =
      {}; // 把 {}; 写入 final Map<int, List<int>> _adjList

  void addEdge(int from, int to) {
    // 定义函数/方法 addEdge
    _adjList.putIfAbsent(from, () => <int>[]);
    _adjList.putIfAbsent(to, () => <int>[]);
    _adjList[from]!.add(to); // _adjList[from]取反 追加 to);
    _adjList[to]!.add(from); // _adjList[to]取反 追加 from);
  }

  List<int> dfs(int start) {
    // 定义函数/方法 dfs
    final visited = <int>{}; // 把 小于 int 超过 {} 存入 已访问集合
    final result = <int>[]; // 把 小于 int 超过 [] 存入 结果
    void helper(int node) {
      // 定义函数/方法 helper
      if (visited.contains(node)) return; // 若 已访问集合 是否包含 节点)) return;
      visited.add(node); // 已访问集合 追加 节点);
      result.add(node); // 结果 追加 节点);
      for (final neighbor in _adjList[node] ?? <int>[]) {
        // for (final neighbor in _adjList[节点] ?? 小于 int 超过 []) {
        helper(neighbor); // helper(neighbor);
      }
    }

    helper(start); // helper(起点);
    return result; // 返回 结果
  }

  List<int> bfs(int start) {
    // 定义函数/方法 bfs
    final visited = <int>{start}; // 把 小于 int 超过 {起点} 存入 已访问集合
    final result = <int>[]; // 把 小于 int 超过 [] 存入 结果
    final queue = <int>[start]; // 把 小于 int 超过 [起点] 存入 队列
    var head = 0; // 把 0 存入 头节点
    while (head < queue.length) {
      // 循环，直到不满足「头节点 小于 队列.长度」
      final node = queue[head++]; // 把 队列[头节点 加一 ] 存入 节点
      result.add(node); // 结果 追加 节点);
      for (final neighbor in _adjList[node] ?? <int>[]) {
        // for (final neighbor in _adjList[节点] ?? 小于 int 超过 []) {
        if (!visited.contains(neighbor)) {
          // 若 取反 已访问集合 是否包含 neighbor
          visited.add(neighbor); // 已访问集合 追加 neighbor);
          queue.add(neighbor); // 队列 追加 neighbor);
        }
      }
    }
    return result; // 返回 结果
  }
}

bool eq(List<int> a, List<int> b) {
  // 定义函数/方法 eq
  if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (var i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] != b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  // case 1: 方形图 0-1-3-2-0
  final g1 = Graph(); // 把 Graph() 存入 g1
  g1.addEdge(0, 1); // g1.addEdge(0, 1);
  g1.addEdge(0, 2); // g1.addEdge(0, 2);
  g1.addEdge(1, 3); // g1.addEdge(1, 3);
  g1.addEdge(2, 3); // g1.addEdge(2, 3);
  if (!eq(g1.dfs(0), [0, 1, 3, 2])) throw StateError('FAILED case1 dfs(0)');
  if (!eq(g1.bfs(0), [0, 1, 2, 3])) throw StateError('FAILED case1 bfs(0)');

  // case 2: 从另一节点出发
  if (!eq(g1.dfs(2), [2, 0, 1, 3])) throw StateError('FAILED case2 dfs(2)');
  if (!eq(g1.bfs(2), [2, 0, 3, 1])) throw StateError('FAILED case2 bfs(2)');

  print('PASS'); // 全部用例通过，输出 PASS
}
