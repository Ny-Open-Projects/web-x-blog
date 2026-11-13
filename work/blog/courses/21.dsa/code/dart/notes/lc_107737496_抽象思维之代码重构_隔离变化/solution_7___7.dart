// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案7：螺旋矩阵分派表 place）
List<int> place(int row, int col, String direction, int n, List<List<int>> m) {
  // 定义函数/方法 place
  final handlers = <String, List<int> Function()>{
    // 把 小于 String, List 小于 int 超过 Function() 超过 { 存入 handlers
    'D': () => (row + 1 < n && m[row + 1][col] == 0)
        ? [row + 1, col]
        : [row, col + 1, 'R'.codeUnitAt(0)],
    'R': () => (col + 1 < n && m[row][col + 1] == 0)
        ? [row, col + 1]
        : [row - 1, col, 'U'.codeUnitAt(0)],
    'U': () => (row - 1 >= 0 && m[row - 1][col] == 0)
        ? [row - 1, col]
        : [row, col - 1, 'L'.codeUnitAt(0)],
    'L': () => (col - 1 >= 0 && m[row][col - 1] == 0)
        ? [row, col - 1]
        : [row + 1, col, 'D'.codeUnitAt(0)],
  };
  return handlers[direction]!(); // 返回 handlers[direction]取反 ()
}

List<List<int>> fillSpiral(int n) {
  // 定义函数/方法 fillSpiral
  final m = List.generate(n, (_) => List<int>.filled(n, 0));
  var row = 0, col = 0; // 把 0, col 赋值为 0 存入 row
  var direction = 'D'; // 把 'D' 存入 direction
  var num = 1; // 把 1 存入 num
  while (num <= n * n) {
    // 循环，直到不满足「num 不超过 元素个数 乘 元素个数」
    m[row][col] = num; // 把 num; 写入 m[row][col]
    num++; // num 加一
    final res = place(
      row,
      col,
      direction,
      n,
      m,
    ); // 把 place(row, col, direction, 元素个数, 映射表) 存入 结果
    row = res[0]; // 把 结果[0] 存入 row
    col = res[1]; // 把 结果[1] 存入 col
    if (res.length == 3)
      direction = String.fromCharCode(
        res[2],
      ); // 若 结果.长度 等于 3) direction 赋值为 String.fromCharCode(结果[2]);
  }
  return m; // 返回 映射表
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (fillSpiral(3).toString() != '[[1, 8, 7], [2, 9, 6], [3, 4, 5]]')
    throw StateError('spiral3 failed');
  if (fillSpiral(4).toString() !=
      '[[1, 12, 11, 10], [2, 13, 16, 9], [3, 14, 15, 8], [4, 5, 6, 7]]') {
    throw StateError('spiral4 failed'); // throw StateError('spiral4 failed');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
