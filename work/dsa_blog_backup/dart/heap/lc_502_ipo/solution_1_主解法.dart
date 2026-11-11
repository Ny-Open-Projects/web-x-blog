// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136847926
// LeetCode 502. IPO — Dart 版（方案1）
int findMaximizedCapital(int k, int w, List<int> profits, List<int> capital) {
  // 定义函数/方法 findMaximizedCapital
  final n = profits.length; // 把 profits.长度 存入 元素个数
  final used = List<bool>.filled(
    n,
    false,
  ); // 把 List 小于 bool 超过 .filled(元素个数, false) 存入 已用标记
  for (var t = 0; t < k; t++) {
    // 让 另一字符串 从 0 开始计数，另一字符串 小于 下标 k 就继续
    var best = -1; // 把 减 1 存入 当前最优
    var bestJ = -1; // 把 减 1 存入 bestJ
    for (var j = 0; j < n; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
      if (!used[j] && capital[j] <= w && profits[j] > best) {
        best = profits[j]; // 把 profits[下标 j] 存入 当前最优
        bestJ = j; // 把 下标 j 存入 bestJ
      }
    }
    if (bestJ < 0) break; // 若 bestJ 小于 0) break;
    w += best; // 权重累加 当前最优
    used[bestJ] = true; // 把 true; 写入 used[bestJ]
  }
  return w; // 返回 权重
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) != 4)
    throw StateError('c1');
  if (findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) != 6)
    throw StateError('c2');
  if (findMaximizedCapital(1, 0, [1, 2], [1, 2]) != 0) throw StateError('c3');
  if (findMaximizedCapital(2, 1, [1, 2, 3], [1, 1, 2]) != 6)
    throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
