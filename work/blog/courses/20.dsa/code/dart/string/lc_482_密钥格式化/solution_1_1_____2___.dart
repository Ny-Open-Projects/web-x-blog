// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138290964
// LeetCode 482. 密钥格式化 — Dart 版（方案1）
String licenseKeyFormatting(String s, int k) {
  // 定义函数/方法 licenseKeyFormatting
  final cleaned = s
      .replaceAll('-', '')
      .toUpperCase(); // 把 字符串.replaceAll(' 减 ', '').toUpperCase() 存入 cleaned
  final n = cleaned.length; // 把 cleaned.长度 存入 元素个数
  if (n == 0) return ''; // 若 元素个数 等于 0，直接返回 ''
  final out = <String>[]; // 把 小于 String 超过 [] 存入 out
  final first = n % k; // 把 元素个数 对…取模 下标 k 存入 first
  var idx = 0; // 把 0 存入 idx
  if (first > 0) {
    // 若 first 超过 0
    for (var i = 0; i < first; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 first 就继续
      out.add(cleaned[idx++]); // out 追加 cleaned[idx 加一 ]);
    }
    if (idx < n) out.add('-'); // 若 idx 小于 元素个数) out 追加 ' 减 ');
  }
  while (idx < n) {
    // 循环，直到不满足「idx 小于 元素个数」
    for (var i = 0; i < k; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 就继续
      out.add(cleaned[idx++]); // out 追加 cleaned[idx 加一 ]);
    }
    if (idx < n) out.add('-'); // 若 idx 小于 元素个数) out 追加 ' 减 ');
  }
  return out.join(); // 返回 out.join()
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (licenseKeyFormatting('5F3Z-2e-9-w', 4) != '5F3Z-2E9W')
    throw StateError('c1');
  if (licenseKeyFormatting('2-5g-3-J', 2) != '2-5G-3J') throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
