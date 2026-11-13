// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
// LeetCode 35. 搜索插入位置 — Dart 版（方案1：二分查找）
int searchInsert(List<int> nums, int target) {
  // 定义函数/方法 searchInsert
  var left = 0, right = nums.length; // 把 0, 右边界 赋值为 数组.长度 存入 左边界
  while (left < right) {
    // 循环，直到不满足「左边界 小于 右边界」
    final mid = left + (right - left) ~/ 2; // 把 左边界 加 (右边界 减 左边界) ~ 除以 2 存入 中点
    if (nums[mid] < target) {
      // 若 数组[中点] 小于 目标值
      left = mid + 1; // 把 中点 加 1 存入 左边界
    } else {
      // 否则
      right = mid; // 把 中点 存入 右边界
    }
  }
  return left; // 返回 左边界
}

void main() {
  // 程序入口：跑内嵌自测用例
  final r = <bool>[
    searchInsert([1, 2, 3], 1) == 0,
    searchInsert([1, 3, 5, 6], 5) == 2,
    searchInsert([1, 3, 5, 6], 2) == 1,
    searchInsert([1, 3, 5, 6], 7) == 4,
    searchInsert([1, 3, 5, 6], 0) == 0,
  ];
  if (r.any((e) => !e)) throw StateError('case failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
