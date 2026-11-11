// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134135902
// LeetCode 344. 反转字符串 — Dart 版（方案1）
String reverseString(String s) => String.fromCharCodes(s.codeUnits.reversed);
void main() {
  if (reverseString('hello') != 'olleh') throw StateError('c1');
  if (reverseString('Hannah') != 'hannaH') throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
