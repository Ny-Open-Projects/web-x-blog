// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案7：八皇后位置对列表）
List<List<int>> nQueensSimple(int n) {
  // 定义函数/方法 nQueensSimple
  final positions = <List<int>>[]; // [row, col]
  final solutions = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 solutions

  bool safe(int r, int c) {
    // 定义函数/方法 safe
    for (final p in positions) {
      // for (final 节点 in positions) {
      if (p[0] == r || (p[0] - r).abs() == (p[1] - c).abs()) {
        // 若 节点[0] 等于 右指针 或 (节点[0] 减 右指针).取绝对值 ) 等于 (节点[1] 减 字符).取绝对值
        return false; // 返回 false
      }
    }
    return true; // 返回 true
  }

  void solve(int col) {
    // 定义函数/方法 solve
    if (col == n) {
      // 若 col 等于 元素个数
      solutions.add(positions.map((p) => p[0]).toList());
      return; // return;
    }
    for (var r = 0; r < n; r++) {
      // 让 右指针 从 0 开始计数，右指针 小于 元素个数 就继续
      if (safe(r, col)) {
        // 若 safe(右指针, col
        positions.add([r, col]); // positions 追加 [右指针, col]);
        solve(col + 1); // solve(col 加 1);
        positions.removeLast(); // positions.removeLast();
      }
    }
  }

  solve(0); // solve(0);
  return solutions; // 返回 solutions
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<dynamic>>[
    [
      8,
      92,
      [0, 4, 7, 5, 2, 6, 1, 3],
    ],
    [
      1,
      1,
      [0],
    ],
    [2, 0, null],
    [
      4,
      2,
      [1, 3, 0, 2],
    ],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 cases.长度 就继续
    final c = cases[idx]; // 把 cases[idx] 存入 字符
    final sols = nQueensSimple(
      c[0] as int,
    ); // 把 nQueensSimple(字符[0] as int) 存入 sols
    if (sols.length != c[1] as int) throw StateError('case $idx count');
    if (c[2] != null && sols[0].toString() != c[2].toString()) {
      // 若 字符[2] 不等于 null 且 sols[0].toString() 不等于 字符[2].toString(
      throw StateError(
        'case $idx first',
      ); // throw StateError('case $idx first');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
