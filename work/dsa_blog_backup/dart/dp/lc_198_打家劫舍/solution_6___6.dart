// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130644389
// LeetCode 198. 打家劫舍 — Dart 版（方案6）
int rob(List<int> nums) {
  var a = 0, b = 0;
  for (final v in nums) {
    final t = b > a + v ? b : a + v;
    a = b;
    b = t;
  }
  return b;
}

void main() {
  if (rob([1, 2, 3, 1]) != 4) throw StateError('c1');
  if (rob([2, 7, 9, 3, 1]) != 12) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
