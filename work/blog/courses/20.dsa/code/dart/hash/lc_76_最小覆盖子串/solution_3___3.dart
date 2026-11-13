// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135256754
// LeetCode 76. 最小覆盖子串 — Dart 版（方案3）
String minWindow(String s, String t) {
  // 定义函数/方法 minWindow
  if (s.isEmpty || t.isEmpty)
    return ''; // 若 字符串.isEmpty 或 另一字符串.isEmpty，直接返回 ''
  final target = <String, int>{}; // 把 小于 String, int 超过 {} 存入 目标值
  for (final c in t.split('')) {
    // for (final 字符 in 另一字符串.split('')) {
    target[c] = (target[c] ?? 0) + 1; // 把 (目标值[字符] ?? 0) 加 1; 写入 target[c]
  }
  final required = target.length; // 把 目标值.长度 存入 required
  var left = 0, formed = 0; // 把 0, formed 赋值为 0 存入 左边界
  final window = <String, int>{}; // 把 小于 String, int 超过 {} 存入 window
  var minLen = 0x7fffffffffffffff,
      minLeft = 0; // 把 0x7fffffffffffffff, minLeft 赋值为 0 存入 minLen
  for (var right = 0; right < s.length; right++) {
    // 让 右边界 从 0 开始计数，右边界 小于 字符串.长度 就继续
    final c = s[right]; // 把 字符串[右边界] 存入 字符
    window[c] = (window[c] ?? 0) + 1; // 把 (window[字符] ?? 0) 加 1; 写入 window[c]
    if (target.containsKey(c) && window[c] == target[c])
      formed++; // 若 目标值.containsKey(字符) 且 window[字符] 等于 目标值[字符]) formed 加一 ;
    while (formed == required) {
      // 循环，直到不满足「formed 等于 required」
      if (right - left + 1 < minLen) {
        // 若 右边界 减 左边界 加 1 小于 minLen
        minLen = right - left + 1; // 把 右边界 减 左边界 加 1 存入 minLen
        minLeft = left; // 把 左边界 存入 minLeft
      }
      final lc = s[left]; // 把 字符串[左边界] 存入 lc
      window[lc] = window[lc]! - 1; // 把 window[lc]取反 减 1; 写入 window[lc]
      if (target.containsKey(lc) && window[lc]! < target[lc]!) formed--;
      left++; // 左边界 加一
    }
  }
  if (minLen == 0x7fffffffffffffff)
    return ''; // 若 minLen 等于 0x7fffffffffffffff，直接返回 ''
  return s.substring(
    minLeft,
    minLeft + minLen,
  ); // 返回 字符串 截取 minLeft, minLeft 加 minLen)
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (minWindow('ADOBECODEBANC', 'ABC') != 'BANC') throw StateError('c1');
  if (minWindow('a', 'a') != 'a')
    throw StateError(
      'c2',
    ); // 若 minWindow('数组', '数组') 不等于 '数组') throw StateError('c2');
  if (minWindow('a', 'aa') != '')
    throw StateError(
      'c3',
    ); // 若 minWindow('数组', 'aa') 不等于 '') throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
