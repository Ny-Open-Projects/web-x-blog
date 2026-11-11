// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Dart 版（方案10）
int findKthLargest(List<int> nums, int k) {
  // 定义函数/方法 findKthLargest
  final a = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 数组
  final n = a.length; // 把 数组.长度 存入 元素个数
  for (var i = n - 1; i > n - 1 - k; i--) {
    // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 超过 元素个数 减 1 减 下标 k 就继续
    for (var j = 0; j < i; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 下标 i 就继续
      if (a[j] > a[j + 1]) {
        // 若 数组[下标 j] 超过 数组[下标 j 加 1]
        final t = a[j]; // 把 数组[下标 j] 存入 另一字符串
        a[j] = a[j + 1]; // 把 数组[下标 j 加 1]; 写入 a[j]
        a[j + 1] = t; // 把 另一字符串; 写入 a[j + 1]
      }
    }
  }
  return a[n - k]; // 返回 数组[元素个数 减 下标 k]
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
