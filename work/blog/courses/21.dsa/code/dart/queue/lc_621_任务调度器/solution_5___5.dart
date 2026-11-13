// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Dart 版

// 方案5（公式法：出现最多的任务 freq 个，有 same 个并列最多，
//        最少时间 = (freq-1)*(n+1) + same，且不能少于任务总数）
int leastInterval(List<String> tasks, int n) {
  // 定义函数/方法 leastInterval
  final cnt = <String, int>{}; // 把 小于 String, int 超过 {} 存入 计数
  for (final t in tasks) {
    // for (final 另一字符串 in tasks) {
    cnt[t] = (cnt[t] ?? 0) + 1; // 把 (计数[另一字符串] ?? 0) 加 1; 写入 cnt[t]
  }
  var freq = 0; // 把 0 存入 频次表
  for (final v in cnt.values) {
    // for (final 值 in 计数.values) {
    if (v > freq) freq = v; // 若 值 超过 频次表) 频次表 赋值为 值;
  }
  var same = 0; // 把 0 存入 same
  for (final v in cnt.values) {
    // for (final 值 in 计数.values) {
    if (v == freq) same++; // 若 值 等于 频次表) same 加一 ;
  }
  final formula =
      (freq - 1) * (n + 1) + same; // 把 (频次表 减 1) 乘 (元素个数 加 1) 加 same 存入 formula
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
