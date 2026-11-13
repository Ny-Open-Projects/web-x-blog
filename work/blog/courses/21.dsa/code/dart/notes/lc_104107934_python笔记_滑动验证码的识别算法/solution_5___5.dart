// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案5：边缘匹配 findGap 响应曲线）
List<bool> detectEdges(List<int> image) {
  // 定义函数/方法 detectEdges
  final edges = List<bool>.filled(
    image.length,
    false,
  ); // 把 List 小于 bool 超过 .filled(image.长度, false) 存入 边集
  for (var i = 1; i < image.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 image.长度 就继续
    edges[i] =
        (image[i] - image[i - 1]).abs() >
        50; // 把 (image[下标 i] 减 image[下标 i 减 1]).取绝对值 ) 超过 50; 写入 edges[i]
  }
  return edges; // 返回 边集
}

List<dynamic> findGap(List<int> bg, List<int> puzzle) {
  // 定义函数/方法 findGap
  final bgEdges = detectEdges(bg); // 把 detectEdges(bg) 存入 bgEdges
  final puzzleEdges = detectEdges(
    puzzle,
  ); // 把 detectEdges(puzzle) 存入 puzzleEdges
  final responses = <int>[]; // 把 小于 int 超过 [] 存入 responses
  for (var x = 0; x <= bg.length - puzzle.length; x++) {
    // 让 x 从 0 开始计数，x 不超过 bg.长度 减 puzzle.长度 就继续
    var score = 0; // 把 0 存入 score
    for (var y = 0; y < puzzle.length; y++) {
      // 让 y 从 0 开始计数，y 小于 puzzle.长度 就继续
      if (bgEdges[x + y] && puzzleEdges[y])
        score++; // 若 bgEdges[x 加 y] 且 puzzleEdges[y]) score 加一 ;
    }
    responses.add(score); // responses 追加 score);
  }
  var bestX = 0; // 把 0 存入 bestX
  for (var i = 1; i < responses.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 responses.长度 就继续
    if (responses[i] > responses[bestX])
      bestX = i; // 若 responses[下标 i] 超过 responses[bestX]) bestX 赋值为 下标 i;
  }
  return [bestX, responses]; // 返回 [bestX, responses]
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
  final got = findGap(bg, puzzle); // 把 findGap(bg, puzzle) 存入 got
  if (got[0] != 3)
    throw StateError(
      'gap failed',
    ); // 若 got[0] 不等于 3) throw StateError('gap failed');
  if (got[1].toString() != '[0, 0, 0, 1, 0]')
    throw StateError('responses failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
