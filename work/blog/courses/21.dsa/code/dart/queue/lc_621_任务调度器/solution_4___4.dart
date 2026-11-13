// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Dart 版

// 方案4（26 位频率桶公式法）
int leastInterval(List<String> tasks, int n) {
  // 定义函数/方法 leastInterval
  final freq = List<int>.filled(
    26,
    0,
  ); // 把 List 小于 int 超过 .filled(26, 0) 存入 频次表
  const a = 65; // 'A'.codeUnitAt(0)
  for (final t in tasks) {
    // for (final 另一字符串 in tasks) {
    freq[t.codeUnitAt(0) - a]++; // 频次表[另一字符串.codeUnitAt(0) 减 数组] 加一 ;
  }
  var maxFreq = 0; // 把 0 存入 maxFreq
  for (final f in freq) {
    // for (final f in 频次表) {
    if (f > maxFreq) maxFreq = f; // 若 f 超过 maxFreq) maxFreq 赋值为 f;
  }
  var same = 0; // 把 0 存入 same
  for (final f in freq) {
    // for (final f in 频次表) {
    if (f == maxFreq) same++; // 若 f 等于 maxFreq) same 加一 ;
  }
  final formula =
      (maxFreq - 1) * (n + 1) +
      same; // 把 (maxFreq 减 1) 乘 (元素个数 加 1) 加 same 存入 formula
  return tasks.length > formula
      ? tasks.length
      : formula; // 返回 tasks.长度 超过 formula ? tasks.长度 : formula
}

void main() {
  // 程序入口：跑内嵌自测用例
  // 与 TS 事实源内嵌用例一致
  final cases = <List<Object>>[
    <Object>[
      ['A', 'A', 'A', 'B', 'B', 'B'],
      2,
      8,
    ],
    <Object>[
      ['A', 'A', 'A', 'A'],
      2,
      10,
    ],
    <Object>[
      ['A', 'B', 'C', 'D'],
      0,
      4,
    ],
  ];
  for (var i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    final got = leastInterval(cases[i][0] as List<String>, cases[i][1] as int);
    if (got != cases[i][2] as int) {
      // 若 got 不等于 cases[下标 i][2] as int
      throw StateError('FAIL case $i got $got want ${cases[i][2]}');
    }
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
