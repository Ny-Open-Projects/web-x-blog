// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — Dart 版（方案A：逐行高度 + 暴力区间 / 卡片扩展）
int getResult(int n, int m, List<String> matrix) {
  // 定义函数/方法 getResult
  var ans = 0; // 把 0 存入 答案
  final height = List<int>.filled(
    m + 2,
    0,
  ); // 把 List 小于 int 超过 .filled(映射表 加 2, 0) 存入 height
  for (var k = 0; k < n; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    for (var i = 1; i <= m; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      if (matrix[k][i - 1] == '.') {
        // 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
        height[i] += 1; // height[i]累加 1
      } else {
        // 否则
        height[i] = 0; // 把 0; 写入 height[i]
      }
    }
    for (var a = 1; a <= m; a++) {
      // 让 数组 从 1 开始计数，数组 不超过 映射表 就继续
      var minH = 50000; // 把 50000 存入 minH
      for (var c = a; c <= m; c++) {
        // 让 字符 从 数组 开始计数，字符 不超过 映射表 就继续
        if (height[c] < minH)
          minH = height[c]; // 若 height[字符] 小于 minH) minH 赋值为 height[字符];
      }
      final area = (m - a + 1) * minH; // 把 (映射表 减 数组 加 1) 乘 minH 存入 area
      if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
    }
  }
  return ans; // 返回 答案
}

int getResultCard(int n, int m, List<String> matrix) {
  // 定义函数/方法 getResultCard
  var ans = 0; // 把 0 存入 答案
  final height = List<int>.filled(
    m + 2,
    0,
  ); // 把 List 小于 int 超过 .filled(映射表 加 2, 0) 存入 height
  for (var k = 0; k < n; k++) {
    // 让 下标 k 从 0 开始计数，下标 k 小于 元素个数 就继续
    for (var i = 1; i <= m; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
      if (matrix[k][i - 1] == '.') {
        // 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
        height[i] += 1; // height[i]累加 1
      } else {
        // 否则
        height[i] = 0; // 把 0; 写入 height[i]
      }
    }
    for (var a = 1; a <= m; a++) {
      // 让 数组 从 1 开始计数，数组 不超过 映射表 就继续
      final curH = height[a]; // 把 height[数组] 存入 curH
      var lo = a - 1; // 把 数组 减 1 存入 左边界
      while (lo >= 1 && height[lo] >= curH) {
        // 循环，直到不满足「左边界 不低于 1 且 height[左边界] 不低于 curH」
        lo--; // 左边界 减一
      }
      var hi = a + 1; // 把 数组 加 1 存入 右边界
      while (hi <= m && height[hi] >= curH) {
        // 循环，直到不满足「右边界 不超过 映射表 且 height[右边界] 不低于 curH」
        hi++; // 右边界 加一
      }
      final area = (hi - lo - 1) * curH; // 把 (右边界 减 左边界 减 1) 乘 curH 存入 area
      if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
    }
  }
  return ans; // 返回 答案
}

void main() {
  // 程序入口：跑内嵌自测用例
  const matrix = <String>[
    '.....',
    'XXXXX',
    '.X...',
    '.....',
  ]; // 把 小于 String 超过 ['.....', 'XXXXX', '.X...', '.....'] 存入 矩阵
  if (getResult(4, 5, matrix) != 6) throw StateError('brute failed');
  if (getResultCard(4, 5, matrix) != 6) throw StateError('card failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
