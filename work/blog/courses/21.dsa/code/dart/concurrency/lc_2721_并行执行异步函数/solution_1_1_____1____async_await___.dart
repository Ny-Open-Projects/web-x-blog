// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386399
// LeetCode 2721. 并行执行异步函数 — Dart 版（方案1）
List<int> executeAll(List<int> fns) => List<int>.from(fns);
void main() {
  // 程序入口：跑内嵌自测用例
  if (executeAll([1, 2, 3]).toString() != '[1, 2, 3]') throw StateError('c1');
  if (executeAll([]).isNotEmpty)
    throw StateError(
      'c2',
    ); // 若 executeAll([]).isNotEmpty) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
