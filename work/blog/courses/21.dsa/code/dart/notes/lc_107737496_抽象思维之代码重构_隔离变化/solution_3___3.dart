// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案3：螺旋矩阵递归填充）
class Matrix {
  // 定义类型
  int n; // int 元素个数;
  List<List<int>> m; // List 小于 List 小于 int 超过 超过 映射表;
  Matrix(this.n) : m = List.generate(n, (_) => List<int>.filled(n, 0));

  void fill(int num, int begin, int size) {
    // 定义函数/方法 fill
    if (size == 0) return; // 若 大小 等于 0) return;
    if (size == 1) {
      // 若 大小 等于 1
      m[begin][begin] = num; // 把 num; 写入 m[begin][begin]
      return; // return;
    }
    for (var j = 0; j < size - 1; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
      m[begin + j][begin] = num; // 把 num; 写入 m[begin + j][begin]
      num++; // num 加一
    }
    for (var j = 0; j < size - 1; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 大小 减 1 就继续
      m[begin + size - 1][begin + j] =
          num; // 把 num; 写入 m[begin + size - 1][begin + j]
      num++; // num 加一
    }
    for (var j = size - 1; j > 0; j--) {
      // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
      m[begin + j][begin + size - 1] =
          num; // 把 num; 写入 m[begin + j][begin + size - 1]
      num++; // num 加一
    }
    for (var j = size - 1; j > 0; j--) {
      // 让 下标 j 从 大小 减 1 开始计数，下标 j 超过 0 就继续
      m[begin][begin + j] = num; // 把 num; 写入 m[begin][begin + j]
      num++; // num 加一
    }
    fill(num, begin + 1, size - 2); // fill(num, begin 加 1, 大小 减 2);
  }
}

String fmtRow(List<int> row) =>
    row.map((x) => x.toString().padLeft(2)).join(' ');

void main() {
  // 程序入口：跑内嵌自测用例
  final m = Matrix(6); // 把 Matrix(6) 存入 映射表
  m.fill(1, 0, 6); // 映射表.fill(1, 0, 6);
  final want = <String>[
    ' 1 20 19 18 17 16',
    ' 2 21 32 31 30 15',
    ' 3 22 33 36 29 14',
    ' 4 23 34 35 28 13',
    ' 5 24 25 26 27 12',
    ' 6  7  8  9 10 11',
  ];
  for (var i = 0; i < 6; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 6 就继续
    final got = fmtRow(m.m[i]); // 把 fmtRow(映射表.映射表[下标 i]) 存入 got
    if (got != want[i]) throw StateError('spiral6 row $i failed');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
