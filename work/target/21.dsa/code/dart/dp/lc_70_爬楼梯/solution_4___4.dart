// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130506068
// LeetCode 70. 爬楼梯 — Dart 版（方案4）
int climbStairs(int n) {
  if (n <= 2) return n;
  var a = 1, b = 2;
  for (var i = 3; i <= n; i++) {
    final t = a + b;
    a = b;
    b = t;
  }
  return b;
}

void main() {
  if (climbStairs(2) != 2 || climbStairs(3) != 3 || climbStairs(10) != 89)
    throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
