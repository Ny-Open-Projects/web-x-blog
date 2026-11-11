// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133834060
// LeetCode 2407. 最长递增子序列II — Dart 版（方案1）
int lengthOfLIS(List<int> nums, int k) {
  // 定义函数/方法 lengthOfLIS
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final dp = List<int>.filled(
    n,
    1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 1) 存入 DP 表
  var best = 0; // 把 0 存入 当前最优
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (var j = 0; j < i; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
      if (nums[j] < nums[i] && nums[i] - nums[j] <= k && dp[j] + 1 > dp[i])
        dp[i] = dp[j] + 1;
    }
    if (dp[i] > best)
      best = dp[i]; // 若 DP 表[下标 i] 超过 当前最优) 当前最优 赋值为 DP 表[下标 i];
  }
  return best; // 返回 当前最优
}

void main() {
  if (lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3) != 5) throw StateError('c1');
  if (lengthOfLIS([1], 1) != 1) throw StateError('c2');
  if (lengthOfLIS([], 3) != 0) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
