// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
// LeetCode 509. 斐波那契数 — Dart 版（方案3）
int fib(int n) {
  if (n < 2) return n;
  var a = 0, b = 1;
  for (var i = 2; i <= n; i++) {
    final t = a + b;
    a = b;
    b = t;
  }
  return b;
}

void main() {
  if (fib(2) != 1 || fib(3) != 2 || fib(4) != 3 || fib(10) != 55)
    throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
