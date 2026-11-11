// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — Dart 版（方案2：哈希表一次遍历）
List<int> twoSum(List<int> nums, int target) {
  // 定义函数/方法 twoSum
  final seen = <int, int>{}; // 把 小于 int, int 超过 {} 存入 已见集合
  for (var i = 0; i < nums.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    final need = target - nums[i]; // 把 目标值 减 数组[下标 i] 存入 need
    if (seen.containsKey(need))
      return [
        seen[need]!,
        i,
      ]; // 若 已见集合.containsKey(need)，直接返回 [已见集合[need]取反 , 下标 i]
    seen[nums[i]] = i; // 把 下标 i; 写入 seen[nums[i]]
  }
  return []; // 返回 []
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (twoSum([2, 7, 11, 15], 9).toString() != '[0, 1]') throw StateError('c1');
  if (twoSum([3, 2, 4], 6).toString() != '[1, 2]') throw StateError('c2');
  if (twoSum([3, 3], 6).toString() != '[0, 1]') throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
