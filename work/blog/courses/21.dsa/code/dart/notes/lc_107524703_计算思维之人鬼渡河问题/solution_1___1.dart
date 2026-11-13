// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Dart 版（方案1：安全判定谓词）
bool isSafe(int r, int g) {
  // 定义判定函数 isSafe
  return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<dynamic>>[
    [3, 3, true],
    [3, 1, true],
    [2, 2, true],
    [1, 3, false],
    [0, 0, true],
  ];
  for (var i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    final c = cases[i]; // 把 cases[下标 i] 存入 字符
    if (isSafe(c[0] as int, c[1] as int) != c[2] as bool) {
      // 若 isSafe(字符[0] as int, 字符[1] as int) 不等于 字符[2] as bool
      throw StateError(
        'is_safe(${c[0]},${c[1]}) failed',
      ); // throw StateError('is_safe(${字符[0]},${字符[1]}) failed');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
