// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133907522
// LeetCode 238. 除自身以外数组的乘积 — Dart 版（方案1）
List<int> productExceptSelf(List<int> nums) {
  // 定义函数/方法 productExceptSelf
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final out = List<int>.filled(
    n,
    1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 1) 存入 out
  var left = 1; // 把 1 存入 左边界
  for (var i = 0; i < n; i++) {
    out[i] = left;
    left *= nums[i];
  } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
  var right = 1; // 把 1 存入 右边界
  for (var i = n - 1; i >= 0; i--) {
    out[i] *= right;
    right *= nums[i];
  } // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
  return out; // 返回 out
}

void main() {
  if (productExceptSelf([1, 2, 3, 4]).toString() != '[24, 12, 8, 6]')
    throw StateError('c1');
  if (productExceptSelf([-1, 1, 0, -3, 3]).toString() != '[0, 0, 9, 0, 0]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
