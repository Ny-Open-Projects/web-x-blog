// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133524779
// LeetCode 167. 两数之和II — Dart 版（方案1）
List<int> twoSum(List<int> numbers, int target) {
  // 定义函数/方法 twoSum
  var l = 0, r = numbers.length - 1; // 把 0, 右指针 赋值为 numbers.长度 减 1 存入 左指针
  while (l < r) {
    // 循环，直到不满足「左指针 小于 右指针」
    final s = numbers[l] + numbers[r]; // 把 numbers[左指针] 加 numbers[右指针] 存入 字符串
    if (s == target)
      return [l + 1, r + 1]; // 若 字符串 等于 目标值，直接返回 [左指针 加 1, 右指针 加 1]
    if (s < target) {
      l++;
    } else {
      r--;
    } // 若 字符串 小于 目标值) { 左指针 加一 ; } else { 右指针 减一 ; }
  }
  return []; // 返回 []
}

void main() {
  if (twoSum([2, 7, 11, 15], 9).toString() != '[1, 2]') throw StateError('c1');
  if (twoSum([2, 3, 4], 6).toString() != '[1, 3]') throw StateError('c2');
  if (twoSum([-1, 0], -1).toString() != '[1, 2]') throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
