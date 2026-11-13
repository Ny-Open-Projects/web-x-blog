// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案4：SAD 绝对差和最佳窗口）
List<int> bestMatchWindow(List<int> bg, List<int> puzzle) {
  // 定义函数/方法 bestMatchWindow
  var bestX = 0; // 把 0 存入 bestX
  var bestScore = 1 << 60; // 把 1 小于 小于 60 存入 bestScore
  final n = puzzle.length; // 把 puzzle.长度 存入 元素个数
  for (var x = 0; x + n <= bg.length; x++) {
    // 让 x 从 0 开始计数，x 加 元素个数 不超过 bg.长度 就继续
    var score = 0; // 把 0 存入 score
    for (var y = 0; y < n; y++) {
      // 让 y 从 0 开始计数，y 小于 元素个数 就继续
      score += (bg[x + y] - puzzle[y])
          .abs(); // score累加 (bg[x 加 y] 减 puzzle[y]).取绝对值 )
    }
    if (score < bestScore) {
      // 若 score 小于 bestScore
      bestScore = score; // 把 score 存入 bestScore
      bestX = x; // 把 x 存入 bestX
    }
  }
  return [bestX, bestScore]; // 返回 [bestX, bestScore]
}

void main() {
  // 程序入口：跑内嵌自测用例
  const bg = <int>[
    10,
    10,
    10,
    10,
    200,
    200,
    200,
    200,
  ]; // 把 小于 int 超过 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
  const puzzle = <int>[
    10,
    200,
    200,
    200,
  ]; // 把 小于 int 超过 [10, 200, 200, 200] 存入 puzzle
  final got = bestMatchWindow(
    bg,
    puzzle,
  ); // 把 bestMatchWindow(bg, puzzle) 存入 got
  if (got[0] != 3 || got[1] != 0) throw StateError('gap failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
