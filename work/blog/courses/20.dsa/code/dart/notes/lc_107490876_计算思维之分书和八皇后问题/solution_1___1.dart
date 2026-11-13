// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案1：分书，共享 assigned + 回溯）
const like = [
  [0, 0, 1, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 1],
];

List<List<int>> allocateBooks() {
  // 定义函数/方法 allocateBooks
  final results = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 results
  final assigned = <int>[
    -1,
    -1,
    -1,
    -1,
    -1,
  ]; // 把 小于 int 超过 [ 减 1, 减 1, 减 1, 减 1, 减 1] 存入 assigned

  void tryAssign(int reader) {
    // 定义函数/方法 tryAssign
    if (reader == 5) {
      // 若 reader 等于 5
      results.add(
        List<int>.from(assigned),
      ); // results 追加 List 小于 int 超过 .from(assigned));
      return; // return;
    }
    for (var book = 0; book < 5; book++) {
      // 让 book 从 0 开始计数，book 小于 5 就继续
      if (like[reader][book] == 1 && assigned[book] == -1) {
        // 若 like[reader][book] 等于 1 且 assigned[book] 等于 减 1
        assigned[book] = reader; // 把 reader; 写入 assigned[book]
        tryAssign(reader + 1); // tryAssign(reader 加 1);
        assigned[book] = -1; // 回溯
      }
    }
  }

  tryAssign(0); // tryAssign(0);
  return results; // 返回 results
}

void main() {
  // 程序入口：跑内嵌自测用例
  final want = <List<int>>[
    [1, 2, 0, 3, 4],
    [1, 4, 0, 3, 2],
  ];
  final res = allocateBooks(); // 把 allocateBooks() 存入 结果
  if (res.toString() != want.toString()) {
    // 若 结果.toString() 不等于 want.toString(
    throw StateError(
      'mismatch: ' + res.toString(),
    ); // throw StateError('mismatch: ' 加 结果.toString());
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
