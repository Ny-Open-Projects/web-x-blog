// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Dart 版（方案1：二分查找）
int binarySearch(List<int> arr, int target) {
  // 定义函数/方法 binarySearch
  var left = 0, right = arr.length - 1; // 把 0, 右边界 赋值为 数组.长度 减 1 存入 左边界
  while (left <= right) {
    // 循环，直到不满足「左边界 不超过 右边界」
    final mid = left + (right - left) ~/ 2; // 把 左边界 加 (右边界 减 左边界) ~ 除以 2 存入 中点
    if (arr[mid] == target) return mid; // 若 数组[中点] 等于 目标值，直接返回 中点
    if (arr[mid] < target) {
      // 若 数组[中点] 小于 目标值
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
  final cases = <List<int>, List<int>>{
    // 把 小于 List 小于 int 超过 , List 小于 int 超过 超过 { 存入 cases
    // arr -> [target, want]
  };
  final arrs = <List<int>>[
    [1, 3, 5, 7, 9],
    [1, 3, 5, 7, 9],
    <int>[],
    [1, 3, 5, 7, 9],
  ];
  final ts = <int>[5, 4, 5, 1]; // 把 小于 int 超过 [5, 4, 5, 1] 存入 ts
  final ws = <int>[2, -1, -1, 0]; // 把 小于 int 超过 [2, 减 1, 减 1, 0] 存入 ws
  for (var i = 0; i < 4; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 4 就继续
    final got = binarySearch(
      arrs[i],
      ts[i],
    ); // 把 binarySearch(arrs[下标 i], ts[下标 i]) 存入 got
    if (got != ws[i])
      throw StateError('case $i failed: got $got want ${ws[i]}');
  }
  print('PASS'); // 全部用例通过，输出 PASS
}
