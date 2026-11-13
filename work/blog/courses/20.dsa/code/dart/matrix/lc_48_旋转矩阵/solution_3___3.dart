// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
// LeetCode 48. 旋转矩阵 — Dart 版

/// 方案3：先上下翻转行（交换行引用），再沿主对角线转置（与 TS 事实源 solution_3 一致）
void rotate(List<List<int>> matrix) {
  // 定义函数/方法 rotate
  final n = matrix.length; // 把 矩阵.长度 存入 元素个数
  for (var i = 0; i < n ~/ 2; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 ~ 除以 2 就继续
    final tmp = matrix[i]; // 把 矩阵[下标 i] 存入 临时变量
    matrix[i] = matrix[n - 1 - i]; // 把 矩阵[元素个数 减 1 减 下标 i]; 写入 matrix[i]
    matrix[n - 1 - i] = tmp; // 把 临时变量; 写入 matrix[n - 1 - i]
  }
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (var j = 0; j < i; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
      final tmp = matrix[i][j]; // 把 矩阵[下标 i][下标 j] 存入 临时变量
      matrix[i][j] = matrix[j][i]; // 把 矩阵[下标 j][下标 i]; 写入 matrix[i][j]
      matrix[j][i] = tmp; // 把 临时变量; 写入 matrix[j][i]
    }
  }
}

bool eqMatrix(List<List<int>> a, List<List<int>> b) {
  // 定义函数/方法 eqMatrix
  if (a.length != b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (var i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i].length != b[i].length)
      return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
    for (var j = 0; j < a[i].length; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
      if (a[i][j] != b[i][j])
        return false; // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]，直接返回 false
    }
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 事实源内嵌用例一致（LeetCode 官方示例）
  final inputs = <List<List<int>>>[
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ],
    [
      [5, 1, 9, 11],
      [2, 4, 8, 10],
      [13, 3, 6, 7],
      [15, 14, 12, 16],
    ],
  ];
  final expecteds = <List<List<int>>>[
    [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3],
    ],
    [
      [15, 13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7, 10, 11],
    ],
  ];
  for (var idx = 0; idx < inputs.length; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 inputs.长度 就继续
    rotate(inputs[idx]); // rotate(inputs[idx]);
    if (!eqMatrix(inputs[idx], expecteds[idx])) {
      // 若 取反 eqMatrix(inputs[idx], expecteds[idx]
      throw StateError(
        'case $idx failed',
      ); // throw StateError('case $idx failed');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
