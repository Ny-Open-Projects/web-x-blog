// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — Dart 版（方案1：暴力双循环）
List<int> twoSum(List<int> nums, int target) {
  // 定义函数/方法 twoSum
  final n = nums.length; // 把 数组.长度 存入 元素个数
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (var j = i + 1; j < n; j++) {
      // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 元素个数 就继续
      if (nums[i] + nums[j] == target)
        return [i, j]; // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值，直接返回 [下标 i, 下标 j]
    }
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
