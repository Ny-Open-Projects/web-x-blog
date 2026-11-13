// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133865307
// LeetCode 39. 组合总和 — Dart 版（方案2）
List<List<int>> combinationSum(List<int> candidates, int target) {
  // 定义函数/方法 combinationSum
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  final path = <int>[]; // 把 小于 int 超过 [] 存入 当前路径
  void dfs(int start, int remaining) {
    // 定义函数/方法 dfs
    if (remaining == 0) {
      // 若 remaining 等于 0
      res.add(List<int>.from(path)); // 结果 追加 List 小于 int 超过 .from(当前路径));
      return; // return;
    }
    if (remaining < 0) return; // 若 remaining 小于 0) return;
    for (var i = start; i < candidates.length; i++) {
      // 让 下标 i 从 起点 开始计数，下标 i 小于 候选数组.长度 就继续
      path.add(candidates[i]); // 当前路径 追加 候选数组[下标 i]);
      dfs(i, remaining - candidates[i]); // dfs(下标 i, remaining 减 候选数组[下标 i]);
      path.removeLast(); // 当前路径.removeLast();
    }
  }

  dfs(0, target); // dfs(0, 目标值);
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = combinationSum([
    2,
    3,
    6,
    7,
  ], 7); // 把 combinationSum([2, 3, 6, 7], 7) 存入 got
  if (got.length != 2)
    throw StateError('cnt'); // 若 got.长度 不等于 2) throw StateError('计数');
  if (got[0].toString() != '[2, 2, 3]' || got[1].toString() != '[7]')
    throw StateError('a');
  final got2 = combinationSum([
    2,
    3,
    5,
  ], 8); // 把 combinationSum([2, 3, 5], 8) 存入 got2
  if (got2.length != 3)
    throw StateError('c2'); // 若 got2.长度 不等于 3) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
