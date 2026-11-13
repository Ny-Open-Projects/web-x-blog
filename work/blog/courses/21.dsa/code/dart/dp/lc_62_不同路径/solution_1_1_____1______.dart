// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130641517
// LeetCode 62. 不同路径 — Dart 版（方案1）
int uniquePaths(int m, int n) {
  // 定义函数/方法 uniquePaths
  final dp = List<int>.filled(
    n,
    1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 1) 存入 DP 表
  for (var i = 1; i < m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 映射表 就继续
    for (var j = 1; j < n; j++)
      dp[j] += dp[j - 1]; // 让 下标 j 从 1 开始计数，下标 j 小于 元素个数 就继续
  }
  return dp[n - 1]; // 返回 DP 表[元素个数 减 1]
}

void main() {
  if (uniquePaths(3, 7) != 28) throw StateError('c1');
  if (uniquePaths(3, 2) != 3) throw StateError('c2');
  if (uniquePaths(1, 1) != 1) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
