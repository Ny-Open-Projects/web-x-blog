// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134577890
// LeetCode 179. 最大数 — Dart 版（方案2）
String largestNumber(List<int> nums) {
  // 定义函数/方法 largestNumber
  final strs = nums.map((v) => v.toString()).toList();
  strs.sort((a, b) => (b + a).compareTo(a + b));
  if (strs[0] == '0') return '0'; // 若 strs[0] 等于 '0'，直接返回 '0'
  return strs.join(); // 返回 strs.join()
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (largestNumber([10, 2]) != '210')
    throw StateError(
      'c1',
    ); // 若 largestNumber([10, 2]) 不等于 '210') throw StateError('c1');
  if (largestNumber([3, 30, 34, 5, 9]) != '9534330') throw StateError('c2');
  if (largestNumber([0, 0]) != '0')
    throw StateError(
      'c3',
    ); // 若 largestNumber([0, 0]) 不等于 '0') throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
