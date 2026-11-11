// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Dart 版（方案7）
void quickselect(List<int> a, int l, int r, int k) {
  // 定义函数/方法 quickselect
  if (l >= r) return; // 若 左指针 不低于 右指针) return;
  var i = l, j = r; // 把 左指针, 下标 j 赋值为 右指针 存入 下标 i
  final pivot = a[(l + r) ~/ 2]; // 把 数组[(左指针 加 右指针) ~ 除以 2] 存入 pivot
  while (i <= j) {
    // 循环，直到不满足「下标 i 不超过 下标 j」
    while (a[i] > pivot) i++; // 循环，直到不满足「数组[下标 i] 超过 pivot) 下标 i 加一 ;」
    while (a[j] < pivot) j--; // 循环，直到不满足「数组[下标 j] 小于 pivot) 下标 j 减一 ;」
    if (i <= j) {
      // 若 下标 i 不超过 下标 j
      final t = a[i]; // 把 数组[下标 i] 存入 另一字符串
      a[i] = a[j]; // 把 数组[下标 j]; 写入 a[i]
      a[j] = t; // 把 另一字符串; 写入 a[j]
      i++; // 下标 i 加一
      j--; // 下标 j 减一
    }
  }
  if (k <= j + 1) {
    // 若 下标 k 不超过 下标 j 加 1
    if (l < j)
      quickselect(
        a,
        l,
        j,
        k,
      ); // 若 左指针 小于 下标 j) quickselect(数组, 左指针, 下标 j, 下标 k);
    return; // return;
  }
  if (k >= i + 1 && i < r) quickselect(a, i, r, k);
}

int findKthLargest(List<int> nums, int k) {
  // 定义函数/方法 findKthLargest
  final a = List<int>.from(nums); // 把 List 小于 int 超过 .from(数组) 存入 数组
  quickselect(a, 0, a.length - 1, k); // quickselect(数组, 0, 数组.长度 减 1, 下标 k);
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
