// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Dart 版（方案3：NCC 归一化互相关）
import 'dart:math' as math; // 引入依赖

int nccMatch(List<int> bg, List<int> puzzle) {
  // 定义函数/方法 nccMatch
  var bestX = 0; // 把 0 存入 bestX
  var bestScore = -double.infinity; // 把 减 double.infinity 存入 bestScore
  final n = puzzle.length; // 把 puzzle.长度 存入 元素个数
  for (var x = 0; x + n <= bg.length; x++) {
    // 让 x 从 0 开始计数，x 加 元素个数 不超过 bg.长度 就继续
    var bw = 0.0, pw = 0.0; // 把 0.0, pw 赋值为 0.0 存入 bw
    for (var i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      bw += bg[x + i]; // bw累加 bg[x 加 下标 i]
      pw += puzzle[i]; // pw累加 puzzle[下标 i]
    }
    bw /= n; // 把 元素个数; 写入 bw /
    pw /= n; // 把 元素个数; 写入 pw /
    var num = 0.0, db = 0.0, dp = 0.0; // 把 0.0, db 赋值为 0.0, DP 表 赋值为 0.0 存入 num
    for (var i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      final a = bg[x + i] - bw; // 把 bg[x 加 下标 i] 减 bw 存入 数组
      final b = puzzle[i] - pw; // 把 puzzle[下标 i] 减 pw 存入 b
      num += a * b; // num累加 数组 乘 b
      db += a * a; // db累加 数组 乘 数组
      dp += b * b; // DP 表累加 b 乘 b
    }
    final denom =
        math.sqrt(db) *
        math.sqrt(dp); // 把 math.sqrt(db) 乘 math.sqrt(DP 表) 存入 denom
    final score = denom != 0.0
        ? num / denom
        : 0.0; // 把 denom 不等于 0.0 ? num 除以 denom : 0.0 存入 score
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
  if (nccMatch(bg, puzzle) != 3) throw StateError('gap failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
