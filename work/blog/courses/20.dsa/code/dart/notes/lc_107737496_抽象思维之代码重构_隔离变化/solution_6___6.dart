// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案6：Matrix 公开 buf 直接访问）
class Matrix {
  // 定义类型
  int row, col; // int row, col;
  List<List<int>> buf; // List 小于 List 小于 int 超过 超过 buf;
  Matrix(this.row, this.col) // Matrix(this.row, this.col)
    : buf = List.generate(row, (_) => List<int>.filled(col, 0));

  int call(int r, int c) {
    // 定义函数/方法 call
    return buf[r][c]; // 返回 buf[右指针][字符]
  }
}

void main() {
  // 程序入口：跑内嵌自测用例
  final m = Matrix(4, 5); // 把 Matrix(4, 5) 存入 映射表
  for (var i = 0; i < 4; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
    for (var j = 0; j < 5; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 5 就继续
      m.buf[i][j] = i * j; // 直接访问 buf
    }
  }
  if (m.call(2, 3) != 6)
    throw StateError(
      'matrix call failed',
    ); // 若 映射表.call(2, 3) 不等于 6) throw StateError('矩阵 call failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
