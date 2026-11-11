// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859971
// LeetCode 2050. 并行课程III — Dart 版（方案2）
int minimumTime(int n, List<List<int>> relations, List<int> time) {
  // 定义函数/方法 minimumTime
  final next = <int, List<int>>{}; // 把 小于 int, List 小于 int 超过 超过 {} 存入 下一个
  final indeg = List<int>.filled(
    n + 1,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数 加 1, 0) 存入 indeg
  for (final r in relations) {
    // for (final 右指针 in relations) {
    next.putIfAbsent(r[0], () => []).add(r[1]);
    indeg[r[1]]++; // indeg[右指针[1]] 加一 ;
  }
  final finish = List<int>.filled(
    n + 1,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数 加 1, 0) 存入 finish
  var queue = <int>[]; // 把 小于 int 超过 [] 存入 队列
  for (var c = 1; c <= n; c++) {
    // 让 字符 从 1 开始计数，字符 不超过 元素个数 就继续
    if (indeg[c] == 0) queue.add(c); // 若 indeg[字符] 等于 0) 队列 追加 字符);
  }
  var total = 0; // 把 0 存入 总和
  while (queue.isNotEmpty) {
    // 循环，直到不满足「队列.isNotEmpty」
    final nq = <int>[]; // 把 小于 int 超过 [] 存入 nq
    for (final c in queue) {
      // for (final 字符 in 队列) {
      finish[c] += time[c - 1]; // finish[c]累加 time[字符 减 1]
      if (finish[c] > total)
        total = finish[c]; // 若 finish[字符] 超过 总和) 总和 赋值为 finish[字符];
      for (final nx in next[c] ?? []) {
        // for (final nx in 下一个[字符] ?? []) {
        if (finish[nx] < finish[c]) finish[nx] = finish[c]; // 若 finish[nx] 小于 finish[字符]) finish[nx] 赋值为 finish[字符];
        if (--indeg[nx] == 0) nq.add(nx); // 若 减一 indeg[nx] 等于 0) nq 追加 nx);
      }
    }
    queue = nq; // 把 nq 存入 队列
  }
  return total; // 返回 总和
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (minimumTime(
        3,
        [
          [1, 3],
          [2, 3],
        ],
        [3, 2, 5],
      ) !=
      8)
    throw StateError('c1');
  if (minimumTime(
        5,
        [
          [1, 2],
          [2, 3],
          [3, 4],
          [4, 5],
        ],
        [1, 2, 3, 4, 5],
      ) !=
      15)
    throw StateError('c2');
  if (minimumTime(1, [], [5]) != 5)
    throw StateError(
      'c3',
    ); // 若 minimumTime(1, [], [5]) 不等于 5) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
