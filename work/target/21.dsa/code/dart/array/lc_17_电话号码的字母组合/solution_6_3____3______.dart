// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133596542
// LeetCode 17. 电话号码的字母组合 — Dart 版（方案6）
List<String> letterCombinations(String digits) {
  // 定义函数/方法 letterCombinations
  if (digits.isEmpty) return []; // 若 digits.isEmpty，直接返回 []
  const map = [
    '',
    '',
    'abc',
    'def',
    'ghi',
    'jkl',
    'mno',
    'pqrs',
    'tuv',
    'wxyz',
  ];
  var res = <String>['']; // 把 小于 String 超过 [''] 存入 结果
  for (final c in digits.split('')) {
    // for (final 字符 in digits.split('')) {
    final next = <String>[]; // 把 小于 String 超过 [] 存入 下一个
    for (final prefix in res) {
      // for (final prefix in 结果) {
      for (final lc in map[int.parse(c)].split('')) {
        // for (final lc in 映射表[int.parse(字符)].split('')) {
        next.add(prefix + lc); // 下一个 追加 prefix 加 lc);
      }
    }
    res = next; // 把 下一个 存入 结果
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = letterCombinations('23'); // 把 letterCombinations('23') 存入 got
  if (got.length != 9 || got[0] != 'ad' || got[8] != 'cf')
    throw StateError('c1');
  if (letterCombinations('').isNotEmpty)
    throw StateError(
      'c2',
    ); // 若 letterCombinations('').isNotEmpty) throw StateError('c2');
  if (letterCombinations('2').length != 3)
    throw StateError(
      'c3',
    ); // 若 letterCombinations('2').长度 不等于 3) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
