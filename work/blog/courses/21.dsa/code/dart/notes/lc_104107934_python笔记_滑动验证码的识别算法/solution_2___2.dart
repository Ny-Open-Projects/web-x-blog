// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案2：Sobel 中心差分边缘 + 匹配）
List<bool> detectEdgesSobel(List<int> image) {
  // 定义函数/方法 detectEdgesSobel
  final n = image.length; // 把 image.长度 存入 元素个数
  final edges = List<bool>.filled(
    n,
    false,
  ); // 把 List 小于 bool 超过 .filled(元素个数, false) 存入 边集
  if (n < 2) return edges; // 若 元素个数 小于 2，直接返回 边集
  edges[0] =
      (image[1] - image[0]).abs() >
      50; // 把 (image[1] 减 image[0]).取绝对值 ) 超过 50; 写入 edges[0]
  for (var i = 1; i < n - 1; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 元素个数 减 1 就继续
    edges[i] = (image[i + 1] - image[i - 1]).abs() > 50;
  }
  edges[n - 1] = (image[n - 1] - image[n - 2]).abs() > 50;
  return edges; // 返回 边集
}

int recognizeCaptcha(List<int> bg, List<int> puzzle) {
  // 定义函数/方法 recognizeCaptcha
  final bgEdges = detectEdgesSobel(bg); // 把 detectEdgesSobel(bg) 存入 bgEdges
  final puzzleEdges = detectEdgesSobel(
    puzzle,
  ); // 把 detectEdgesSobel(puzzle) 存入 puzzleEdges
  var bestX = 0; // 把 0 存入 bestX
  var bestScore = -1; // 把 减 1 存入 bestScore
  for (var x = 0; x <= bg.length - puzzle.length; x++) {
    // 让 x 从 0 开始计数，x 不超过 bg.长度 减 puzzle.长度 就继续
    var score = 0; // 把 0 存入 score
    for (var y = 0; y < puzzle.length; y++) {
      // 让 y 从 0 开始计数，y 小于 puzzle.长度 就继续
      if (bgEdges[x + y] && puzzleEdges[y])
        score++; // 若 bgEdges[x 加 y] 且 puzzleEdges[y]) score 加一 ;
    }
    if (score > bestScore) {
      // 若 score 超过 bestScore
      bestScore = score; // 把 score 存入 bestScore
      bestX = x; // 把 x 存入 bestX
    }
  }
  return bestX; // 返回 bestX
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
  if (recognizeCaptcha(bg, puzzle) != 3) throw StateError('gap failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
