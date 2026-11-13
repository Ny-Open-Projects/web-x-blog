// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134424807
// LeetCode 485. 最大连续1的个数 — Dart 版（方案1）
int findMaxConsecutiveOnes(List<int> nums) {
  // 定义函数/方法 findMaxConsecutiveOnes
  var best = 0, cur = 0; // 把 0, 当前值 赋值为 0 存入 当前最优
  for (final v in nums) {
    // for (final 值 in 数组) {
    if (v == 1) {
      cur++;
      if (cur > best) best = cur;
    } else {
      cur = 0;
    }
  }
  return best; // 返回 当前最优
}

void main() {
  if (findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) != 3) throw StateError('c1');
  if (findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) != 2) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
