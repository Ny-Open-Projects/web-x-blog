// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
// 抽象思维之对比算法 发现共性 — Dart 版（方案3）
int climbStairsRefactored(int n) {
  // 定义函数/方法 climbStairsRefactored
  if (n == 0) return 1; // 若 元素个数 等于 0，直接返回 1
  if (n < 0) return 0; // 若 元素个数 小于 0，直接返回 0
  final dp = List<int>.filled(
    n + 1,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数 加 1, 0) 存入 DP 表
  dp[0] = 1; // 把 1; 写入 dp[0]
  for (var i = 1; i <= n; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
    dp[i] = dp[i - 1]; // 把 DP 表[下标 i 减 1]; 写入 dp[i]
    if (i >= 2)
      dp[i] += dp[i - 2]; // 若 下标 i 不低于 2) DP 表[下标 i] 累加 DP 表[下标 i 减 2];
    if (i >= 3)
      dp[i] += dp[i - 3]; // 若 下标 i 不低于 3) DP 表[下标 i] 累加 DP 表[下标 i 减 3];
  }
  return dp[n]; // 返回 DP 表[元素个数]
}

void main() {
  if (climbStairsRefactored(10) != 274 || climbStairsRefactored(3) != 4)
    throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
