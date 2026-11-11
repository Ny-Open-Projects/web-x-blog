// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134204437
// LeetCode 79. 单词搜索 — Dart 版（方案2）
bool exist(List<List<String>> board, String word) {
  // 定义函数/方法 exist
  final rows = board.length,
      cols = board[0].length; // 把 棋盘.长度, 列数 赋值为 棋盘[0].长度 存入 行数
  final w = word.split(''); // 把 单词.split('') 存入 权重
  bool dfs(int i, int j, int k) {
    // 定义函数/方法 dfs
    if (k == w.length) return true; // 若 下标 k 等于 权重.长度，直接返回 true
    if (i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != w[k])
      return false;
    final saved = board[i][j]; // 把 棋盘[下标 i][下标 j] 存入 saved
    board[i][j] = '#'; // 把 '#'; 写入 board[i][j]
    final found =
        dfs(i + 1, j, k + 1) ||
        dfs(i - 1, j, k + 1) ||
        dfs(i, j + 1, k + 1) ||
        dfs(i, j - 1, k + 1);
    board[i][j] = saved; // 把 saved; 写入 board[i][j]
    return found; // 返回 found
  }

  for (var i = 0; i < rows; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 行数 就继续
    for (var j = 0; j < cols; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 列数 就继续
      if (dfs(i, j, 0)) return true; // 若 dfs(下标 i, 下标 j, 0)，直接返回 true
    }
  }
  return false; // 返回 false
}

void main() {
  // 程序入口：跑内嵌自测用例
  final b = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
  ];
  if (!exist(b, 'ABCCED'))
    throw StateError('c1'); // 若 取反 exist(b, 'ABCCED')) throw StateError('c1');
  if (!exist(b, 'SEE'))
    throw StateError('c2'); // 若 取反 exist(b, 'SEE')) throw StateError('c2');
  if (exist(b, 'ABCB'))
    throw StateError('c3'); // 若 exist(b, 'ABCB')) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
