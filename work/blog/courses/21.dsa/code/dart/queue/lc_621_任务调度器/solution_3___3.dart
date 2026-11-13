// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
// LeetCode 621. 任务调度器 — Dart 版

// 方案3（贪心模拟，每轮取剩余次数最多的 n+1 个，最后一轮只计实际执行数）
int leastInterval(List<String> tasks, int n) {
  // 定义函数/方法 leastInterval
  final count = <String, int>{}; // 把 小于 String, int 超过 {} 存入 计数
  for (final t in tasks) {
    // for (final 另一字符串 in tasks) {
    count[t] = (count[t] ?? 0) + 1; // 把 (计数[另一字符串] ?? 0) 加 1; 写入 count[t]
  }
  var cnt = count.values.toList(); // 把 计数.values.toList() 存入 计数
  var time = 0; // 把 0 存入 time
  while (cnt.isNotEmpty) {
    // 循环，直到不满足「计数.isNotEmpty」
    cnt.sort((a, b) => b.compareTo(a));
    var used = 0; // 把 0 存入 已用标记
    final take = n + 1 < cnt.length
        ? n + 1
        : cnt.length; // 把 元素个数 加 1 小于 计数.长度 ? 元素个数 加 1 : 计数.长度 存入 take
    for (var i = 0; i < take; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 take 就继续
      if (cnt[i] > 0) {
        // 若 计数[下标 i] 超过 0
        cnt[i] -= 1; // cnt[i]累减 1
        used++; // 已用标记 加一
      }
    }
    cnt = cnt.where((c) => c > 0).toList();
    time += cnt.isNotEmpty
        ? n + 1
        : used; // time累加 计数.isNotEmpty ? 元素个数 加 1 : 已用标记
  }
  return time; // 返回 time
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
