// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案3：八皇后递归 isSafe，行号 1..n）
List<List<int>> nQueensSafe(int n) {
  // 定义函数/方法 nQueensSafe
  final results = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 results
  final board = List<int>.filled(
    n,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数, 0) 存入 棋盘

  bool isSafe(int col, int row) {
    // 定义判定函数 isSafe
    for (var c = 0; c < col; c++) {
      // 让 字符 从 0 开始计数，字符 小于 col 就继续
      if (board[c] == row || (board[c] - row).abs() == (c - col).abs()) {
        // 若 棋盘[字符] 等于 row 或 (棋盘[字符] 减 row).取绝对值 ) 等于 (字符 减 col).取绝对值
        return false; // 返回 false
      }
    }
    return true; // 返回 true
  }

  void place(int col) {
    // 定义函数/方法 place
    if (col == n) {
      // 若 col 等于 元素个数
      results.add(
        List<int>.from(board),
      ); // results 追加 List 小于 int 超过 .from(棋盘));
      return; // return;
    }
    for (var row = 1; row <= n; row++) {
      // 让 row 从 1 开始计数，row 不超过 元素个数 就继续
      if (isSafe(col, row)) {
        // 若 isSafe(col, row
        board[col] = row; // 把 row; 写入 board[col]
        place(col + 1); // place(col 加 1);
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
      [1, 5, 8, 6, 3, 7, 2, 4],
    ],
    [
      1,
      1,
      [1],
    ],
    [2, 0, null],
    [
      4,
      2,
      [2, 4, 1, 3],
    ],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 cases.长度 就继续
    final c = cases[idx]; // 把 cases[idx] 存入 字符
    final sols = nQueensSafe(
      c[0] as int,
    ); // 把 nQueensSafe(字符[0] as int) 存入 sols
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
