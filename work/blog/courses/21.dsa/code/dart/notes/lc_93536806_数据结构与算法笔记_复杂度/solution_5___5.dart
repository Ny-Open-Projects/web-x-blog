// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
// 数据结构与算法笔记: 复杂度 — Dart 版（方案5）
int funcCalls(int n) {
  // 定义函数/方法 funcCalls
  if (n <= 1) return 1; // 若 元素个数 不超过 1，直接返回 1
  return 2 * funcCalls(n - 1); // 返回 2 乘 funcCalls(元素个数 减 1)
}

void main() {
  if (funcCalls(1) != 1 ||
      funcCalls(2) != 2 ||
      funcCalls(5) != 16 ||
      funcCalls(10) != 512)
    throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
