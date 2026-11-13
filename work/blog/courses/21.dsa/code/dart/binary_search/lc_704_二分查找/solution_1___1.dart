// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
// LeetCode 704. 二分查找 — Dart 版（方案1：经典二分查找，闭区间 [left, right]）

int search(List<int> nums, int target) {
  // 定义函数/方法 search
  var left = 0; // 把 0 存入 左边界
  var right = nums.length - 1; // 把 数组.长度 减 1 存入 右边界
  while (left <= right) {
    // 循环，直到不满足「左边界 不超过 右边界」
    final mid = left + (right - left) ~/ 2; // 把 左边界 加 (右边界 减 左边界) ~ 除以 2 存入 中点
    final v = nums[mid]; // 把 数组[中点] 存入 值
    if (v == target) {
      // 若 值 等于 目标值
      return mid; // 返回 中点
    } else if (v < target) {
      // 否则，若 值 小于 目标值
      left = mid + 1; // 把 中点 加 1 存入 左边界
    } else {
      // 否则
      right = mid - 1; // 把 中点 减 1 存入 右边界
    }
  }
  return -1; // 返回 减 1
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (search([1, 2, 3], 1) != 0) throw StateError('case 1 failed');
  if (search([-1, 0, 3, 5, 9, 12], 9) != 4) throw StateError('case 2 failed');
  if (search([-1, 0, 3, 5, 9, 12], 2) != -1) throw StateError('case 3 failed');
  print('PASS'); // 全部用例通过，输出 PASS
}
