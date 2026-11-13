// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134109616
// LeetCode 78. 子集 — Dart 版（方案2）
List<List<int>> subsets(List<int> nums) {
  // 定义函数/方法 subsets
  final res = <List<int>>[]; // 把 小于 List 小于 int 超过 超过 [] 存入 结果
  final path = <int>[]; // 把 小于 int 超过 [] 存入 当前路径
  void dfs(int start) {
    // 定义函数/方法 dfs
    res.add(List<int>.from(path)); // 结果 追加 List 小于 int 超过 .from(当前路径));
    for (var i = start; i < nums.length; i++) {
      // 让 下标 i 从 起点 开始计数，下标 i 小于 数组.长度 就继续
      path.add(nums[i]); // 当前路径 追加 数组[下标 i]);
      dfs(i + 1); // dfs(下标 i 加 1);
      path.removeLast(); // 当前路径.removeLast();
    }
  }

  dfs(0); // dfs(0);
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (subsets([1, 2, 3]).length != 8)
    throw StateError(
      'c1',
    ); // 若 subsets([1, 2, 3]).长度 不等于 8) throw StateError('c1');
  if (subsets([0]).length != 2)
    throw StateError('c2'); // 若 subsets([0]).长度 不等于 2) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
