// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
// 字典序最大问题分析 — Dart 版（方案4）
List<int> lexicographicallyLargest(int n, List<int> arr) {
  // 定义函数/方法 lexicographicallyLargest
  final v = List<int>.from(arr)..sort((a, b) => b.compareTo(a));
  return v.sublist(0, n); // 返回 值.sublist(0, 元素个数)
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (lexicographicallyLargest(3, [1, 2, 3]).toString() != '[3, 2, 1]')
    throw StateError('c1');
  if (lexicographicallyLargest(4, [4, 2, 9, 7]).toString() != '[9, 7, 4, 2]')
    throw StateError('c2');
  if (lexicographicallyLargest(2, [5, 1]).toString() != '[5, 1]')
    throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
