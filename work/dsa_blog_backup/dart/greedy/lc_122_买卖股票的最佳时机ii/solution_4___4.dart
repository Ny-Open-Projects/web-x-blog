// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133925028
// LeetCode 122. 买卖股票的最佳时机II — Dart 版（方案4）
int maxProfit(List<int> prices) {
  // 定义函数/方法 maxProfit
  var profit = 0; // 把 0 存入 profit
  for (var i = 1; i < prices.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 价格序列.长度 就继续
    if (prices[i] > prices[i - 1]) {
      // 若 价格序列[下标 i] 超过 价格序列[下标 i 减 1]
      profit +=
          prices[i] - prices[i - 1]; // profit累加 价格序列[下标 i] 减 价格序列[下标 i 减 1]
    }
  }
  return profit; // 返回 profit
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (maxProfit([7, 1, 5, 3, 6, 4]) != 7) throw StateError('c1');
  if (maxProfit([1, 2, 3, 4, 5]) != 4)
    throw StateError(
      'c2',
    ); // 若 maxProfit([1, 2, 3, 4, 5]) 不等于 4) throw StateError('c2');
  if (maxProfit([7, 6, 4, 3, 1]) != 0)
    throw StateError(
      'c3',
    ); // 若 maxProfit([7, 6, 4, 3, 1]) 不等于 0) throw StateError('c3');
  print('PASS'); // 全部用例通过，输出 PASS
}
