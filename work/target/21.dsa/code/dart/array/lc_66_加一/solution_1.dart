// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134707891
// LeetCode 66. 加一 — Dart 版（方案1）
List<int> plusOne(List<int> digits) {
  // 定义函数/方法 plusOne
  final d = List<int>.from(digits); // 把 List 小于 int 超过 .from(digits) 存入 d
  for (var i = d.length - 1; i >= 0; i--) {
    // 让 下标 i 从 d.长度 减 1 开始计数，下标 i 不低于 0 就继续
    if (d[i] < 9) {
      d[i]++;
      return d;
    } // 若 d[下标 i] 小于 9) { d[下标 i] 加一 ; return d; }
    d[i] = 0; // 把 0; 写入 d[i]
  }
  return [1, ...d]; // 返回 [1, ...d]
}

void main() {
  if (plusOne([1, 2, 3]).toString() != '[1, 2, 4]') throw StateError('c1');
  if (plusOne([4, 3, 2, 1]).toString() != '[4, 3, 2, 2]')
    throw StateError('c2');
  if (plusOne([9]).toString() != '[1, 0]') throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
