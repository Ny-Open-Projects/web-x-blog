// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
// LeetCode 347. 前K个高频元素 — Dart 版（方案4）
List<int> topKFrequent(List<int> nums, int k) {
  // 定义函数/方法 topKFrequent
  final counts = <int, int>{}; // 把 小于 int, int 超过 {} 存入 counts
  for (final v in nums) {
    // for (final 值 in 数组) {
    counts[v] = (counts[v] ?? 0) + 1; // 把 (counts[值] ?? 0) 加 1; 写入 counts[v]
  }
  final items =
      counts.entries
          .toList() // 把 counts.entries.toList() 存入 items
        ..sort((a, b) {
          // 排序
          if (a.value != b.value)
            return b.value.compareTo(
              a.value,
            ); // 若 数组.value 不等于 b.value，直接返回 b.value.compareTo(数组.value)
          return a.key.compareTo(b.key); // 返回 数组.key.compareTo(b.key)
        }); // });
  return items.take(k).map((e) => e.key).toList();
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = topKFrequent([1, 1, 1, 2, 2, 3], 2)
    ..sort(); // 把 topKFrequent([1, 1, 1, 2, 2, 3], 2). 排序 ) 存入 got
  if (got.toString() != '[1, 2]')
    throw StateError(
      'c1',
    ); // 若 got.toString() 不等于 '[1, 2]') throw StateError('c1');
  if (topKFrequent([1], 1).toString() != '[1]') throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
