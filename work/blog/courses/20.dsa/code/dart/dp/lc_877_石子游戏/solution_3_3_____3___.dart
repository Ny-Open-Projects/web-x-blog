// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130709323
// LeetCode 877. 石子游戏 — Dart 版（方案3）
bool stoneGame(List<int> piles) => true;
void main() {
  if (!stoneGame([5, 3, 4, 5])) throw StateError('c1');
  if (!stoneGame([3, 7, 2, 3])) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
