// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130701795
// LeetCode 43. 字符串相乘 — Dart 版（方案2）
String multiply(String num1, String num2) {
  // 定义函数/方法 multiply
  if (num1 == '0' || num2 == '0')
    return '0'; // 若 num1 等于 '0' 或 num2 等于 '0'，直接返回 '0'
  final m = num1.length, n = num2.length; // 把 num1.长度, 元素个数 赋值为 num2.长度 存入 映射表
  final result = List<int>.filled(
    m + n,
    0,
  ); // 把 List 小于 int 超过 .filled(映射表 加 元素个数, 0) 存入 结果
  for (var i = m - 1; i >= 0; i--) {
    // 让 下标 i 从 映射表 减 1 开始计数，下标 i 不低于 0 就继续
    for (var j = n - 1; j >= 0; j--) {
      // 让 下标 j 从 元素个数 减 1 开始计数，下标 j 不低于 0 就继续
      final mul = (num1.codeUnitAt(i) - 0x30) * (num2.codeUnitAt(j) - 0x30);
      final p1 = i + j,
          p2 = i + j + 1; // 把 下标 i 加 下标 j, p2 赋值为 下标 i 加 下标 j 加 1 存入 p1
      final total = mul + result[p2]; // 把 mul 加 结果[p2] 存入 总和
      result[p2] = total % 10; // 把 总和 对…取模 10; 写入 result[p2]
      result[p1] += total ~/ 10; // result[p1]累加 总和 ~ 除以 10
    }
  }
  final sb = StringBuffer(); // 把 StringBuffer() 存入 sb
  var started = false; // 把 false 存入 started
  for (final d in result) {
    // for (final d in 结果) {
    if (d != 0 || started) {
      // 若 d 不等于 0 或 started
      sb.write(d); // sb.write(d);
      started = true; // 把 true 存入 started
    }
  }
  final s = sb.toString(); // 把 sb.toString() 存入 字符串
  return s.isEmpty ? '0' : s; // 返回 字符串.isEmpty ? '0' : 字符串
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (multiply('2', '3') != '6')
    throw StateError(
      'c1',
    ); // 若 multiply('2', '3') 不等于 '6') throw StateError('c1');
  if (multiply('123', '456') != '56088') throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
