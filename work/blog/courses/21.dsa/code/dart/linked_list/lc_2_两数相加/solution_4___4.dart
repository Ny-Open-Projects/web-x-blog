// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133598918
// LeetCode 2. 两数相加 — Dart 版（方案4）
List<int> addTwoNumbers(List<int> a, List<int> b) {
  // 定义函数/方法 addTwoNumbers
  var i = 0, j = 0, carry = 0; // 把 0, 下标 j 赋值为 0, carry 赋值为 0 存入 下标 i
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  while (i < a.length || j < b.length || carry > 0) {
    // 循环，直到不满足「下标 i 小于 数组.长度 或 下标 j 小于 b.长度 或 carry 超过 0」
    var total = carry; // 把 carry 存入 总和
    if (i < a.length) {
      // 若 下标 i 小于 数组.长度
      total += a[i++]; // 总和累加 数组[下标 i 加一 ]
    }
    if (j < b.length) {
      // 若 下标 j 小于 b.长度
      total += b[j++]; // 总和累加 b[下标 j 加一 ]
    }
    out.add(total % 10); // out 追加 总和 对…取模 10);
    carry = total ~/ 10; // 把 总和 ~ 除以 10 存入 carry
  }
  if (out.isEmpty) out.add(0); // 若 out.isEmpty) out 追加 0);
  return out; // 返回 out
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (addTwoNumbers([2, 4, 3], [5, 6, 4]).toString() != '[7, 0, 8]')
    throw StateError('c1');
  if (addTwoNumbers([0], [0]).toString() != '[0]') throw StateError('c2');
  if (addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]).toString() !=
      '[8, 9, 9, 9, 0, 0, 0, 1]')
    throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
