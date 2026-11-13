// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
// LeetCode 2454. 下一个更大元素 IV — Dart 版（方案1）
List<int> secondGreater(List<int> nums) {
  // 定义函数/方法 secondGreater
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final res = List<int>.filled(
    n,
    -1,
  ); // 把 List 小于 int 超过 .filled(元素个数, 减 1) 存入 结果
  final s1 = <int>[]; // 把 小于 int 超过 [] 存入 s1
  final s2 = <int>[]; // 把 小于 int 超过 [] 存入 s2
  for (var i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    while (s2.isNotEmpty && nums[s2.last] < nums[i]) {
      // 循环，直到不满足「s2.isNotEmpty 且 数组[s2.last] 小于 数组[下标 i]」
      res[s2.removeLast()] = nums[i]; // 把 数组[下标 i]; 写入 res[s2.removeLast()]
    }
    while (s1.isNotEmpty && nums[s1.last] < nums[i]) {
      // 循环，直到不满足「s1.isNotEmpty 且 数组[s1.last] 小于 数组[下标 i]」
      s2.add(s1.removeLast()); // s2 追加 s1.removeLast());
    }
    s1.add(i); // s1 追加 下标 i);
  }
  return res; // 返回 结果
}

void main() {
  if (secondGreater([2, 4, 0, 9, 6]).toString() != '[9, 6, 6, -1, -1]')
    throw StateError('c1');
  if (secondGreater([5, 4, 3, 2, 1]).toString() != '[-1, -1, -1, -1, -1]')
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
