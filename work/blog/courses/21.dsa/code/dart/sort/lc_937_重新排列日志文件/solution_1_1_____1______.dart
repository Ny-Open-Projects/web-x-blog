// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/139965098
// LeetCode 937. 重新排列日志文件 — Dart 版（方案1）
List<String> reorderLogFiles(List<String> logs) {
  // 定义函数/方法 reorderLogFiles
  bool isDigit(String s) =>
      s.isNotEmpty && s[0].codeUnitAt(0) >= 0x30 && s[0].codeUnitAt(0) <= 0x39;
  String contentOf(String log) {
    // 定义函数/方法 contentOf
    final idx = log.indexOf(' '); // 把 log 查找 ' ') 存入 idx
    return log.substring(idx + 1); // 返回 log 截取 idx 加 1)
  }

  final letter = <String>[]; // 把 小于 String 超过 [] 存入 letter
  final digit = <String>[]; // 把 小于 String 超过 [] 存入 digit
  for (final log in logs) {
    // for (final log in logs) {
    if (isDigit(contentOf(log))) {
      // 若 isDigit(contentOf(log
      digit.add(log); // digit 追加 log);
    } else {
      // 否则
      letter.add(log); // letter 追加 log);
    }
  }
  letter.sort((a, b) {
    // 排序
    final ca = contentOf(a); // 把 contentOf(数组) 存入 ca
    final cb = contentOf(b); // 把 contentOf(b) 存入 cb
    if (ca != cb) return ca.compareTo(cb); // 若 ca 不等于 cb，直接返回 ca.compareTo(cb)
    return a.compareTo(b); // 返回 数组.compareTo(b)
  }); // });
  return [...letter, ...digit]; // 返回 [...letter, ...digit]
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = reorderLogFiles([
    'a1 9 2 3 1',
    'g1 act car',
    'zo4 4 7',
    'ab1 off key dog',
    'a8 act zoo',
  ]);
  if (got.toString() !=
      '[g1 act car, a8 act zoo, ab1 off key dog, a1 9 2 3 1, zo4 4 7]')
    throw StateError('c1');
  print('PASS'); // 全部用例通过，输出 PASS
}
