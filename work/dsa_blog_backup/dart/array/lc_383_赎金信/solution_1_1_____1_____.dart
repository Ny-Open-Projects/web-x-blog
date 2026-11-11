// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134312127
// LeetCode 383. 赎金信 — Dart 版（方案1）
bool canConstruct(String ransom, String magazine) {
  // 定义函数/方法 canConstruct
  final cnt = List<int>.filled(26, 0); // 把 List 小于 int 超过 .filled(26, 0) 存入 计数
  for (final c in magazine.split('')) {
    cnt[c.codeUnitAt(0) - 97]++;
  }
  for (final c in ransom.split('')) {
    // for (final 字符 in ransom.split('')) {
    final i = c.codeUnitAt(0) - 97; // 把 字符.codeUnitAt(0) 减 97 存入 下标 i
    cnt[i]--; // 计数[下标 i] 减一 ;
    if (cnt[i] < 0) return false; // 若 计数[下标 i] 小于 0，直接返回 false
  }
  return true; // 返回 true
}

void main() {
  if (canConstruct('a', 'b')) throw StateError('c1');
  if (canConstruct('aa', 'ab')) throw StateError('c2');
  if (!canConstruct('aa', 'aab')) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
