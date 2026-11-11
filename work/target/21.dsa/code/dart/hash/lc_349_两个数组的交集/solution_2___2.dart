// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135064368
// LeetCode 349. 两个数组的交集 — Dart 版（方案2）
List<int> intersection(List<int> nums1, List<int> nums2) {
  // 定义函数/方法 intersection
  final s1 = nums1.toSet(); // 把 数组1.toSet() 存入 s1
  final seen = <int>{}; // 把 小于 int 超过 {} 存入 已见集合
  final res = <int>[]; // 把 小于 int 超过 [] 存入 结果
  for (final v in nums2) {
    // for (final 值 in 数组2) {
    if (s1.contains(v) && !seen.contains(v)) {
      // 若 s1 是否包含 值) 且 取反 已见集合 是否包含 值
      res.add(v); // 结果 追加 值);
      seen.add(v); // 已见集合 追加 值);
    }
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (intersection([1, 2, 2, 1], [2, 2]).toString() != '[2]')
    throw StateError('c1');
  if (intersection([4, 9, 5], [9, 4, 9, 8, 4]).toString() != '[9, 4]')
    throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
