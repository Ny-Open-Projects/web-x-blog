// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145295630
// LeetCode 1047. 删除字符串中的所有相邻重复项 — Dart 版（方案1）
String removeDuplicates(String s) {
  // 定义函数/方法 removeDuplicates
  final st = <String>[]; // 把 小于 String 超过 [] 存入 st
  for (final c in s.split('')) {
    // for (final 字符 in 字符串.split('')) {
    if (st.isNotEmpty && st.last == c) {
      st.removeLast();
    } else {
      st.add(c);
    }
  }
  return st.join(); // 返回 st.join()
}

void main() {
  if (removeDuplicates('abbaca') != 'ca') throw StateError('c1');
  if (removeDuplicates('azxxzy') != 'ay') throw StateError('c2');
  if (removeDuplicates('') != '') throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
