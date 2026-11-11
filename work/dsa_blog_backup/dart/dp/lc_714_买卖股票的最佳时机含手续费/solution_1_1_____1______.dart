// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130741193
// LeetCode 714. 买卖股票的最佳时机含手续费 — Dart 版（方案1）
int maxProfitFee(List<int> prices, int fee) {
  // 定义函数/方法 maxProfitFee
  var hold = -prices[0], sold = 0; // 把 减 价格序列[0], sold 赋值为 0 存入 hold
  for (var i = 1; i < prices.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
    final p = prices[i]; // 把 价格序列[下标 i] 存入 节点
    final nh = hold > sold - p
        ? hold
        : sold - p; // 把 hold 超过 sold 减 节点 ? hold : sold 减 节点 存入 nh
    final ns = sold > hold + p - fee
        ? sold
        : hold +
              p -
              fee; // 把 sold 超过 hold 加 节点 减 fee ? sold : hold 加 节点 减 fee 存入 ns
    hold = nh; // 把 nh 存入 hold
    sold = ns; // 把 ns 存入 sold
  }
  return sold; // 返回 sold
}

void main() {
  if (maxProfitFee([1, 3, 2, 8, 4, 9], 2) != 8) throw StateError('c1');
  if (maxProfitFee([1], 1) != 0) throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
