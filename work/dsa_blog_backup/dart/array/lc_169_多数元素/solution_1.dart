// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133531071
// LeetCode 169. 多数元素 — Dart 版（方案1）
int majorityElement(List<int> nums) {
  // 定义函数/方法 majorityElement
  final counts = <int, int>{}; // 把 小于 int, int 超过 {} 存入 counts
  var best = nums[0], bn = 0; // 把 数组[0], bn 赋值为 0 存入 当前最优
  for (final v in nums) {
    // for (final 值 in 数组) {
    final c = (counts[v] ?? 0) + 1; // 把 (counts[值] ?? 0) 加 1 存入 字符
    counts[v] = c; // 把 字符; 写入 counts[v]
    if (c > bn) {
      bn = c;
      best = v;
    } // 若 字符 超过 bn) { bn 赋值为 字符; 当前最优 赋值为 值; }
  }
  return best; // 返回 当前最优
}

void main() {
  if (majorityElement([3, 2, 3]) != 3) throw StateError('c1');
  if (majorityElement([2, 2, 1, 1, 1, 2, 2]) != 2) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
