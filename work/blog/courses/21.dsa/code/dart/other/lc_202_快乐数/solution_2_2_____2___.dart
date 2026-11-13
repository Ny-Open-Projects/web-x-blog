// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135124945
// LeetCode 202. 快乐数 — Dart 版（方案2）
int bitSquareSum(int n) {
  // 定义函数/方法 bitSquareSum
  var s = 0; // 把 0 存入 字符串
  while (n > 0) {
    // 循环，直到不满足「元素个数 超过 0」
    final d = n % 10; // 把 元素个数 对…取模 10 存入 d
    s += d * d; // 字符串累加 d 乘 d
    n = n ~/ 10; // 把 元素个数 ~ 除以 10 存入 元素个数
  }
  return s; // 返回 字符串
}

bool isHappy(int n) {
  // 定义判定函数 isHappy
  final seen = <int>{}; // 把 小于 int 超过 {} 存入 已见集合
  while (n != 1 && !seen.contains(n)) {
    // 循环，直到不满足「元素个数 不等于 1 且 取反 已见集合 是否包含 元素个数」
    seen.add(n); // 已见集合 追加 元素个数);
    n = bitSquareSum(n); // 把 bitSquareSum(元素个数) 存入 元素个数
  }
  return n == 1; // 返回 元素个数 等于 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (bitSquareSum(1) != 1)
    throw StateError('a1'); // 若 bitSquareSum(1) 不等于 1) throw StateError('a1');
  if (bitSquareSum(19) != 82)
    throw StateError(
      'a2',
    ); // 若 bitSquareSum(19) 不等于 82) throw StateError('a2');
  if (bitSquareSum(82) != 68)
    throw StateError(
      'a3',
    ); // 若 bitSquareSum(82) 不等于 68) throw StateError('a3');
  if (!isHappy(19) || !isHappy(1) || isHappy(2)) throw StateError('b');
  print('PASS'); // 全部用例通过，输出 PASS
}
