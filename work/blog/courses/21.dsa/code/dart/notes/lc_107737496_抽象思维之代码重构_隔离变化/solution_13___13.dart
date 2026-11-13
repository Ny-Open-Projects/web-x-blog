// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
// LeetCode 107737496. 代码重构_隔离变化 — Dart 版（方案13：微型正则匹配 match/matchhere/matchstar）
bool matchstar(String c, String re, String text) {
  // 定义函数/方法 matchstar
  var i = 0; // 把 0 存入 下标 i
  while (true) {
    // 循环，直到不满足「true」
    if (matchhere(re, text.substring(i)))
      return true; // 若 matchhere(re, text 截取 下标 i))，直接返回 true
    if (i >= text.length) break; // 若 下标 i 不低于 text.长度) break;
    if (text[i] != c && c != '.')
      break; // 若 text[下标 i] 不等于 字符 且 字符 不等于 '.') break;
    i++; // 下标 i 加一
  }
  return false; // 返回 false
}

bool matchhere(String re, String text) {
  // 定义函数/方法 matchhere
  if (re.isEmpty) return true; // 若 re.isEmpty，直接返回 true
  if (re.length >= 2 && re[1] == '*')
    return matchstar(re[0], re.substring(2), text);
  if (re[0] == r'$' && re.length == 1)
    return text.isEmpty; // 若 re[0] 等于 右指针'$' 且 re.长度 等于 1，直接返回 text.isEmpty
  if (text.isNotEmpty && (re[0] == '.' || re[0] == text[0])) {
    // 若 text.isNotEmpty 且 (re[0] 等于 '.' 或 re[0] 等于 text[0]
    return matchhere(
      re.substring(1),
      text.substring(1),
    ); // 返回 matchhere(re 截取 1), text 截取 1))
  }
  return false; // 返回 false
}

bool match(String re, String text) {
  // 定义函数/方法 match
  if (re.isNotEmpty && re[0] == '^') return matchhere(re.substring(1), text);
  var i = 0; // 把 0 存入 下标 i
  while (true) {
    // 循环，直到不满足「true」
    if (matchhere(re, text.substring(i)))
      return true; // 若 matchhere(re, text 截取 下标 i))，直接返回 true
    if (i >= text.length) break; // 若 下标 i 不低于 text.长度) break;
    i++; // 下标 i 加一
  }
  return false; // 返回 false
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!match('abc', 'xxabcxx'))
    throw StateError(
      'm1 failed',
    ); // 若 取反 match('abc', 'xxabcxx')) throw StateError('m1 failed');
  if (!match('a.c', 'axc'))
    throw StateError(
      'm2 failed',
    ); // 若 取反 match('数组.字符', 'axc')) throw StateError('m2 failed');
  if (!match('a*', 'aaaa'))
    throw StateError(
      'm3 failed',
    ); // 若 取反 match('数组 乘 ', 'aaaa')) throw StateError('m3 failed');
  if (match('^a', 'ba'))
    throw StateError(
      'm4 failed',
    ); // 若 match(' 按位异或 数组', 'ba')) throw StateError('m4 failed');
  if (!match(r'c$', 'abc'))
    throw StateError(
      'm5 failed',
    ); // 若 取反 match(右指针'字符$', 'abc')) throw StateError('m5 failed');
  if (!match('a.*c', 'aXYZc')) throw StateError('m6 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
