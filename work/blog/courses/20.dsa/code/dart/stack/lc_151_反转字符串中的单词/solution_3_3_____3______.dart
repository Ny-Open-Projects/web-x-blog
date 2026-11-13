// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130846022
// LeetCode 151. 反转字符串中的单词 — Dart 版（方案3）
String reverseWords(String s) {
  // 定义函数/方法 reverseWords
  final words = s
      .trim()
      .split(RegExp(r'\s+'))
      .where((w) => w.isNotEmpty)
      .toList();
  return words.reversed.join(' '); // 返回 单词列表.reversed.join(' ')
}

void main() {
  if (reverseWords('the sky is blue') != 'blue is sky the')
    throw StateError('c1');
  if (reverseWords('  hello world  ') != 'world hello') throw StateError('c2');
  if (reverseWords('a good   example') != 'example good a')
    throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
