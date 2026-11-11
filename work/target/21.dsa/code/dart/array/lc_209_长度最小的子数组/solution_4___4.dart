// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133807379
// LeetCode 209. 长度最小的子数组 — Dart 版（方案4）
int minSubArrayLen(int target, List<int> nums) {
  // 定义函数/方法 minSubArrayLen
  var l = 0, sum = 0, best = -1; // 把 0, 累计和 赋值为 0, 当前最优 赋值为 减 1 存入 左指针
  for (var r = 0; r < nums.length; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 数组.长度 就继续
    sum += nums[r]; // 累计和累加 数组[右指针]
    while (sum >= target) {
      // 循环，直到不满足「累计和 不低于 目标值」
      final len = r - l + 1; // 把 右指针 减 左指针 加 1 存入 长度
      if (best == -1 || len < best)
        best = len; // 若 当前最优 等于 减 1 或 长度 小于 当前最优) 当前最优 赋值为 长度;
      sum -= nums[l++]; // 累计和累减 数组[左指针 加一 ]
    }
  }
  return best == -1 ? 0 : best; // 返回 当前最优 等于 减 1 ? 0 : 当前最优
}

void main() {
  if (minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) != 2) throw StateError('c1');
  if (minSubArrayLen(4, [1, 4, 4]) != 1) throw StateError('c2');
  if (minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) != 0) throw StateError('c3');
  if (minSubArrayLen(1, [1, 2, 3]) != 1) throw StateError('c4');
  print('PASS');
} // 全部用例通过，输出 PASS
