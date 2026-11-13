// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108013114
// LeetCode 108013114. 贪心策略之BST&BBST_hashtable+dictionary+map — Dart 版（贪心策略之 BST/BBST/哈希表：Kruskal 最小生成树（并查集 + 排序））
final parent = <int, int>{}; // 把 小于 int, int 超过 {} 存入 parent

int find(int x) {
  // 定义函数/方法 find
  parent.putIfAbsent(x, () => x);
  while (parent[x] != x) {
    // 循环，直到不满足「parent[x] 不等于 x」
    parent[x] = parent[parent[x]]!; // 把 parent[parent[x]]取反 ; 写入 parent[x]
    x = parent[x]!; // 把 parent[x]取反 存入 x
  }
  return x!; // 返回 x取反
}

int kruskalMst(List<List<int>> edges) {
  // 定义函数/方法 kruskalMst
  final sorted = List<List<int>>.from(edges)
    ..sort((a, b) => a[2].compareTo(b[2]));
  parent.clear(); // parent.clear();
  var total = 0; // 把 0 存入 总和
  for (final e in sorted) {
    // for (final e in sorted) {
    final ru = find(e[0]); // 把 find(e[0]) 存入 ru
    final rv = find(e[1]); // 把 find(e[1]) 存入 rv
    if (ru != rv) {
      // 若 ru 不等于 rv
      parent[ru] = rv; // 把 rv; 写入 parent[ru]
      total += e[2]; // 总和累加 e[2]
    }
  }
  return total; // 返回 总和
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<List<int>>, int>{
    // 把 小于 List 小于 List 小于 int 超过 超过 , int 超过 { 存入 cases
    [
      [0, 1, 10],
      [0, 2, 6],
      [0, 3, 5],
      [1, 3, 15],
      [2, 3, 4],
    ]: 19,
    [
      [0, 1, 1],
      [1, 2, 2],
      [2, 3, 3],
      [3, 4, 4],
    ]: 10,
    [
      [0, 1, 2],
      [1, 2, 3],
    ]: 5,
    <List<int>>[]: 0,
  };
  var idx = 0; // 把 0 存入 idx
  cases.forEach((edges, want) {
    // cases.forEach((边集, want) {
    final got = kruskalMst(edges); // 把 kruskalMst(边集) 存入 got
    if (got != want) throw StateError('case $idx failed: got $got want $want');
    idx++; // idx 加一
  }); // });
  print('PASS'); // 全部用例通过，输出 PASS
}
