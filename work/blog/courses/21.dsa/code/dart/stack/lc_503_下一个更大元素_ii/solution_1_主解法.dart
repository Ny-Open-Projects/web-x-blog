// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145045460
// LeetCode 503. 下一个更大元素 II — Dart 版（方案1）
List<int> nextGreaterElements(List<int> nums) {
  // 定义函数/方法 nextGreaterElements
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final res = List<int>.filled(
    n,
    -1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 减 1) 存入 结果
  final st = <int>[]; // 把 小于 int 超过 [] 存入 st
  for (var i = 0; i < 2 * n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 2 乘 元素个数 就继续
    final ii = i % n; // 把 下标 i 对…取模 元素个数 存入 ii
    while (st.isNotEmpty && nums[st.last] < nums[ii]) {
      // 循环，直到不满足「st.isNotEmpty 且 数组[st.last] 小于 数组[ii]」
      res[st.removeLast()] = nums[ii]; // 把 数组[ii]; 写入 res[st.removeLast()]
    }
    if (i < n) st.add(ii); // 若 下标 i 小于 元素个数) st 追加 ii);
  }
  return res; // 返回 结果
}

void main() {
  if (nextGreaterElements([1, 2, 1]).toString() != '[2, -1, 2]')
    throw StateError('c1');
  if (nextGreaterElements([3, 2, 1]).toString() != '[-1, 3, 3]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
