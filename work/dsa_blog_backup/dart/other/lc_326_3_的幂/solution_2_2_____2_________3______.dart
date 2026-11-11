// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135359346
// LeetCode 326. 3的幂 — Dart 版（方案2）
bool isPowerOfThree(int n) {
  // 定义判定函数 isPowerOfThree
  while (n != 0 && n % 3 == 0) {
    // 循环，直到不满足「元素个数 不等于 0 且 元素个数 对…取模 3 等于 0」
    n = n ~/ 3; // 把 元素个数 ~ 除以 3 存入 元素个数
  }
  return n == 1; // 返回 元素个数 等于 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!isPowerOfThree(27))
    throw StateError('c1'); // 若 取反 isPowerOfThree(27)) throw StateError('c1');
  if (isPowerOfThree(0))
    throw StateError('c2'); // 若 isPowerOfThree(0)) throw StateError('c2');
  if (!isPowerOfThree(9))
    throw StateError('c3'); // 若 取反 isPowerOfThree(9)) throw StateError('c3');
  if (isPowerOfThree(-1))
    throw StateError('c4'); // 若 isPowerOfThree( 减 1)) throw StateError('c4');
  if (!isPowerOfThree(1))
    throw StateError('c5'); // 若 取反 isPowerOfThree(1)) throw StateError('c5');
  print('PASS'); // 全部用例通过，输出 PASS
}
