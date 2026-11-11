// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
// LeetCode 54. 螺旋矩阵 — Dart 版

/// 方案1：四边界逐层收缩
List<int> spiralOrder(List<List<int>> matrix) {
  // 定义函数/方法 spiralOrder
  if (matrix.isEmpty || matrix[0].isEmpty)
    return []; // 若 矩阵.isEmpty 或 矩阵[0].isEmpty，直接返回 []
  final result = <int>[]; // 把 小于 int 超过 [] 存入 结果
  var top = 0,
      bottom = matrix.length - 1,
      left = 0,
      right = matrix[0].length - 1;
  while (top <= bottom && left <= right) {
    // 循环，直到不满足「top 不超过 bottom 且 左边界 不超过 右边界」
    for (var i = left; i <= right; i++)
      result.add(matrix[top][i]); // 让 下标 i 从 左边界 开始计数，下标 i 不超过 右边界 就继续
    top++; // top 加一
    for (var i = top; i <= bottom; i++)
      result.add(matrix[i][right]); // 让 下标 i 从 top 开始计数，下标 i 不超过 bottom 就继续
    right--; // 右边界 减一
    if (top <= bottom) {
      // 若 top 不超过 bottom
      for (var i = right; i >= left; i--)
        result.add(matrix[bottom][i]); // 让 下标 i 从 右边界 开始计数，下标 i 不低于 左边界 就继续
      bottom--; // bottom 减一
    }
    if (left <= right) {
      // 若 左边界 不超过 右边界
      for (var i = bottom; i >= top; i--)
        result.add(matrix[i][left]); // 让 下标 i 从 bottom 开始计数，下标 i 不低于 top 就继续
      left++; // 左边界 加一
    }
  }
  return result; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 事实源内嵌用例一致：空矩阵
  if (spiralOrder([]).isNotEmpty) {
    // 若 spiralOrder([]).isNotEmpty
    throw StateError('FAILED empty'); // throw StateError('FAILED empty');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
