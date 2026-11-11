// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133904873
// LeetCode 148. 排序链表 — Dart 版（方案1）
List<int> sortList(List<int> vals) {
  // 定义函数/方法 sortList
  final v = List<int>.from(vals)
    ..sort(); // 把 List 小于 int 超过 .from(vals). 排序 ) 存入 值
  return v; // 返回 值
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (sortList([4, 2, 1, 3]).toString() != '[1, 2, 3, 4]')
    throw StateError('c1');
  if (sortList([-1, 5, 3, 4, 0]).toString() != '[-1, 0, 3, 4, 5]')
    throw StateError('c2');
  if (sortList([]).isNotEmpty)
    throw StateError(
      'c3',
    ); // 若 sortList([]).isNotEmpty) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
