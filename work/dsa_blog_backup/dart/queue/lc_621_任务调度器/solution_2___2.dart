// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Dart 版

// 方案2（Counter 公式法）
int leastInterval(List<String> tasks, int n) {
  // 定义函数/方法 leastInterval
  final count = <String, int>{}; // 把 小于 String, int 超过 {} 存入 计数
  for (final t in tasks) {
    // for (final 另一字符串 in tasks) {
    count[t] = (count[t] ?? 0) + 1; // 把 (计数[另一字符串] ?? 0) 加 1; 写入 count[t]
  }
  var maxCount = 0; // 把 0 存入 maxCount
  for (final v in count.values) {
    // for (final 值 in 计数.values) {
    if (v > maxCount) maxCount = v; // 若 值 超过 maxCount) maxCount 赋值为 值;
  }
  var maxCountTasks = 0; // 把 0 存入 maxCountTasks
  for (final v in count.values) {
    // for (final 值 in 计数.values) {
    if (v == maxCount) maxCountTasks++; // 若 值 等于 maxCount) maxCountTasks 加一 ;
  }
  final formula =
      (maxCount - 1) * (n + 1) +
      maxCountTasks; // 把 (maxCount 减 1) 乘 (元素个数 加 1) 加 maxCountTasks 存入 formula
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
