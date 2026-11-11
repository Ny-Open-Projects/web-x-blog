// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
// 数据结构与算法之查找: 顺序查找 — Dart 版（方案3）
int seqSearch(List<int> arr, int key) {
  // 定义函数/方法 seqSearch
  for (var i = 0; i < arr.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (arr[i] == key) return i; // 若 数组[下标 i] 等于 key，直接返回 下标 i
  }
  return -1; // 返回 减 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (seqSearch([1, 2, 3], 1) != 0)
    throw StateError(
      'c1',
    ); // 若 seqSearch([1, 2, 3], 1) 不等于 0) throw StateError('c1');
  if (seqSearch([1, 2, 3], 2) != 1)
    throw StateError(
      'c2',
    ); // 若 seqSearch([1, 2, 3], 2) 不等于 1) throw StateError('c2');
  if (seqSearch([1, 2, 3], 4) != -1)
    throw StateError(
      'c3',
    ); // 若 seqSearch([1, 2, 3], 4) 不等于 减 1) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
