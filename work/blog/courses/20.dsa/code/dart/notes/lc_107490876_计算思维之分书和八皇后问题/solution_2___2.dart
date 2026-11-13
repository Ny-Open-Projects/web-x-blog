// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Dart 版（方案2：分书，函数式不可变副本）
const like = [
  [0, 0, 1, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 1],
];

List<List<int>> allocateBooksFunc() {
  // 定义函数/方法 allocateBooksFunc
  final results = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 results

  void tryAssign(int reader, List<int> assigned) {
    // 定义函数/方法 tryAssign
    if (reader == 5) {
      // 若 reader 等于 5
      results.add(assigned); // results 追加 assigned);
      return; // return;
    }
    for (var book = 0; book < 5; book++) {
      // 让 book 从 0 开始计数，book 小于 5 就继续
      if (like[reader][book] == 1 && assigned[book] == -1) {
        // 若 like[reader][book] 等于 1 且 assigned[book] 等于 减 1
        final nxt = List<int>.from(
          assigned,
        ); // 把 List 小于 int 超过 .from(assigned) 存入 nxt
        nxt[book] = reader; // 把 reader; 写入 nxt[book]
        tryAssign(reader + 1, nxt); // tryAssign(reader 加 1, nxt);
      }
    }
  }

  tryAssign(0, <int>[
    -1,
    -1,
    -1,
    -1,
    -1,
  ]); // tryAssign(0, 小于 int 超过 [ 减 1, 减 1, 减 1, 减 1, 减 1]);
  return results; // 返回 results
}

void main() {
  // 程序入口：跑内嵌自测用例
  final want = <List<int>>[
    [1, 2, 0, 3, 4],
    [1, 4, 0, 3, 2],
  ];
  final res = allocateBooksFunc(); // 把 allocateBooksFunc() 存入 结果
  if (res.toString() != want.toString()) throw StateError('mismatch');
  print('PASS'); // 全部用例通过，输出 PASS
}
