// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 1143. 最长公共子序列 — Dart 版（方案1）
int longestCommonSubsequence(String t1, String t2) {
  // 定义函数/方法 longestCommonSubsequence
  final m = t1.length, n = t2.length; // 把 t1.长度, 元素个数 赋值为 t2.长度 存入 映射表
  final dp = List<int>.filled(
    n + 1,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数 加 1, 0) 存入 DP 表
  for (var i = 1; i <= m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    var prevDiag = 0; // 把 0 存入 prevDiag
    for (var j = 1; j <= n; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 不超过 元素个数 就继续
      final tmp = dp[j]; // 把 DP 表[下标 j] 存入 临时变量
      dp[j] = t1[i - 1] == t2[j - 1]
          ? prevDiag + 1
          : (dp[j] > dp[j - 1] ? dp[j] : dp[j - 1]);
      prevDiag = tmp; // 把 临时变量 存入 prevDiag
    }
  }
  return dp[n]; // 返回 DP 表[元素个数]
}

void main() {
  if (longestCommonSubsequence('abcde', 'ace') != 3) throw StateError('c1');
  if (longestCommonSubsequence('abc', 'abc') != 3) throw StateError('c2');
  if (longestCommonSubsequence('abc', 'def') != 0) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
