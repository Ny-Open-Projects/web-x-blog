// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468105
// LeetCode 136. 只出现一次的数字 — Dart 版（方案2）
int singleNumber(List<int> nums) {
  var x = 0;
  for (final v in nums) {
    x ^= v;
  }
  return x;
}

void main() {
  if (singleNumber([2, 2, 1]) != 1) throw StateError('c1');
  if (singleNumber([4, 1, 2, 1, 2]) != 4) throw StateError('c2');
  if (singleNumber([1]) != 1) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
