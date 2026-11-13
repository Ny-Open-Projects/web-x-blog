// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136838836
// LeetCode 791. 自定义字符串排序 — Dart 版（方案1）
String customSortString(String order, String s) {
  // 定义函数/方法 customSortString
  final count = <String, int>{}; // 把 小于 String, int 超过 {} 存入 计数
  for (final c in s.split('')) {
    // for (final 字符 in 字符串.split('')) {
    count[c] = (count[c] ?? 0) + 1; // 把 (计数[字符] ?? 0) 加 1; 写入 count[c]
  }
  final out = <String>[]; // 把 小于 String 超过 [] 存入 out
  for (final c in order.split('')) {
    // for (final 字符 in order.split('')) {
    final n = count[c] ?? 0; // 把 计数[字符] ?? 0 存入 元素个数
    for (var i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      out.add(c); // out 追加 字符);
    }
    count[c] = 0; // 把 0; 写入 count[c]
  }
  final rest = <String>[]; // 把 小于 String 超过 [] 存入 rest
  for (final e in count.entries) {
    // for (final e in 计数.entries) {
    for (var i = 0; i < e.value; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 e.value 就继续
      rest.add(e.key); // rest 追加 e.key);
    }
  }
  rest.sort(); // 排序
  return (out..addAll(rest)).join(); // 返回 (out..addAll(rest)).join()
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (customSortString('cba', 'abcd') != 'cbad') throw StateError('c1');
  if (customSortString('bcafg', 'abcd') != 'bcad') throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
