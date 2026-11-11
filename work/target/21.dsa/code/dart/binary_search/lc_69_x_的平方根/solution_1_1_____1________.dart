// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Dart 版（1 ) 方案1：二分（精确区间判断））
int mySqrt(int x) {
  // 定义函数/方法 mySqrt
  if (x < 2) return x; // 若 x 小于 2，直接返回 x
  var lo = 1, hi = x ~/ 2; // 把 1, 右边界 赋值为 x ~ 除以 2 存入 左边界
  while (lo <= hi) {
    // 循环，直到不满足「左边界 不超过 右边界」
    final m = lo + (hi - lo) ~/ 2; // 把 左边界 加 (右边界 减 左边界) ~ 除以 2 存入 映射表
    if (m * m <= x && x < (m + 1) * (m + 1))
      return m; // 若 映射表 乘 映射表 不超过 x 且 x 小于 (映射表 加 1) 乘 (映射表 加 1)，直接返回 映射表
    if (m * m > x) {
      hi = m - 1;
    } else {
      lo = m + 1;
    }
  }
  return lo; // 返回 左边界
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<int>>[
    [4, 2],
    [8, 2],
    [16, 4],
    [2147395599, 46339],
  ];
  for (final c in cases) {
    // for (final 字符 in cases) {
    if (mySqrt(c[0]) != c[1]) throw StateError('x=${c[0]}');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
