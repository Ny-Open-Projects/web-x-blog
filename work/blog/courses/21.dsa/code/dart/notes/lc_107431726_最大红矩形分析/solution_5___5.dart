// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
// LeetCode 107431726. 最大红矩形分析 — Dart 版（方案E：逐行高度 + 单调栈）
int maxRedRectangle(List<String> matrix) {
  // 定义函数/方法 maxRedRectangle
  final n = matrix.length; // 把 矩阵.长度 存入 元素个数
  final m = matrix[0].length; // 把 矩阵[0].长度 存入 映射表
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
    final stack = <int>[0]; // 把 小于 int 超过 [0] 存入 栈
    for (var i = 1; i <= m + 1; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 加 1 就继续
      final hi = i <= m
          ? height[i]
          : 0; // 把 下标 i 不超过 映射表 ? height[下标 i] : 0 存入 右边界
      while (height[stack.last] > hi) {
        // 循环，直到不满足「height[栈.last] 超过 右边界」
        final nowH =
            height[stack.removeLast()]; // 把 height[栈.removeLast()] 存入 nowH
        final width = i - stack.last - 1; // 把 下标 i 减 栈.last 减 1 存入 width
        final area = nowH * width; // 把 nowH 乘 width 存入 area
        if (area > ans) ans = area; // 若 area 超过 答案) 答案 赋值为 area;
      }
      stack.add(i); // 栈 追加 下标 i);
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
  if (maxRedRectangle(matrix) != 6) throw StateError('mono failed');
  if (maxRedRectangle(<String>['...', '...', '...']) != 9)
    throw StateError('all dots failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
