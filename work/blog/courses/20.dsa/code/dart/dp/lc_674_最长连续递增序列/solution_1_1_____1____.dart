// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771608
// LeetCode 674. 最长连续递增序列 — Dart 版（方案1）
int findLengthOfLCIS(List<int> nums) {
  // 定义函数/方法 findLengthOfLCIS
  if (nums.isEmpty) return 0; // 若 数组.isEmpty，直接返回 0
  var best = 1, cur = 1; // 把 1, 当前值 赋值为 1 存入 当前最优
  for (var i = 1; i < nums.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
    if (nums[i] > nums[i - 1]) {
      cur++;
      if (cur > best) best = cur;
    } else {
      cur = 1;
    }
  }
  return best; // 返回 当前最优
}

void main() {
  if (findLengthOfLCIS([1, 3, 5, 4, 7]) != 3) throw StateError('c1');
  if (findLengthOfLCIS([2, 2, 2, 2, 2]) != 1) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
