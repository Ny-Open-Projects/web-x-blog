// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734179
// LeetCode 518. 零钱兑换II — Dart 版（方案3）
int change(int amount, List<int> coins) {
  // 定义函数/方法 change
  final dp = List<int>.filled(
    amount + 1,
    0,
  ); // 把 List 小于 int 超过 .filled(目标金额 加 1, 0) 存入 DP 表
  dp[0] = 1; // 把 1; 写入 dp[0]
  for (final c in coins) {
    // for (final 字符 in 硬币面额) {
    for (var a = c; a <= amount; a++)
      dp[a] += dp[a - c]; // 让 数组 从 字符 开始计数，数组 不超过 目标金额 就继续
  }
  return dp[amount]; // 返回 DP 表[目标金额]
}

void main() {
  if (change(5, [1, 2, 5]) != 4) throw StateError('c1');
  if (change(3, [2]) != 0) throw StateError('c2');
  if (change(10, [1, 2, 5]) != 10) throw StateError('c3');
  if (change(0, [1, 2]) != 1) throw StateError('c4');
  print('PASS');
} // 全部用例通过，输出 PASS
