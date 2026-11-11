// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135129920
// LeetCode 8. 字符串转换整数 (atoi) — Dart 版（方案2）
int myAtoi(String s) {
  // 定义函数/方法 myAtoi
  var i = 0; // 把 0 存入 下标 i
  final n = s.length; // 把 字符串.长度 存入 元素个数
  while (i < n && s[i] == ' ')
    i++; // 循环，直到不满足「下标 i 小于 元素个数 且 字符串[下标 i] 等于 ' ') 下标 i 加一 ;」
  var sign = 1; // 把 1 存入 sign
  if (i < n && (s[i] == '+' || s[i] == '-')) {
    // 若 下标 i 小于 元素个数 且 (字符串[下标 i] 等于 ' 加 ' 或 字符串[下标 i] 等于 ' 减 '
    if (s[i] == '-') sign = -1; // 若 字符串[下标 i] 等于 ' 减 ') sign 赋值为 减 1;
    i++; // 下标 i 加一
  }
  var ans = 0; // 把 0 存入 答案
  while (i < n && s.codeUnitAt(i) >= 0x30 && s.codeUnitAt(i) <= 0x39) {
    ans =
        ans * 10 +
        (s.codeUnitAt(i) -
            0x30); // 把 答案 乘 10 加 (字符串.codeUnitAt(下标 i) 减 0x30) 存入 答案
    if (ans > 2147483648)
      ans = 2147483648; // 若 答案 超过 2147483648) 答案 赋值为 2147483648;
    i++; // 下标 i 加一
  }
  ans *= sign; // 把 sign; 写入 ans *
  if (ans > 2147483647) return 2147483647; // 若 答案 超过 2147483647，直接返回 2147483647
  if (ans < -2147483648)
    return -2147483648; // 若 答案 小于 减 2147483648，直接返回 减 2147483648
  return ans; // 返回 答案
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (myAtoi('42') != 42)
    throw StateError('c1'); // 若 myAtoi('42') 不等于 42) throw StateError('c1');
  if (myAtoi(' -42') != -42)
    throw StateError(
      'c2',
    ); // 若 myAtoi(' 减 42') 不等于 减 42) throw StateError('c2');
  if (myAtoi('4193 with words') != 4193)
    throw StateError(
      'c3',
    ); // 若 myAtoi('4193 with 单词列表') 不等于 4193) throw StateError('c3');
  if (myAtoi('-91283472332') != -2147483648) throw StateError('c4');
  if (myAtoi('words and 987') != 0)
    throw StateError(
      'c5',
    ); // 若 myAtoi('单词列表 and 987') 不等于 0) throw StateError('c5');
  print('PASS'); // 全部用例通过，输出 PASS
}
