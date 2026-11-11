// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案4：八皇后显式栈迭代）
bool valid(int x, List<int> a) {
  // 定义函数/方法 valid
  final y = a.length + 1; // 把 数组.长度 加 1 存入 y
  for (var i = 1; i <= a.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 数组.长度 就继续
    if (x == a[i - 1] || (y - i).abs() == (x - a[i - 1]).abs()) {
      return false; // 返回 false
    }
  }
  return true; // 返回 true
}

List<List<int>> nQueensStack(int n) {
  // 定义函数/方法 nQueensStack
  final solutions = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 solutions
  final stack = <List<int>>[
    <int>[],
  ]; // 把 小于 List 小于 int 超过 超过 [ 小于 int 超过 []] 存入 栈
  while (stack.isNotEmpty) {
    // 循环，直到不满足「栈.isNotEmpty」
    final a = stack.removeLast(); // 把 栈.removeLast() 存入 数组
    if (a.length == n) {
      // 若 数组.长度 等于 元素个数
      solutions.add(a); // solutions 追加 数组);
    } else {
      // 否则
      for (var i = 1; i <= n; i++) {
        // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
        if (valid(i, a)) {
          // 若 valid(下标 i, 数组
          final b = List<int>.from(a); // 把 List 小于 int 超过 .from(数组) 存入 b
          b.add(i); // b 追加 下标 i);
          stack.add(b); // 栈 追加 b);
        }
      }
    }
  }
  return solutions; // 返回 solutions
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = <List<dynamic>>[
    [
      8,
      92,
      [8, 4, 1, 3, 6, 2, 7, 5],
    ],
    [
      1,
      1,
      [1],
    ],
    [2, 0, null],
    [
      4,
      2,
      [3, 1, 4, 2],
    ],
  ];
  for (var idx = 0; idx < cases.length; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 cases.长度 就继续
    final c = cases[idx]; // 把 cases[idx] 存入 字符
    final sols = nQueensStack(
      c[0] as int,
    ); // 把 nQueensStack(字符[0] as int) 存入 sols
    if (sols.length != c[1] as int) throw StateError('case $idx count');
    if (c[2] != null && sols[0].toString() != c[2].toString()) {
      // 若 字符[2] 不等于 null 且 sols[0].toString() 不等于 字符[2].toString(
      throw StateError(
        'case $idx first',
      ); // throw StateError('case $idx first');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
