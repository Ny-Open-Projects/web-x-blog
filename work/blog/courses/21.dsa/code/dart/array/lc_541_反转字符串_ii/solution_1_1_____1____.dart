// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134588341
// LeetCode 541. 反转字符串II — Dart 版（方案1）
String reverseStr(String s, int k) {
  // 定义函数/方法 reverseStr
  final sb = StringBuffer(); // 把 StringBuffer() 存入 sb
  var i = 0; // 把 0 存入 下标 i
  while (i < s.length) {
    // 循环，直到不满足「下标 i 小于 字符串.长度」
    final end = (i + k < s.length)
        ? i + k
        : s.length; // 把 (下标 i 加 下标 k 小于 字符串.长度) ? 下标 i 加 下标 k : 字符串.长度 存入 终点
    sb.write(s.substring(i, end).split('').reversed.join()); // 拼接为字符串
    if (end < s.length) {
      // 若 终点 小于 字符串.长度
      final segEnd = (end + k < s.length)
          ? end + k
          : s.length; // 把 (终点 加 下标 k 小于 字符串.长度) ? 终点 加 下标 k : 字符串.长度 存入 segEnd
      sb.write(s.substring(end, segEnd)); // sb.write(字符串 截取 终点, segEnd));
    }
    i += 2 * k; // 下标 i累加 2 乘 下标 k
  }
  return sb.toString(); // 返回 sb.toString()
}

void main() {
  if (reverseStr('abcdefg', 2) != 'bacdfeg') throw StateError('c1');
  if (reverseStr('abcd', 2) != 'bacd') throw StateError('c2');
  if (reverseStr('abc', 1) != 'abc') throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
