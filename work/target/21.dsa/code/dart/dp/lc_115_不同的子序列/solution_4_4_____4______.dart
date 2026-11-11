// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130590161
// LeetCode 115. 不同的子序列 — Dart 版（方案4）
int numDistinct(String s, String t) {
  // 定义函数/方法 numDistinct
  final m = s.length, n = t.length; // 把 字符串.长度, 元素个数 赋值为 另一字符串.长度 存入 映射表
  final dp = List<int>.filled(
    n + 1,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数 加 1, 0) 存入 DP 表
  dp[0] = 1; // 把 1; 写入 dp[0]
  for (var i = 1; i <= m; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 映射表 就继续
    for (var j = n; j >= 1; j--) {
      // 让 下标 j 从 元素个数 开始计数，下标 j 不低于 1 就继续
      if (s[i - 1] == t[j - 1]) dp[j] += dp[j - 1];
    }
  }
  return dp[n]; // 返回 DP 表[元素个数]
}

void main() {
  if (numDistinct('rabbbit', 'rabbit') != 3) throw StateError('c1');
  if (numDistinct('babgbag', 'bag') != 5) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
