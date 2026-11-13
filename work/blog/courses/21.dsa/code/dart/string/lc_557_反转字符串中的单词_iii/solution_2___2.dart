// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 557. 反转字符串中的单词III — Dart 版（方案2）
String reverseWords(String s) {
  // 定义函数/方法 reverseWords
  final out = <String>[]; // 把 小于 String 超过 [] 存入 out
  for (final w in s.split(' ')) {
    // for (final 权重 in 字符串.split(' ')) {
    if (w.isEmpty) continue; // 若 权重.isEmpty) continue;
    out.add(w.split('').reversed.join()); // 拼接为字符串
  }
  return out.join(' '); // 返回 out.join(' ')
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (reverseWords("Let's take LeetCode contest") !=
      "s'teL ekat edoCteeL tsetnoc")
    throw StateError('c1');
  if (reverseWords('God Ding') != 'doG gniD') throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
