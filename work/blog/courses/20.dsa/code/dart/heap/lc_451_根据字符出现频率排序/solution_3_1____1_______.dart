// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137060905
// LeetCode 451. 根据字符出现频率排序 — Dart 版（方案3）
String frequencySort(String s) {
  // 定义函数/方法 frequencySort
  if (s.isEmpty) return ''; // 若 字符串.isEmpty，直接返回 ''
  final counts = <String, int>{}; // 把 小于 String, int 超过 {} 存入 counts
  final firstIdx = <String, int>{}; // 把 小于 String, int 超过 {} 存入 firstIdx
  for (var i = 0; i < s.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 字符串.长度 就继续
    final c = s[i]; // 把 字符串[下标 i] 存入 字符
    counts[c] = (counts[c] ?? 0) + 1; // 把 (counts[字符] ?? 0) 加 1; 写入 counts[c]
    firstIdx.putIfAbsent(c, () => i);
  }
  final keys =
      counts.keys
          .toList() // 把 counts.keys.toList() 存入 keys
        ..sort((a, b) {
          // 排序
          if (counts[a] != counts[b]) return counts[b]!.compareTo(counts[a]!);
          return firstIdx[a]!.compareTo(
            firstIdx[b]!,
          ); // 返回 firstIdx[数组]取反 .compareTo(firstIdx[b]取反 )
        }); // });
  final sb = StringBuffer(); // 把 StringBuffer() 存入 sb
  for (final c in keys) {
    // for (final 字符 in keys) {
    sb.write(c * counts[c]!); // sb.write(字符 乘 counts[字符]取反 );
  }
  return sb.toString(); // 返回 sb.toString()
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (frequencySort('tree') != 'eetr')
    throw StateError(
      'c1',
    ); // 若 frequencySort('tree') 不等于 'eetr') throw StateError('c1');
  if (frequencySort('') != '')
    throw StateError(
      'c2',
    ); // 若 frequencySort('') 不等于 '') throw StateError('c2');
  if (frequencySort('cccaaa') != 'cccaaa') throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
