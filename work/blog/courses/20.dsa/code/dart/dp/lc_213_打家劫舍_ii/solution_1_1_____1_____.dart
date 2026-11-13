// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130716392
// LeetCode 213. 打家劫舍II — Dart 版（方案1）
int robLine(List<int> nums) {
  var a = 0, b = 0;
  for (final v in nums) {
    final t = b > a + v ? b : a + v;
    a = b;
    b = t;
  }
  return b;
}

int robII(List<int> nums) {
  // 定义函数/方法 robII
  if (nums.length == 1) return nums[0]; // 若 数组.长度 等于 1，直接返回 数组[0]
  return robLine(nums.sublist(1))
              .compareTo(robLine(nums.sublist(0, nums.length - 1))) >=
          0
      ? robLine(nums.sublist(1)) // ? robLine(数组.sublist(1))
      : robLine(
          nums.sublist(0, nums.length - 1),
        ); // : robLine(数组.sublist(0, 数组.长度 减 1));
}

void main() {
  if (robII([2, 3, 2]) != 3) throw StateError('c1');
  if (robII([1, 2, 3, 1]) != 4) throw StateError('c2');
  if (robII([1]) != 1) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
