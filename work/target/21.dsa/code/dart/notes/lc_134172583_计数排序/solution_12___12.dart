// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
// 数据结构与算法之排序: 计数排序 — Dart 版（方案12）
List<int> countSort(List<int> nums) {
  // 定义函数/方法 countSort
  if (nums.isEmpty) return nums; // 若 数组.isEmpty，直接返回 数组
  var mx = nums[0], mn = nums[0]; // 把 数组[0], mn 赋值为 数组[0] 存入 mx
  for (final v in nums) {
    if (v > mx) mx = v;
    if (v < mn) mn = v;
  }
  final range = mx - mn + 1; // 把 mx 减 mn 加 1 存入 range
  final count = List<int>.filled(
    range,
    0,
  ); // 把 List 小于 int 超过 .filled(range, 0) 存入 计数
  final output = List<int>.filled(
    nums.length,
    0,
  ); // 把 List 小于 int 超过 .filled(数组.长度, 0) 存入 输出
  for (final v in nums) {
    count[v - mn]++;
  } // for (final 值 in 数组) { 计数[值 减 mn] 加一 ; }
  for (var i = 1; i < range; i++) {
    count[i] += count[i - 1];
  } // 让 下标 i 从 1 开始计数，下标 i 小于 range 就继续
  for (var i = nums.length - 1; i >= 0; i--) {
    // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 不低于 0 就继续
    output[count[nums[i] - mn] - 1] =
        nums[i]; // 把 数组[下标 i]; 写入 output[count[nums[i] - mn] - 1]
    count[nums[i] - mn]--; // 计数[数组[下标 i] 减 mn] 减一 ;
  }
  return output; // 返回 输出
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (countSort([5, 3, 8, 3, 1]).toString() != '[1, 3, 3, 5, 8]')
    throw StateError('c1');
  final big = countSort([
    102,
    103,
    108,
    107,
    101,
    102,
    102,
    102,
    107,
    103,
    109,
    108,
    102,
    101,
    104,
    102,
    104,
    106,
    109,
    102,
  ]);
  if (big.length != 20 || big.first != 101 || big.last != 109)
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
