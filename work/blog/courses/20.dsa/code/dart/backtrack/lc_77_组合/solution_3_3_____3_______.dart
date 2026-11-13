// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134178290
// LeetCode 77. 组合 — Dart 版（方案3）
List<List<int>> combine(int n, int k) {
  // 定义函数/方法 combine
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  final path = <int>[]; // 把 小于 int 超过 [] 存入 当前路径
  void dfs(int start) {
    // 定义函数/方法 dfs
    if (path.length == k) {
      // 若 当前路径.长度 等于 下标 k
      res.add(List<int>.from(path)); // 结果 追加 List 小于 int 超过 .from(当前路径));
      return; // return;
    }
    for (var i = start; i <= n - (k - path.length) + 1; i++) {
      // 让 下标 i 从 起点 开始计数，下标 i 不超过 元素个数 减 (下标 k 减 当前路径.长度) 加 1 就继续
      path.add(i); // 当前路径 追加 下标 i);
      dfs(i + 1); // dfs(下标 i 加 1);
      path.removeLast(); // 当前路径.removeLast();
    }
  }

  dfs(1); // dfs(1);
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = combine(4, 2); // 把 combine(4, 2) 存入 got
  if (got.length != 6)
    throw StateError('cnt'); // 若 got.长度 不等于 6) throw StateError('计数');
  if (got[0].toString() != '[1, 2]' || got[5].toString() != '[3, 4]')
    throw StateError('c');
  if (combine(1, 1).length != 1)
    throw StateError('c2'); // 若 combine(1, 1).长度 不等于 1) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
