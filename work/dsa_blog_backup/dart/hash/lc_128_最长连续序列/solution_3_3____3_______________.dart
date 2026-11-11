// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167108
// LeetCode 128. 最长连续序列 — Dart 版（方案3）
int longestConsecutive(List<int> nums) {
  // 定义函数/方法 longestConsecutive
  final set = nums.toSet(); // 把 数组.toSet() 存入 set
  var best = 0; // 把 0 存入 当前最优
  for (final num in set) {
    // for (final num in set) {
    if (set.contains(num - 1)) continue; // 若 set 是否包含 num 减 1)) continue;
    var cur = num; // 把 num 存入 当前值
    var streak = 1; // 把 1 存入 streak
    while (set.contains(cur + 1)) {
      // 循环，直到不满足「set 是否包含 当前值 加 1」
      cur++; // 当前值 加一
      streak++; // streak 加一
    }
    if (streak > best) best = streak; // 若 streak 超过 当前最优) 当前最优 赋值为 streak;
  }
  return best; // 返回 当前最优
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (longestConsecutive([100, 4, 200, 1, 3, 2]) != 4) throw StateError('c1');
  if (longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) != 9)
    throw StateError('c2');
  if (longestConsecutive([]) != 0)
    throw StateError(
      'c3',
    ); // 若 longestConsecutive([]) 不等于 0) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
