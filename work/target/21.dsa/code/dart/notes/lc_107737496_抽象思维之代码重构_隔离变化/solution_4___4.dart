// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案4：螺旋矩阵方向模拟 placeFill）
List<List<int>> placeFill(int n) {
  // 定义函数/方法 placeFill
  final m = List.generate(n, (_) => List<int>.filled(n, 0));
  var row = 0, col = 0; // 把 0, col 赋值为 0 存入 row
  var direction = 'D'; // 把 'D' 存入 direction
  var num = 1; // 把 1 存入 num
  final total = n * n; // 把 元素个数 乘 元素个数 存入 总和
  while (num <= total) {
    // 循环，直到不满足「num 不超过 总和」
    m[row][col] = num; // 把 num; 写入 m[row][col]
    num++; // num 加一
    if (direction == 'D') {
      // 若 direction 等于 'D'
      if (row + 1 < n && m[row + 1][col] == 0) {
        // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0
        row++; // row 加一
      } else {
        // 否则
        direction = 'R'; // 把 'R' 存入 direction
        col++; // col 加一
      }
    } else if (direction == 'R') {
      // 否则，若 direction 等于 'R'
      if (col + 1 < n && m[row][col + 1] == 0) {
        // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0
        col++; // col 加一
      } else {
        // 否则
        direction = 'U'; // 把 'U' 存入 direction
        row--; // row 减一
      }
    } else if (direction == 'U') {
      // 否则，若 direction 等于 'U'
      if (row - 1 >= 0 && m[row - 1][col] == 0) {
        // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0
        row--; // row 减一
      } else {
        // 否则
        direction = 'L'; // 把 'L' 存入 direction
        col--; // col 减一
      }
    } else {
      // 否则
      if (col - 1 >= 0 && m[row][col - 1] == 0) {
        // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0
        col--; // col 减一
      } else {
        // 否则
        direction = 'D'; // 把 'D' 存入 direction
        row++; // row 加一
      }
    }
  }
  return m; // 返回 映射表
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (placeFill(3).toString() != '[[1, 8, 7], [2, 9, 6], [3, 4, 5]]') {
    throw StateError('place3 failed'); // throw StateError('place3 failed');
  }
  if (placeFill(4).toString() !=
      '[[1, 12, 11, 10], [2, 13, 16, 9], [3, 14, 15, 8], [4, 5, 6, 7]]') {
    throw StateError('place4 failed'); // throw StateError('place4 failed');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
