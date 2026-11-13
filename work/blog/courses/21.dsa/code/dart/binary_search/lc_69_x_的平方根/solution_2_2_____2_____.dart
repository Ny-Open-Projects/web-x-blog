// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Dart 版（2 ) 方案2：二分（保留 ans））
int mySqrt(int x) {
  // 定义函数/方法 mySqrt
  var lo = 0, hi = x, ans = 0; // 把 0, 右边界 赋值为 x, 答案 赋值为 0 存入 左边界
  while (lo <= hi) {
    // 循环，直到不满足「左边界 不超过 右边界」
    final m = lo + (hi - lo) ~/ 2; // 把 左边界 加 (右边界 减 左边界) ~ 除以 2 存入 映射表
    if (m * m <= x) {
      ans = m;
      lo = m + 1;
    } else {
      hi = m - 1;
    }
  }
  return ans; // 返回 答案
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
