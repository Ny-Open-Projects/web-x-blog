// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Dart 版（方案2：快速选择求第 k 小）
int selectK(List<int> a, int lo, int hi, int k) {
  // 定义函数/方法 selectK
  if (lo == hi) return a[lo]; // 若 左边界 等于 右边界，直接返回 数组[左边界]
  final pivot = a[hi]; // 把 数组[右边界] 存入 pivot
  var i = lo; // 把 左边界 存入 下标 i
  for (var j = lo; j < hi; j++) {
    // 让 下标 j 从 左边界 开始计数，下标 j 小于 右边界 就继续
    if (a[j] <= pivot) {
      // 若 数组[下标 j] 不超过 pivot
      final t = a[i]; // 把 数组[下标 i] 存入 另一字符串
      a[i] = a[j]; // 把 数组[下标 j]; 写入 a[i]
      a[j] = t; // 把 另一字符串; 写入 a[j]
      i++; // 下标 i 加一
    }
  }
  final t = a[i]; // 把 数组[下标 i] 存入 另一字符串
  a[i] = a[hi]; // 把 数组[右边界]; 写入 a[i]
  a[hi] = t; // 把 另一字符串; 写入 a[hi]
  if (i == k) return a[i]; // 若 下标 i 等于 下标 k，直接返回 数组[下标 i]
  if (i > k)
    return selectK(
      a,
      lo,
      i - 1,
      k,
    ); // 若 下标 i 超过 下标 k，直接返回 selectK(数组, 左边界, 下标 i 减 1, 下标 k)
  return selectK(a, i + 1, hi, k); // 返回 selectK(数组, 下标 i 加 1, 右边界, 下标 k)
}

int quickSelect(List<int> arr, int k) {
  // 定义函数/方法 quickSelect
  final a = List<int>.from(arr); // 把 List 小于 int 超过 .from(数组) 存入 数组
  return selectK(a, 0, a.length - 1, k); // 返回 selectK(数组, 0, 数组.长度 减 1, 下标 k)
}

void main() {
  // 程序入口：跑内嵌自测用例
  final base = <int>[
    3,
    1,
    4,
    1,
    5,
    9,
    2,
    6,
  ]; // 把 小于 int 超过 [3, 1, 4, 1, 5, 9, 2, 6] 存入 base
  final ks = <int>[2, 3, 0, 7]; // 把 小于 int 超过 [2, 3, 0, 7] 存入 ks
  final ws = <int>[2, 3, 1, 9]; // 把 小于 int 超过 [2, 3, 1, 9] 存入 ws
  for (var idx = 0; idx < 4; idx++) {
    // 让 idx 从 0 开始计数，idx 小于 4 就继续
    final got = quickSelect(
      base,
      ks[idx],
    ); // 把 quickSelect(base, ks[idx]) 存入 got
    if (got != ws[idx])
      throw StateError('case $idx failed: got $got want ${ws[idx]}');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
