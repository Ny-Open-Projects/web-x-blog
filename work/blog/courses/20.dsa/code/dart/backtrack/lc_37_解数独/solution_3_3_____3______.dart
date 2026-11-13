// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134045157
// LeetCode 37. 解数独 — Dart 版（方案3）
void solveSudoku(List<List<String>> board) {
  // 定义函数/方法 solveSudoku
  bool valid(int r, int c, String ch) {
    // 定义函数/方法 valid
    for (var i = 0; i < 9; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 9 就继续
      if (board[r][i] == ch || board[i][c] == ch)
        return false; // 若 棋盘[右指针][下标 i] 等于 字符 或 棋盘[下标 i][字符] 等于 字符，直接返回 false
    }
    final br = r ~/ 3 * 3,
        bc = c ~/ 3 * 3; // 把 右指针 ~ 除以 3 乘 3, bc 赋值为 字符 ~ 除以 3 乘 3 存入 br
    for (var i = br; i < br + 3; i++) {
      // 让 下标 i 从 br 开始计数，下标 i 小于 br 加 3 就继续
      for (var j = bc; j < bc + 3; j++) {
        // 让 下标 j 从 bc 开始计数，下标 j 小于 bc 加 3 就继续
        if (board[i][j] == ch)
          return false; // 若 棋盘[下标 i][下标 j] 等于 字符，直接返回 false
      }
    }
    return true; // 返回 true
  }

  bool dfs() {
    // 定义函数/方法 dfs
    for (var r = 0; r < 9; r++) {
      // 让 右指针 从 0 开始计数，右指针 小于 9 就继续
      for (var c = 0; c < 9; c++) {
        // 让 字符 从 0 开始计数，字符 小于 9 就继续
        if (board[r][c] == '.') {
          // 若 棋盘[右指针][字符] 等于 '.'
          for (var n = 1; n <= 9; n++) {
            // 让 元素个数 从 1 开始计数，元素个数 不超过 9 就继续
            final ch = n.toString(); // 把 元素个数.toString() 存入 字符
            if (valid(r, c, ch)) {
              // 若 valid(右指针, 字符, 字符
              board[r][c] = ch; // 把 字符; 写入 board[r][c]
              if (dfs()) return true; // 若 dfs()，直接返回 true
              board[r][c] = '.'; // 把 '.'; 写入 board[r][c]
            }
          }
          return false; // 返回 false
        }
      }
    }
    return true; // 返回 true
  }

  dfs(); // dfs();
}

void main() {
  // 程序入口：跑内嵌自测用例
  final board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
  ];
  solveSudoku(board); // solveSudoku(棋盘);
  final solved = [
    '534678912',
    '672195348',
    '198342567',
    '859761423',
    '426853791',
    '713924856',
    '961537284',
    '287419635',
    '345286179',
  ];
  for (var r = 0; r < 9; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 9 就继续
    if (board[r].join() != solved[r]) throw StateError('row $r');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
