// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135424151
// LeetCode 292. Nim游戏 — Dart 版（方案1）
bool canWinNim(int n) => n % 4 != 0;
void main() {
  // 程序入口：跑内嵌自测用例
  if (canWinNim(4))
    throw StateError('c1'); // 若 canWinNim(4)) throw StateError('c1');
  if (!canWinNim(1) || !canWinNim(2))
    throw StateError(
      'c2',
    ); // 若 取反 canWinNim(1) 或 取反 canWinNim(2)) throw StateError('c2');
  if (canWinNim(8))
    throw StateError('c3'); // 若 canWinNim(8)) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
