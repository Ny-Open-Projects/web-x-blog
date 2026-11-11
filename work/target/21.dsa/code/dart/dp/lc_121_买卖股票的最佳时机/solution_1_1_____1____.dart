// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130515763
// LeetCode 121. 买卖股票的最佳时机 — Dart 版（方案1）
int maxProfit(List<int> prices) {
  // 定义函数/方法 maxProfit
  var minP = -1, best = 0; // 把 减 1, 当前最优 赋值为 0 存入 minP
  for (final p in prices) {
    // for (final 节点 in 价格序列) {
    if (minP == -1 || p < minP)
      minP = p; // 若 minP 等于 减 1 或 节点 小于 minP) minP 赋值为 节点;
    if (p - minP > best)
      best = p - minP; // 若 节点 减 minP 超过 当前最优) 当前最优 赋值为 节点 减 minP;
  }
  return best; // 返回 当前最优
}

void main() {
  if (maxProfit([7, 1, 5, 3, 6, 4]) != 5) throw StateError('c1');
  if (maxProfit([7, 6, 4, 3, 1]) != 0) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
