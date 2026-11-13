// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130540333
// LeetCode 72. 编辑距离 — Dart 版（方案2）
int minDistance(String w1, String w2) {
  // 定义函数/方法 minDistance
  final m = w1.length, n = w2.length; // 把 w1.长度, 元素个数 赋值为 w2.长度 存入 映射表
  final dp = List<int>.generate(n + 1, (j) => j);
  for (var i = 1; i <= m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    var prevDiag = dp[0]; // 把 DP 表[0] 存入 prevDiag
    dp[0] = i; // 把 下标 i; 写入 dp[0]
    for (var j = 1; j <= n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
      final tmp = dp[j]; // 把 DP 表[下标 j] 存入 临时变量
      dp[j] = w1[i - 1] == w2[j - 1]
          ? prevDiag
          : 1 + [prevDiag, dp[j], dp[j - 1]].reduce((a, b) => a < b ? a : b);
      prevDiag = tmp; // 把 临时变量 存入 prevDiag
    }
  }
  return dp[n]; // 返回 DP 表[元素个数]
}

void main() {
  if (minDistance('horse', 'ros') != 3) throw StateError('c1');
  if (minDistance('intention', 'execution') != 5) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
