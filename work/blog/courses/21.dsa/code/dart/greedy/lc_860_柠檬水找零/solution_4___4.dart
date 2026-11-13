// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167617
// LeetCode 860. 柠檬水找零 — Dart 版（方案4）
bool lemonadeChange(List<int> bills) {
  // 定义函数/方法 lemonadeChange
  var f5 = 0, f10 = 0; // 把 0, f10 赋值为 0 存入 f5
  for (final b in bills) {
    // for (final b in bills) {
    if (b == 5) {
      // 若 b 等于 5
      f5++; // f5 加一
    } else if (b == 10) {
      // 否则，若 b 等于 10
      f10++; // f10 加一
      f5--; // f5 减一
    } else {
      // 否则
      if (f10 > 0) {
        // 若 f10 超过 0
        f10--; // f10 减一
        f5--; // f5 减一
      } else {
        // 否则
        f5 -= 3; // f5累减 3
      }
    }
    if (f5 < 0) return false; // 若 f5 小于 0，直接返回 false
  }
  return true; // 返回 true
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (!lemonadeChange([5, 5, 5, 10, 20])) throw StateError('c1');
  if (lemonadeChange([5, 5, 10, 10, 20])) throw StateError('c2');
  if (!lemonadeChange([5, 5, 5, 5, 20])) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
