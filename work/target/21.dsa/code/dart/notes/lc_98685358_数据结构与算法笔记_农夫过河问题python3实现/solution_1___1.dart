// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
// LeetCode 98685358. 农夫过河问题 — Dart 版（农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸 1=右岸）

bool isSafe(List<int> s) {
  // 定义判定函数 isSafe
  if (s[1] == s[2] && s[0] != s[1])
    return false; // 若 字符串[1] 等于 字符串[2] 且 字符串[0] 不等于 字符串[1]，直接返回 false
  if (s[2] == s[3] && s[0] != s[2])
    return false; // 若 字符串[2] 等于 字符串[3] 且 字符串[0] 不等于 字符串[2]，直接返回 false
  return true; // 返回 true
}

String key(List<int> s) => s.join(',');

List<List<int>>? solve() {
  // List 小于 List 小于 int 超过 超过 ? solve() {
  final start = <int>[0, 0, 0, 0]; // 把 小于 int 超过 [0, 0, 0, 0] 存入 起点
  final goal = <int>[1, 1, 1, 1]; // 把 小于 int 超过 [1, 1, 1, 1] 存入 goal
  final prev = <String, String?>{}; // key -> 父 key（起点为 null）
  final stateBy =
      <String, List<int>>{}; // 把 小于 String, List 小于 int 超过 超过 {} 存入 stateBy
  prev[key(start)] = null; // 把 null; 写入 prev[key(start)]
  stateBy[key(start)] = start; // 把 起点; 写入 stateBy[key(start)]
  final q = <List<int>>[start]; // 把 小于 List 小于 int 超过 超过 [起点] 存入 节点
  var head = 0; // 把 0 存入 头节点
  while (head < q.length) {
    // 循环，直到不满足「头节点 小于 节点.长度」
    final cur = q[head++]; // 把 节点[头节点 加一 ] 存入 当前值
    final ck = key(cur); // 把 key(当前值) 存入 ck
    if (ck == key(goal)) {
      // 若 ck 等于 key(goal
      final path = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 当前路径
      String? k = ck; // 把 ck; 写入 String? k
      while (k != null) {
        // 循环，直到不满足「下标 k 不等于 null」
        path.add(stateBy[k]!); // 当前路径 追加 stateBy[下标 k]取反 );
        k = prev[k]; // 把 前一个[下标 k] 存入 下标 k
      }
      return path.reversed.toList(); // 返回 当前路径.reversed.toList()
    }
    final farmer = cur[0]; // 把 当前值[0] 存入 farmer
    for (var i = 0; i < 4; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
      if (i != 0 && cur[i] != farmer)
        continue; // 若 下标 i 不等于 0 且 当前值[下标 i] 不等于 farmer) continue;
      final nxt = List<int>.from(cur); // 把 List 小于 int 超过 .from(当前值) 存入 nxt
      nxt[0] = 1 - farmer; // 把 1 减 farmer; 写入 nxt[0]
      if (i != 0)
        nxt[i] = 1 - farmer; // 若 下标 i 不等于 0) nxt[下标 i] 赋值为 1 减 farmer;
      final nk = key(nxt); // 把 key(nxt) 存入 nk
      if (prev.containsKey(nk)) continue; // 若 前一个.containsKey(nk)) continue;
      if (!isSafe(nxt)) continue; // 若 取反 isSafe(nxt)) continue;
      prev[nk] = ck; // 把 ck; 写入 prev[nk]
      stateBy[nk] = nxt; // 把 nxt; 写入 stateBy[nk]
      q.add(nxt); // 节点 追加 nxt);
    }
  }
  return null; // 返回 null
}

void main() {
  // 程序入口：跑内嵌自测用例
  final want = <List<int>>[
    <int>[0, 0, 0, 0],
    <int>[1, 0, 1, 0],
    <int>[0, 0, 1, 0],
    <int>[1, 1, 1, 0],
    <int>[0, 1, 0, 0],
    <int>[1, 1, 0, 1],
    <int>[0, 1, 0, 1],
    <int>[1, 1, 1, 1],
  ];
  final path = solve(); // 把 solve() 存入 当前路径
  if (path == null)
    throw StateError(
      'FAILED: 无解',
    ); // 若 当前路径 等于 null) throw StateError('FAILED: 无解');
  final ok =
      path.length == want.length &&
      List.generate(
        want.length,
        (i) => path[i].toString() == want[i].toString(),
      ).every((x) => x);
  if (!ok)
    throw StateError(
      'FAILED: path mismatch',
    ); // 若 取反 ok) throw StateError('FAILED: 当前路径 mismatch');
  print('PASS'); // 全部用例通过，输出 PASS
}
