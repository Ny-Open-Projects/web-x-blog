// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135917076
// LeetCode 567. 字符串的排列 — Dart 版（方案1）
bool checkInclusion(String s1, String s2) {
  // 定义判定函数 checkInclusion
  final m = s1.length, n = s2.length; // 把 s1.长度, 元素个数 赋值为 s2.长度 存入 映射表
  if (m > n) return false; // 若 映射表 超过 元素个数，直接返回 false
  final s1c = List<int>.filled(26, 0); // 把 List 小于 int 超过 .filled(26, 0) 存入 s1c
  final s2c = List<int>.filled(26, 0); // 把 List 小于 int 超过 .filled(26, 0) 存入 s2c
  for (var i = 0; i < m; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    s1c[s1.codeUnitAt(i) - 97]++; // s1c[s1.codeUnitAt(下标 i) 减 97] 加一 ;
    s2c[s2.codeUnitAt(i) - 97]++; // s2c[s2.codeUnitAt(下标 i) 减 97] 加一 ;
  }
  bool eq() {
    // 定义函数/方法 eq
    for (var i = 0; i < 26; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 26 就继续
      if (s1c[i] != s2c[i])
        return false; // 若 s1c[下标 i] 不等于 s2c[下标 i]，直接返回 false
    }
    return true; // 返回 true
  }

  if (eq()) return true; // 若 eq()，直接返回 true
  for (var i = m; i < n; i++) {
    // 让 下标 i 从 映射表 开始计数，下标 i 小于 元素个数 就继续
    s2c[s2.codeUnitAt(i) - 97]++; // s2c[s2.codeUnitAt(下标 i) 减 97] 加一 ;
    s2c[s2.codeUnitAt(i - m) -
        97]--; // s2c[s2.codeUnitAt(下标 i 减 映射表) 减 97] 减一 ;
    if (eq()) return true; // 若 eq()，直接返回 true
  }
  return false; // 返回 false
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!checkInclusion('ab', 'eidbaooo')) throw StateError('c1');
  if (checkInclusion('ab', 'eidboaoo'))
    throw StateError(
      'c2',
    ); // 若 checkInclusion('ab', 'eidboaoo')) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
