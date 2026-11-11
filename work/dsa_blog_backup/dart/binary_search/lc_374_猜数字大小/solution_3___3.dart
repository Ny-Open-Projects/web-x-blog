// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238093
// LeetCode 374. 猜数字大小 — Dart 版（方案3：迭代二分）
var pick = 6; // 把 6 存入 pick
int guess(int num) {
  // 定义函数/方法 guess
  if (num == pick) return 0; // 若 num 等于 pick，直接返回 0
  return num < pick ? 1 : -1; // 返回 num 小于 pick ? 1 : 减 1
}

int guessNumber(int n) {
  // 定义函数/方法 guessNumber
  var low = 1, high = n; // 把 1, high 赋值为 元素个数 存入 low
  while (low <= high) {
    // 循环，直到不满足「low 不超过 high」
    final mid = low + (high - low) ~/ 2; // 把 low 加 (high 减 low) ~ 除以 2 存入 中点
    final res = guess(mid); // 把 guess(中点) 存入 结果
    if (res == 0) return mid; // 若 结果 等于 0，直接返回 中点
    if (res == 1) {
      low = mid + 1;
    } else {
      high = mid - 1;
    } // 若 结果 等于 1) { low 赋值为 中点 加 1; } else { high 赋值为 中点 减 1; }
  }
  return -1; // 返回 减 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  final cases = [
    [10, 6],
    [1, 1],
    [5, 3],
    [2, 2],
  ];
  for (final c in cases) {
    // for (final 字符 in cases) {
    pick = c[1]; // 把 字符[1] 存入 pick
    if (guessNumber(c[0]) != c[1]) throw StateError('n=${c[0]} pick=${c[1]}');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
