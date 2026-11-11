// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案6：合成滑块数据 buildSynthetic）
List<List<int>> buildSynthetic(int bgLen, int gapStart, int puzzleLen) {
  // 定义函数/方法 buildSynthetic
  final bg = List<int>.filled(
    bgLen,
    10,
  ); // 把 List 小于 int 超过 .filled(bgLen, 10) 存入 bg
  for (var i = gapStart; i < (gapStart + puzzleLen).clamp(0, bgLen); i++) {
    bg[i] = 200; // 把 200; 写入 bg[i]
  }
  final puzzle = bg.sublist(gapStart, (gapStart + puzzleLen).clamp(0, bgLen));
  return [bg, puzzle]; // 返回 [bg, puzzle]
}

void main() {
  // 程序入口：跑内嵌自测用例
  final got = buildSynthetic(8, 3, 4); // 把 buildSynthetic(8, 3, 4) 存入 got
  if (got[0].toString() != '[10, 10, 10, 200, 200, 200, 200, 10]')
    throw StateError('bg failed');
  if (got[1].toString() != '[200, 200, 200, 200]')
    throw StateError('puzzle failed');
  if (got[1].length != 4 || got[0].length != 8) throw StateError('lens failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
