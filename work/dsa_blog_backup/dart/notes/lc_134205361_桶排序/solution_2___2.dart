// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
// 数据结构与算法之排序: 桶排序 — Dart 版（方案2）
int getIndex(List<int> arr, int k) {
  // 定义函数/方法 getIndex
  for (final v in arr) {
    if (v == k) return k;
  } // 把 赋值为 下标 k) return 下标 k; } 写入 for (final v in arr) { if (v
  return -1; // 返回 减 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (getIndex([1, 2, 3], 1) != 1)
    throw StateError(
      'c1',
    ); // 若 getIndex([1,2,3], 1) 不等于 1) throw StateError('c1');
  if (getIndex([1, 2, 3], 3) != 3)
    throw StateError(
      'c2',
    ); // 若 getIndex([1,2,3], 3) 不等于 3) throw StateError('c2');
  if (getIndex([1, 2, 3], 5) != -1)
    throw StateError(
      'c3',
    ); // 若 getIndex([1,2,3], 5) 不等于 减 1) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
