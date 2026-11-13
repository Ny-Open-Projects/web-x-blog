// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130497821
// LeetCode 53. 最大子数组和 — Dart 版（方案2）
int maxSubArray(List<int> nums) {
  // 定义函数/方法 maxSubArray
  var best = nums[0], cur = nums[0]; // 把 数组[0], 当前值 赋值为 数组[0] 存入 当前最优
  for (var i = 1; i < nums.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
    cur = cur > 0
        ? cur + nums[i]
        : nums[i]; // 把 当前值 超过 0 ? 当前值 加 数组[下标 i] : 数组[下标 i] 存入 当前值
    if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
  }
  return best; // 返回 当前最优
}

void main() {
  if (maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) != 6) throw StateError('c1');
  if (maxSubArray([1]) != 1) throw StateError('c2');
  if (maxSubArray([5, 4, -1, 7, 8]) != 23) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
