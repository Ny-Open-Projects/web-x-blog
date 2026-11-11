// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133767953
// LeetCode 46. 全排列 — Dart 版（方案2）
List<List<int>> permute(List<int> nums) {
  // 定义函数/方法 permute
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  final used = List<bool>.filled(
    nums.length,
    false,
  ); // 把 List 小于 bool 超过 .filled(数组.长度, false) 存入 已用标记
  final path = <int>[]; // 把 小于 int 超过 [] 存入 当前路径
  void dfs() {
    // 定义函数/方法 dfs
    if (path.length == nums.length) {
      // 若 当前路径.长度 等于 数组.长度
      res.add(List<int>.from(path)); // 结果 追加 List 小于 int 超过 .from(当前路径));
      return; // return;
    }
    for (var i = 0; i < nums.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (used[i]) continue; // 若 已用标记[下标 i]) continue;
      used[i] = true; // 把 true; 写入 used[i]
      path.add(nums[i]); // 当前路径 追加 数组[下标 i]);
      dfs(); // dfs();
      path.removeLast(); // 当前路径.removeLast();
      used[i] = false; // 把 false; 写入 used[i]
    }
  }

  dfs(); // dfs();
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = permute([1, 2, 3]); // 把 permute([1, 2, 3]) 存入 got
  if (got.length != 6)
    throw StateError('cnt'); // 若 got.长度 不等于 6) throw StateError('计数');
  if (got[0].toString() != '[1, 2, 3]' ||
      got[1].toString() != '[1, 3, 2]' ||
      got[5].toString() != '[3, 2, 1]')
    throw StateError('perm');
  if (permute([0, 1]).length != 2)
    throw StateError(
      'c2',
    ); // 若 permute([0, 1]).长度 不等于 2) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
