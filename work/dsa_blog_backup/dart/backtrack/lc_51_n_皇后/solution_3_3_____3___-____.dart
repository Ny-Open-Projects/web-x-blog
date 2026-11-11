// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133970744
// LeetCode 51. N皇后 — Dart 版（方案3）
List<List<String>> solveNQueens(int n) {
  // 定义函数/方法 solveNQueens
  final res = <List<String>>[]; // 把 小于 List 小于 String 超过 超过 [] 存入 结果
  final cols = List<int>.filled(
    n,
    -1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 减 1) 存入 列数
  void dfs(int row) {
    // 定义函数/方法 dfs
    if (row == n) {
      // 若 row 等于 元素个数
      final board = <String>[]; // 把 小于 String 超过 [] 存入 棋盘
      for (var r = 0; r < n; r++) {
        // 让 右指针 从 0 开始计数，右指针 小于 元素个数 就继续
        final line = List<String>.generate(n, (c) => cols[r] == c ? 'Q' : '.');
        board.add(line.join()); // 拼接为字符串
      }
      res.add(board); // 结果 追加 棋盘);
      return; // return;
    }
    for (var col = 0; col < n; col++) {
      // 让 col 从 0 开始计数，col 小于 元素个数 就继续
      var valid = true; // 把 true 存入 valid
      for (var r = 0; r < row; r++) {
        // 让 右指针 从 0 开始计数，右指针 小于 row 就继续
        if (cols[r] == col || (r - row).abs() == (cols[r] - col).abs()) {
          valid = false; // 把 false 存入 valid
          break; // 跳出循环
        }
      }
      if (valid) {
        // 若 valid
        cols[row] = col; // 把 col; 写入 cols[row]
        dfs(row + 1); // dfs(row 加 1);
        cols[row] = -1; // 把 减 1; 写入 cols[row]
      }
    }
  }

  dfs(0); // dfs(0);
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = solveNQueens(4); // 把 solveNQueens(4) 存入 got
  if (got.length != 2)
    throw StateError('cnt'); // 若 got.长度 不等于 2) throw StateError('计数');
  if (got[0][0] != '.Q..' || got[0][3] != '..Q.' || got[1][0] != '..Q.')
    throw StateError('b');
  if (solveNQueens(1).length != 1)
    throw StateError(
      'c2',
    ); // 若 solveNQueens(1).长度 不等于 1) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
