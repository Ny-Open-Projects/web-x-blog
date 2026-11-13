// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
// LeetCode 922. 按奇偶排序数组II — Dart 版（方案7）
List<int> sortArrayByParityII(List<int> nums) {
  // 定义函数/方法 sortArrayByParityII
  final sorted = List<int>.from(nums)
    ..sort(); // 把 List 小于 int 超过 .from(数组). 排序 ) 存入 sorted
  final res = List<int>.filled(
    sorted.length,
    0,
  ); // 把 List 小于 int 超过 .filled(sorted.长度, 0) 存入 结果
  var odd = 1, even = 0; // 把 1, even 赋值为 0 存入 odd
  for (final item in sorted) {
    // for (final item in sorted) {
    if (item % 2 != 0) {
      // 若 item 对…取模 2 不等于 0
      res[odd] = item; // 把 item; 写入 res[odd]
      odd += 2; // odd累加 2
    } else {
      // 否则
      res[even] = item; // 把 item; 写入 res[even]
      even += 2; // even累加 2
    }
  }
  return res; // 返回 结果
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (sortArrayByParityII([4, 2, 5, 7]).toString() != '[2, 5, 4, 7]')
    throw StateError('c1');
  if (sortArrayByParityII([2, 3]).toString() != '[2, 3]')
    throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
