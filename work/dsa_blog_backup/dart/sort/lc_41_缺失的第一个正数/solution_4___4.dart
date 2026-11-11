// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066015
// LeetCode 41. 缺失的第一个正数 — Dart 版（方案4）
int firstMissingPositive(List<int> nums) {
  // 定义函数/方法 firstMissingPositive
  if (nums.isEmpty) return 1; // 若 数组.isEmpty，直接返回 1
  final pos = nums.where((v) => v > 0).toList()..sort();
  if (pos.isEmpty) return 1; // 若 pos.isEmpty，直接返回 1
  if (pos[0] != 1) return 1; // 若 pos[0] 不等于 1，直接返回 1
  final n = pos.length; // 把 pos.长度 存入 元素个数
  for (var i = 0; i < n - 1; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 减 1 就继续
    if (pos[i + 1] - pos[i] > 1)
      return pos[i] + 1; // 若 pos[下标 i 加 1] 减 pos[下标 i] 超过 1，直接返回 pos[下标 i] 加 1
  }
  return pos[n - 1] + 1; // 返回 pos[元素个数 减 1] 加 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (firstMissingPositive([1, 2, 0]) != 3) throw StateError('c1');
  if (firstMissingPositive([3, 4, -1, 1]) != 2) throw StateError('c2');
  if (firstMissingPositive([7, 8, 9, 11, 12]) != 1) throw StateError('c3');
  if (firstMissingPositive([]) != 1)
    throw StateError(
      'c4',
    ); // 若 firstMissingPositive([]) 不等于 1) throw StateError('c4');
  print('PASS'); // 全部用例通过，输出 PASS
}
