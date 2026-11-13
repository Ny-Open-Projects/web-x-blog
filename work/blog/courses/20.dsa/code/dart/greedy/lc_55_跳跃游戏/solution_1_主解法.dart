// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133844403
// LeetCode 55. 跳跃游戏 — Dart 版（方案1）
bool canJump(List<int> nums) {
  // 定义函数/方法 canJump
  var maxReach = 0; // 把 0 存入 maxReach
  for (var i = 0; i < nums.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (i > maxReach) return false; // 若 下标 i 超过 maxReach，直接返回 false
    final r = i + nums[i]; // 把 下标 i 加 数组[下标 i] 存入 右指针
    if (r > maxReach) maxReach = r; // 若 右指针 超过 maxReach) maxReach 赋值为 右指针;
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!canJump([2, 3, 1, 1, 4]))
    throw StateError(
      'c1',
    ); // 若 取反 canJump([2, 3, 1, 1, 4])) throw StateError('c1');
  if (canJump([3, 2, 1, 0, 4]))
    throw StateError(
      'c2',
    ); // 若 canJump([3, 2, 1, 0, 4])) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
