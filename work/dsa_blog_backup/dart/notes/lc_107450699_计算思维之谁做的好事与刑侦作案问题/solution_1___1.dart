// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107450699
// 计算思维之谁做的好事 — Dart 版（方案1）
String findGoodMan() {
  // 定义函数/方法 findGoodMan
  for (final m in ['A', 'B', 'C', 'D']) {
    // for (final 映射表 in ['A', 'B', 'C', 'D']) {
    var t = 0; // 把 0 存入 另一字符串
    if (m != 'A') t++; // 若 映射表 不等于 'A') 另一字符串 加一 ;
    if (m == 'C') t++; // 若 映射表 等于 'C') 另一字符串 加一 ;
    if (m == 'D') t++; // 若 映射表 等于 'D') 另一字符串 加一 ;
    if (m != 'D') t++; // 若 映射表 不等于 'D') 另一字符串 加一 ;
    if (t == 3) return m; // 若 另一字符串 等于 3，直接返回 映射表
  }
  return '?'; // 返回 '?'
}

void main() {
  if (findGoodMan() != 'C') throw StateError('x');
  print('PASS');
} // 全部用例通过，输出 PASS
