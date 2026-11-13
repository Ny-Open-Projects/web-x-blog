// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138481618
// LeetCode 2042. 检查句子中的数字是否递增 — Dart 版（方案1）
bool areNumbersAscending(String s) {
  // 定义函数/方法 areNumbersAscending
  var prev = -1; // 把 减 1 存入 前一个
  for (final tok in s.split(' ')) {
    // for (final tok in 字符串.split(' ')) {
    if (tok.isNotEmpty &&
        tok[0].codeUnitAt(0) >= 0x30 &&
        tok[0].codeUnitAt(0) <= 0x39) {
      final num = int.parse(tok); // 把 int.parse(tok) 存入 num
      if (num <= prev) return false; // 若 num 不超过 前一个，直接返回 false
      prev = num; // 把 num 存入 前一个
    }
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!areNumbersAscending(
    '1 box has 3 blue 4 red 6 green and 12 yellow marbles',
  ))
    throw StateError('c1');
  if (areNumbersAscending('hello world 5 x 5')) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
