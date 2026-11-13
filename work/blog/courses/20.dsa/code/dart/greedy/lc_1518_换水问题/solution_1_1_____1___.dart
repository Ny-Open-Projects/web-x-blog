// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 1518. 换水问题 — Dart 版（方案1）
int numWaterBottles(int numBottles, int numExchange) {
  // 定义函数/方法 numWaterBottles
  var ans = numBottles; // 把 numBottles 存入 答案
  var empty = numBottles; // 把 numBottles 存入 empty
  while (empty >= numExchange) {
    // 循环，直到不满足「empty 不低于 numExchange」
    final newB = empty ~/ numExchange; // 把 empty ~ 除以 numExchange 存入 newB
    ans += newB; // 答案累加 newB
    empty =
        newB + empty % numExchange; // 把 newB 加 empty 对…取模 numExchange 存入 empty
  }
  return ans; // 返回 答案
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (numWaterBottles(9, 3) != 13)
    throw StateError(
      'c1',
    ); // 若 numWaterBottles(9, 3) 不等于 13) throw StateError('c1');
  if (numWaterBottles(15, 4) != 19)
    throw StateError(
      'c2',
    ); // 若 numWaterBottles(15, 4) 不等于 19) throw StateError('c2');
  print('PASS'); // 全部用例通过，输出 PASS
}
