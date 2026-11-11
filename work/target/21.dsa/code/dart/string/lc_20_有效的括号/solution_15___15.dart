// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133759617
// LeetCode 20. 有效的括号 — Dart 版（方案15）
bool isValid(String s) {
  // 定义判定函数 isValid
  final stack = <String>[]; // 把 小于 String 超过 [] 存入 栈
  final pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
  }; // 把 {')': '(', ']': '[', '}': '{'} 存入 pairs
  for (final ch in s.split('')) {
    // for (final 字符 in 字符串.split('')) {
    if (pairs.containsKey(ch)) {
      // 若 pairs.containsKey(字符
      final top = stack.isNotEmpty
          ? stack.removeLast()
          : '#'; // 把 栈.isNotEmpty ? 栈.removeLast() : '#' 存入 top
      if (top != pairs[ch]) return false; // 若 top 不等于 pairs[字符]，直接返回 false
    } else {
      // 否则
      stack.add(ch); // 栈 追加 字符);
    }
  }
  return stack.isEmpty; // 返回 栈.isEmpty
}

void main() {
  // 程序入口：跑内嵌自测用例
  final tests = [
    '(',
    '()',
    "()[]{}",
    '(]',
    '([)]',
    'abc',
  ]; // 把 ['(', '()', 「()[]{}」, '(]', '([)]', 'abc'] 存入 tests
  final want = [
    false,
    true,
    true,
    false,
    false,
    false,
  ]; // 把 [false, true, true, false, false, false] 存入 want
  for (var i = 0; i < tests.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 tests.长度 就继续
    if (isValid(tests[i]) != want[i]) throw StateError('case $i');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
