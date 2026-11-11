// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138771574
// LeetCode 93. 复原IP地址 — Dart 版（方案2）
bool validSeg(String s) {
  // 定义函数/方法 validSeg
  if (s.isEmpty || s.length > 3)
    return false; // 若 字符串.isEmpty 或 字符串.长度 超过 3，直接返回 false
  if (s.length > 1 && s[0] == '0')
    return false; // 若 字符串.长度 超过 1 且 字符串[0] 等于 '0'，直接返回 false
  return int.parse(s) <= 255; // 返回 int.parse(字符串) 不超过 255
}

List<String> restoreIpAddresses(String s) {
  // 定义函数/方法 restoreIpAddresses
  final res = <String>[]; // 把 小于 String 超过 [] 存入 结果
  final n = s.length; // 把 字符串.长度 存入 元素个数
  if (n < 4 || n > 12) return res; // 若 元素个数 小于 4 或 元素个数 超过 12，直接返回 结果
  for (var a = 1; a <= 3; a++) {
    // 让 数组 从 1 开始计数，数组 不超过 3 就继续
    for (var b = 1; b <= 3; b++) {
      // 让 b 从 1 开始计数，b 不超过 3 就继续
      for (var c = 1; c <= 3; c++) {
        // 让 字符 从 1 开始计数，字符 不超过 3 就继续
        final d = n - a - b - c; // 把 元素个数 减 数组 减 b 减 字符 存入 d
        if (d < 1 || d > 3) continue; // 若 d 小于 1 或 d 超过 3) continue;
        final s1 = s.substring(0, a); // 把 字符串 截取 0, 数组) 存入 s1
        final s2 = s.substring(a, a + b); // 把 字符串 截取 数组, 数组 加 b) 存入 s2
        final s3 = s.substring(
          a + b,
          a + b + c,
        ); // 把 字符串 截取 数组 加 b, 数组 加 b 加 字符) 存入 s3
        final s4 = s.substring(a + b + c); // 把 字符串 截取 数组 加 b 加 字符) 存入 s4
        if (validSeg(s1) && validSeg(s2) && validSeg(s3) && validSeg(s4)) {
          // 若 validSeg(s1) 且 validSeg(s2) 且 validSeg(s3) 且 validSeg(s4
          res.add('$s1.$s2.$s3.$s4'); // 结果 追加 '$s1.$s2.$s3.$s4');
        }
      }
    }
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = restoreIpAddresses(
    '25525511135',
  ); // 把 restoreIpAddresses('25525511135') 存入 got
  if (got.length != 2 ||
      got[0] != '255.255.11.135' ||
      got[1] != '255.255.111.35')
    throw StateError('c1');
  final g2 = restoreIpAddresses('0000'); // 把 restoreIpAddresses('0000') 存入 g2
  if (g2.length != 1 || g2[0] != '0.0.0.0')
    throw StateError(
      'c2',
    ); // 若 g2.长度 不等于 1 或 g2[0] 不等于 '0.0.0.0') throw StateError('c2');
  if (restoreIpAddresses('abc').isNotEmpty) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
