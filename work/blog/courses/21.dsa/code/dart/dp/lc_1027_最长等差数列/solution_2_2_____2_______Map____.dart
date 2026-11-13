// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130687299
// LeetCode 1027. 最长等差数列 — Dart 版（方案2）
int longestArithSeqLength(List<int> nums) {
  // 定义函数/方法 longestArithSeqLength
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final dp = List<Map<int, int>>.generate(n, (_) => {});
  var best = 1; // 把 1 存入 当前最优
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (var j = 0; j < i; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
      final d = nums[i] - nums[j]; // 把 数组[下标 i] 减 数组[下标 j] 存入 d
      final cur = (dp[j][d] ?? 1) + 1; // 把 (DP 表[下标 j][d] ?? 1) 加 1 存入 当前值
      dp[i][d] = cur; // 把 当前值; 写入 dp[i][d]
      if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
    }
  }
  return best; // 返回 当前最优
}

void main() {
  if (longestArithSeqLength([9, 4, 7, 2, 10]) != 3) throw StateError('c1');
  if (longestArithSeqLength([3, 6, 9, 12]) != 4) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
