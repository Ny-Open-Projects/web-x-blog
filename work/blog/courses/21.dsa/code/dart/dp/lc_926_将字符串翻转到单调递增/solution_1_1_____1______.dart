// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130659442
// LeetCode 926. 将字符串翻转到单调递增 — Dart 版（方案1）
int minFlipsMonoIncr(String s) {
  // 定义函数/方法 minFlipsMonoIncr
  var ones = 0, flips = 0; // 把 0, flips 赋值为 0 存入 ones
  for (final c in s.split('')) {
    // for (final 字符 in 字符串.split('')) {
    if (c == '1') {
      ones++;
    } // 若 字符 等于 '1') { ones 加一 ; }
    else {
      // 否则
      flips++; // flips 加一
      if (ones < flips) flips = ones; // 若 ones 小于 flips) flips 赋值为 ones;
    }
  }
  return flips; // 返回 flips
}

void main() {
  if (minFlipsMonoIncr('00110') != 1) throw StateError('c1');
  if (minFlipsMonoIncr('010110') != 2) throw StateError('c2');
  if (minFlipsMonoIncr('00011000') != 2) throw StateError('c3');
  print('PASS');
} // 全部用例通过，输出 PASS
