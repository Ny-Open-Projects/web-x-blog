// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
// 数据结构与算法之排序: 基数排序 — Dart 版（方案1）
List<int> radixSort(List<int> nums) {
  // 定义函数/方法 radixSort
  if (nums.isEmpty) return nums; // 若 数组.isEmpty，直接返回 数组
  var mn = nums[0], mx = nums[0]; // 把 数组[0], mx 赋值为 数组[0] 存入 mn
  for (final v in nums) {
    if (v < mn) mn = v;
    if (v > mx) mx = v;
  }
  final offset = mn < 0 ? -mn : 0; // 把 mn 小于 0 ? 减 mn : 0 存入 offset
  final adj = nums.map((v) => v + offset).toList();
  var maxAdj = adj[0]; // 把 邻接表[0] 存入 maxAdj
  for (final v in adj) {
    if (v > maxAdj) maxAdj = v;
  } // 把 值; } 写入 for (final v in adj) { if (v > maxAdj) maxAdj
  var radix = 1; // 把 1 存入 radix
  final tmp = List<int>.filled(
    adj.length,
    0,
  ); // 把 List 小于 int 超过 .filled(邻接表.长度, 0) 存入 临时变量
  while (maxAdj >= radix) {
    // 循环，直到不满足「maxAdj 不低于 radix」
    final bucket = List<int>.filled(
      10,
      0,
    ); // 把 List 小于 int 超过 .filled(10, 0) 存入 bucket
    for (final v in adj) {
      bucket[(v ~/ radix) % 10]++;
    } // for (final 值 in 邻接表) { bucket[(值 ~ 除以 radix) 对…取模 10] 加一 ; }
    for (var i = 1; i < 10; i++) {
      bucket[i] += bucket[i - 1];
    } // 让 下标 i 从 1 开始计数，下标 i 小于 10 就继续
    for (var i = adj.length - 1; i >= 0; i--) {
      // 让 下标 i 从 邻接表.长度 减 1 开始计数，下标 i 不低于 0 就继续
      tmp[--bucket[(adj[i] ~/ radix) % 10]] =
          adj[i]; // 把 邻接表[下标 i]; 写入 tmp[--bucket[(adj[i] ~/ radix) % 10]]
    }
    for (var i = 0; i < adj.length; i++) {
      adj[i] = tmp[i];
    } // 让 下标 i 从 0 开始计数，下标 i 小于 邻接表.长度 就继续
    radix *= 10; // 把 10; 写入 radix *
  }
  return adj.map((x) => x - offset).toList();
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (radixSort([5, 4, 3, 2, 1]).toString() != '[1, 2, 3, 4, 5]')
    throw StateError('c1');
  if (radixSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]).toString() !=
      '[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
