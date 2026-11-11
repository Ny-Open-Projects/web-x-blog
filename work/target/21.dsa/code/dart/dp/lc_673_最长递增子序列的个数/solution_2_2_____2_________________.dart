// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771847
// LeetCode 673. 最长递增子序列的个数 — Dart 版（方案2）
int findNumberOfLIS(List<int> nums) {
  // 定义函数/方法 findNumberOfLIS
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final dp = List<int>.filled(
    n,
    1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 1) 存入 DP 表
  final cnt = List<int>.filled(n, 1); // 把 List 小于 int 超过 .filled(元素个数, 1) 存入 计数
  var best = 0, res = 0; // 把 0, 结果 赋值为 0 存入 当前最优
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (var j = 0; j < i; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
      if (nums[j] < nums[i]) {
        // 若 数组[下标 j] 小于 数组[下标 i]
        if (dp[j] + 1 > dp[i]) {
          dp[i] = dp[j] + 1;
          cnt[i] = cnt[j];
        } else if (dp[j] + 1 == dp[i])
          cnt[i] += cnt[j]; // 否则，若 DP 表[下标 j] 加 1 等于 DP 表[下标 i]) 计数[下标 i] 累加 计数[下标 j];
      }
    }
    if (dp[i] > best) {
      best = dp[i];
      res = cnt[i];
    } else if (dp[i] == best)
      res += cnt[i]; // 否则，若 DP 表[下标 i] 等于 当前最优) 结果 累加 计数[下标 i];
  }
  return res; // 返回 结果
}

void main() {
  if (findNumberOfLIS([1, 3, 5, 4, 7]) != 2) throw StateError('c1');
  if (findNumberOfLIS([2, 2, 2, 2, 2]) != 5) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
