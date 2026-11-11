// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
// 计算思维之下楼梯台阶和象棋跳马问题 — Dart 版（方案5）
int climbStairsVariants(int n) {
  // 定义函数/方法 climbStairsVariants
  if (n <= 1) return 1; // 若 元素个数 不超过 1，直接返回 1
  var a = 1, b = 1; // 把 1, b 赋值为 1 存入 数组
  for (var i = 2; i <= n; i++) {
    final t = a + b;
    a = b;
    b = t;
  } // 让 下标 i 从 2 开始计数，下标 i 不超过 元素个数 就继续
  return b; // 返回 b
}

void main() {
  if (climbStairsVariants(10) != 89 ||
      climbStairsVariants(1) != 1 ||
      climbStairsVariants(2) != 2)
    throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
