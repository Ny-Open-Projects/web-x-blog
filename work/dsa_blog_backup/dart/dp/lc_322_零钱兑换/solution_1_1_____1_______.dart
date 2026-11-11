// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130683917
// LeetCode 322. 零钱兑换 — Dart 版（方案1）
int coinChange(List<int> coins, int amount) {
  // 定义函数/方法 coinChange
  final dp = List<int>.filled(
    amount + 1,
    -1,
  ); // 把 List 小于 int 超过 .filled(目标金额 加 1, 减 1) 存入 DP 表
  dp[0] = 0; // 把 0; 写入 dp[0]
  for (var a = 1; a <= amount; a++) {
    // 让 数组 从 1 开始计数，数组 不超过 目标金额 就继续
    for (final c in coins) {
      // for (final 字符 in 硬币面额) {
      if (c <= a && dp[a - c] != -1) {
        // 若 字符 不超过 数组 且 DP 表[数组 减 字符] 不等于 减 1
        if (dp[a] == -1 || dp[a - c] + 1 < dp[a]) dp[a] = dp[a - c] + 1;
      }
    }
  }
  return dp[amount]; // 返回 DP 表[目标金额]
}

void main() {
  if (coinChange([1, 2, 5], 11) != 3) throw StateError('c1');
  if (coinChange([2], 3) != -1) throw StateError('c2');
  if (coinChange([1], 0) != 0) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
