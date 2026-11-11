// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案5：八皇后布尔数组标记，行号 0..n-1）
List<List<int>> nQueensBool(int n) {
  // 定义函数/方法 nQueensBool
  final colRow = List<int>.filled(
    n,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数, 0) 存入 colRow
  final rows = List<bool>.filled(
    n,
    true,
  ); // 把 List 小于 bool 超过 .filled(元素个数, true) 存入 行数
  final diag1 = List<bool>.filled(
    2 * n - 1,
    true,
  ); // 把 List 小于 bool 超过 .filled(2 乘 元素个数 减 1, true) 存入 diag1
  final diag2 = List<bool>.filled(
    2 * n - 1,
    true,
  ); // 把 List 小于 bool 超过 .filled(2 乘 元素个数 减 1, true) 存入 diag2
  final offset = n - 1; // 把 元素个数 减 1 存入 offset
  final results = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 results

  void place(int col) {
    // 定义函数/方法 place
    if (col == n) {
      // 若 col 等于 元素个数
      results.add(
        List<int>.from(colRow),
      ); // results 追加 List 小于 int 超过 .from(colRow));
      return; // return;
    }
    for (var row = 0; row < n; row++) {
      // 让 row 从 0 开始计数，row 小于 元素个数 就继续
      final d1 = col - row + offset; // 把 col 减 row 加 offset 存入 d1
      final d2 = col + row; // 把 col 加 row 存入 d2
      if (rows[row] && diag1[d1] && diag2[d2]) {
        // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
        colRow[col] = row; // 把 row; 写入 colRow[col]
        rows[row] = false; // 把 false; 写入 rows[row]
        diag1[d1] = false; // 把 false; 写入 diag1[d1]
        diag2[d2] = false; // 把 false; 写入 diag2[d2]
        place(col + 1); // place(col 加 1);
        rows[row] = true; // 把 true; 写入 rows[row]
        diag1[d1] = true; // 把 true; 写入 diag1[d1]
        diag2[d2] = true; // 把 true; 写入 diag2[d2]
      }
    }
  }

  place(0); // place(0);
  return results; // 返回 results
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
    final sols = nQueensBool(
      c[0] as int,
    ); // 把 nQueensBool(字符[0] as int) 存入 sols
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
