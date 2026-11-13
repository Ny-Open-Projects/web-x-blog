// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136236962
// LeetCode 1685. 有序数组中差绝对值之和 — Dart 版（方案1）
List<int> getSumAbsoluteDifferences(List<int> nums) {
  // 定义函数/方法 getSumAbsoluteDifferences
  final n = nums.length; // 把 数组.长度 存入 元素个数
  var total = 0; // 把 0 存入 总和
  for (final v in nums) {
    total += v;
  } // 把 值; } 写入 for (final v in nums) { total +
  var prefix = 0; // 把 0 存入 prefix
  final out = <int>[]; // 把 小于 int 超过 [] 存入 out
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    final v = nums[i]; // 把 数组[下标 i] 存入 值
    final left = v * i - prefix; // 把 值 乘 下标 i 减 prefix 存入 左边界
    final right =
        (total - prefix - v) -
        v * (n - 1 - i); // 把 (总和 减 prefix 减 值) 减 值 乘 (元素个数 减 1 减 下标 i) 存入 右边界
    out.add(left + right); // out 追加 左边界 加 右边界);
    prefix += v; // prefix累加 值
  }
  return out; // 返回 out
}

void main() {
  if (getSumAbsoluteDifferences([2, 3, 5]).toString() != '[4, 3, 5]')
    throw StateError('c1');
  if (getSumAbsoluteDifferences([1, 4, 6, 8, 10]).toString() !=
      '[24, 15, 13, 15, 21]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
