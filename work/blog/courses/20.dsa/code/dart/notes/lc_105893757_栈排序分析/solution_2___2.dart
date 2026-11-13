// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
// 栈排序分析 — Dart 版（方案2）
List<int> stackSort(List<int> input) {
  // 定义函数/方法 stackSort
  final st = <int>[]; // 把 小于 int 超过 [] 存入 st
  for (final v in input) {
    st.add(v);
  } // for (final 值 in input) { st 追加 值); }
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  while (st.isNotEmpty) {
    out.add(st.removeLast());
  } // 循环，直到不满足「st.isNotEmpty) { out 追加 st.removeLast()); }」
  return out; // 返回 out
}

void main() {
  if (stackSort([3, 1, 5, 2, 4]).toString() != '[4, 2, 5, 1, 3]')
    throw StateError('c1');
  print('PASS');
} // 全部用例通过，输出 PASS
