// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133968437
// LeetCode 268. 丢失的数字 — Dart 版（方案1）
int missingNumber(List<int> nums) {
  // 定义函数/方法 missingNumber
  final n = nums.length; // 把 数组.长度 存入 元素个数
  var sum = 0; // 把 0 存入 累计和
  for (final v in nums) {
    sum += v;
  } // 把 值; } 写入 for (final v in nums) { sum +
  return n * (n + 1) ~/ 2 - sum; // 返回 元素个数 乘 (元素个数 加 1) ~ 除以 2 减 累计和
}

void main() {
  if (missingNumber([3, 0, 1]) != 2) throw StateError('c1');
  if (missingNumber([0, 1]) != 2) throw StateError('c2');
  if (missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) != 8) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
