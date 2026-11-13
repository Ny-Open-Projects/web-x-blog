// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Dart 版（方案3：DFS+奇偶步求解）
const D = <List<int>>[
  [2, 0],
  [1, 0],
  [1, 1],
  [0, 1],
  [0, 2],
];

bool safe(int r, int g) {
  // 定义函数/方法 safe
  return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

List<List<int>> solve() {
  // 定义函数/方法 solve
  final path = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 当前路径
  final visited = <String>{}; // 把 小于 String 超过 {} 存入 已访问集合

  bool dfs(int r, int g, int step) {
    // 定义函数/方法 dfs
    if (r == 0 && g == 0) return true; // 若 右指针 等于 0 且 g 等于 0，直接返回 true
    final key = '$r,$g,${step % 2}'; // 把 '$右指针,$g,${步数 对…取模 2}' 存入 key
    if (visited.contains(key)) return false; // 若 已访问集合 是否包含 key)，直接返回 false
    visited.add(key); // 已访问集合 追加 key);
    final odd = step % 2 == 1; // 把 步数 对…取模 2 等于 1 存入 odd
    for (final d in D) {
      // for (final d in D) {
      final dr = d[0], dg = d[1]; // 把 d[0], dg 赋值为 d[1] 存入 dr
      var nr = 0, ng = 0; // 把 0, ng 赋值为 0 存入 nr
      var skip = false; // 把 false 存入 skip
      if (odd) {
        // 若 odd
        if (r < dr || g < dg) {
          // 若 右指针 小于 dr 或 g 小于 dg
          skip = true; // 把 true 存入 skip
        } else {
          // 否则
          nr = r - dr; // 把 右指针 减 dr 存入 nr
          ng = g - dg; // 把 g 减 dg 存入 ng
        }
      } else {
        // 否则
        if ((3 - r) < dr || (3 - g) < dg) {
          // 若 (3 减 右指针) 小于 dr 或 (3 减 g) 小于 dg
          skip = true; // 把 true 存入 skip
        } else {
          // 否则
          nr = r + dr; // 把 右指针 加 dr 存入 nr
          ng = g + dg; // 把 g 加 dg 存入 ng
        }
      }
      if (skip) continue; // 若 skip) continue;
      if (!safe(nr, ng)) continue; // 若 取反 safe(nr, ng)) continue;
      if (dfs(nr, ng, step + 1)) {
        // 若 dfs(nr, ng, 步数 加 1
        path.add([dr, dg]); // 当前路径 追加 [dr, dg]);
        return true; // 返回 true
      }
    }
    return false; // 返回 false
  }

  dfs(3, 3, 1); // dfs(3, 3, 1);
  return path.reversed.toList(); // 返回 当前路径.reversed.toList()
}

void main() {
  // 程序入口：跑内嵌自测用例
  final want = <List<int>>[
    [1, 1],
    [1, 0],
    [0, 2],
    [0, 1],
    [2, 0],
    [1, 1],
    [2, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
  ];
  final got = solve(); // 把 solve() 存入 got
  if (got.toString() != want.toString()) {
    // 若 got.toString() 不等于 want.toString(
    throw StateError(
      'solve mismatch: ' + got.toString(),
    ); // throw StateError('solve mismatch: ' 加 got.toString());
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
