// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130736023
// LeetCode 415. 字符串相加 — Dart 版（方案1）
String addStrings(String a, String b) {
  // 定义函数/方法 addStrings
  var i = a.length - 1,
      j = b.length - 1,
      carry = 0; // 把 数组.长度 减 1, 下标 j 赋值为 b.长度 减 1, carry 赋值为 0 存入 下标 i
  final out = <String>[]; // 把 小于 String 超过 [] 存入 out
  while (i >= 0 || j >= 0 || carry > 0) {
    // 循环，直到不满足「下标 i 不低于 0 或 下标 j 不低于 0 或 carry 超过 0」
    var total = carry; // 把 carry 存入 总和
    if (i >= 0) {
      // 若 下标 i 不低于 0
      total += a.codeUnitAt(i--) - 0x30; // 总和累加 数组.codeUnitAt(下标 i 减一 ) 减 0x30
    }
    if (j >= 0) {
      // 若 下标 j 不低于 0
      total += b.codeUnitAt(j--) - 0x30; // 总和累加 b.codeUnitAt(下标 j 减一 ) 减 0x30
    }
    out.add((total % 10).toString()); // out 追加 (总和 对…取模 10).toString());
    carry = total ~/ 10; // 把 总和 ~ 除以 10 存入 carry
  }
  if (out.isEmpty) out.add('0'); // 若 out.isEmpty) out 追加 '0');
  return out.reversed.join(); // 返回 out.reversed.join()
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (addStrings('11', '123') != '134')
    throw StateError(
      'c1',
    ); // 若 addStrings('11', '123') 不等于 '134') throw StateError('c1');
  if (addStrings('456', '77') != '533')
    throw StateError(
      'c2',
    ); // 若 addStrings('456', '77') 不等于 '533') throw StateError('c2');
  if (addStrings('0', '0') != '0')
    throw StateError(
      'c3',
    ); // 若 addStrings('0', '0') 不等于 '0') throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
