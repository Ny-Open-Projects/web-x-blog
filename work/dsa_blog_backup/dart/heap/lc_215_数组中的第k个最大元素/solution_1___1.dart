// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Dart 版（方案1）
int findKthLargest(List<int> nums, int k) {
  // 定义函数/方法 findKthLargest
  final a = List<int>.from(nums)..sort((x, y) => y.compareTo(x));
  return a[k - 1]; // 返回 数组[下标 k 减 1]
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (findKthLargest([3, 2, 1, 5, 6, 4], 2) != 5) throw StateError('c1');
  if (findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) != 4)
    throw StateError('c2');
  if (findKthLargest([1], 1) != 1)
    throw StateError(
      'c3',
    ); // 若 findKthLargest([1], 1) 不等于 1) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
