// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134982348
// LeetCode 977. 有序数组的平方 — Dart 版（方案3）
List<int> sortedSquares(List<int> nums) {
  // 定义函数/方法 sortedSquares
  final n = nums.length; // 把 数组.长度 存入 元素个数
  final out = List<int>.filled(
    n,
    0,
  ); // 把 List 小于 int 超过 .filled(元素个数, 0) 存入 out
  var l = 0,
      r = n - 1,
      idx = n - 1; // 把 0, 右指针 赋值为 元素个数 减 1, idx 赋值为 元素个数 减 1 存入 左指针
  while (l <= r) {
    // 循环，直到不满足「左指针 不超过 右指针」
    final a = nums[l].abs(),
        b = nums[r].abs(); // 把 数组[左指针].取绝对值 ), b 赋值为 数组[右指针].取绝对值 ) 存入 数组
    if (a > b) {
      out[idx--] = a * a;
      l++;
    } // 若 数组 超过 b) { out[idx 减一 ] 赋值为 数组 乘 数组; 左指针 加一 ; }
    else {
      out[idx--] = b * b;
      r--;
    } // 否则
  }
  return out; // 返回 out
}

void main() {
  if (sortedSquares([-4, -1, 0, 3, 10]).toString() != '[0, 1, 9, 16, 100]')
    throw StateError('c1');
  if (sortedSquares([-7, -3, 2, 3, 11]).toString() != '[4, 9, 9, 49, 121]')
    throw StateError('c2');
  if (sortedSquares([1, 2, 3]).toString() != '[1, 4, 9]')
    throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
