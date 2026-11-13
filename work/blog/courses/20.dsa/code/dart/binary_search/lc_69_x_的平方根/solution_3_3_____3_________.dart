// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145299731
// LeetCode 69. x 的平方根 — Dart 版（3 ) 方案3：牛顿迭代）
int mySqrt(int x) {
  // 定义函数/方法 mySqrt
  if (x < 2) return x; // 若 x 小于 2，直接返回 x
  var r = x; // 把 x 存入 右指针
  while (r * r > x) {
    // 循环，直到不满足「右指针 乘 右指针 超过 x」
    r = (r + x ~/ r) ~/ 2; // 把 (右指针 加 x ~ 除以 右指针) ~ 除以 2 存入 右指针
  }
  return r; // 返回 右指针
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
