// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 3100. 换水问题 II — Dart 版（方案1）
int maxBottlesDrunk(int numBottles, int numExchange) {
  // 定义函数/方法 maxBottlesDrunk
  var drunk = numBottles, empty = numBottles, ne = numExchange;
  while (empty >= ne) {
    // 循环，直到不满足「empty 不低于 ne」
    empty -= ne; // empty累减 ne
    ne++; // ne 加一
    drunk++; // drunk 加一
    empty++; // empty 加一
  }
  return drunk; // 返回 drunk
}

void main() {
  if (maxBottlesDrunk(10, 3) != 13) throw StateError('c1');
  if (maxBottlesDrunk(1, 2) != 1) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
