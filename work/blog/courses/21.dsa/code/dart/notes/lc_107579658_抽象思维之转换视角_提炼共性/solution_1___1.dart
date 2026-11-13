// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
// LeetCode 107579658. 转换视角，提炼共性 — Dart 版（抽象思维之转换视角：统一分书问题与八皇后的回溯框架）
// queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
const LIKE = [
  [0, 0, 1, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 1],
];

List<List<int>> solveUnified(bool queen) {
  // 定义函数/方法 solveUnified
  final size = queen ? 8 : 5; // 把 queen ? 8 : 5 存入 大小
  final q = List<int>.filled(
    size,
    -1,
  ); // 把 List 小于 int 超过 .filled(大小, 减 1) 存入 节点
  final rows = List<bool>.filled(
    size,
    true,
  ); // 把 List 小于 bool 超过 .filled(大小, true) 存入 行数
  final diag1 = List<bool>.filled(
    2 * size - 1,
    true,
  ); // 把 List 小于 bool 超过 .filled(2 乘 大小 减 1, true) 存入 diag1
  final diag2 = List<bool>.filled(
    2 * size - 1,
    true,
  ); // 把 List 小于 bool 超过 .filled(2 乘 大小 减 1, true) 存入 diag2
  final results = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 results

  bool isValid(int row, int col) {
    // 定义判定函数 isValid
    if (queen) return true; // 若 queen，直接返回 true
    return LIKE[row][col] == 1; // 返回 LIKE[row][col] 等于 1
  }

  bool isSafe(int row, int col) {
    // 定义判定函数 isSafe
    if (queen)
      return rows[row] && diag1[col + size - 1 - row] && diag2[col + row];
    return rows[row]; // 返回 行数[row]
  }

  void place(int col) {
    // 定义函数/方法 place
    if (col == size) {
      // 若 col 等于 大小
      results.add(List<int>.from(q)); // results 追加 List 小于 int 超过 .from(节点));
      return; // return;
    }
    for (var row = 0; row < size; row++) {
      // 让 row 从 0 开始计数，row 小于 大小 就继续
      if (!isValid(row, col)) continue; // 若 取反 isValid(row, col)) continue;
      if (!isSafe(row, col)) continue; // 若 取反 isSafe(row, col)) continue;
      q[col] = row; // 把 row; 写入 q[col]
      rows[row] = false; // 把 false; 写入 rows[row]
      if (queen) {
        // 若 queen
        diag1[col + size - 1 - row] =
            false; // 把 false; 写入 diag1[col + size - 1 - row]
        diag2[col + row] = false; // 把 false; 写入 diag2[col + row]
      }
      place(col + 1); // place(col 加 1);
      rows[row] = true; // 把 true; 写入 rows[row]
      if (queen) {
        // 若 queen
        diag1[col + size - 1 - row] =
            true; // 把 true; 写入 diag1[col + size - 1 - row]
        diag2[col + row] = true; // 把 true; 写入 diag2[col + row]
      }
    }
  }

  place(0); // place(0);
  return results; // 返回 results
}

void main() {
  // 程序入口：跑内嵌自测用例
  final want = <List<int>>[
    [1, 2, 0, 3, 4],
    [1, 4, 0, 3, 2],
  ];
  final got = solveUnified(false); // 把 solveUnified(false) 存入 got
  if (got.toString() != want.toString()) {
    // 若 got.toString() 不等于 want.toString(
    throw StateError('solveUnified(false) mismatch: ' + got.toString());
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
