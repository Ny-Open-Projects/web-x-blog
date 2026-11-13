// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130588647
// LeetCode 123. 买卖股票的最佳时机III — Dart 版（方案2）
int maxProfitIII(List<int> prices) {
  // 定义函数/方法 maxProfitIII
  var buy1 = -1000000000, sell1 = 0, buy2 = -1000000000, sell2 = 0;
  for (final p in prices) {
    // for (final 节点 in 价格序列) {
    buy1 = buy1 > -p ? buy1 : -p; // 把 buy1 超过 减 节点 ? buy1 : 减 节点 存入 buy1
    sell1 = sell1 > buy1 + p
        ? sell1
        : buy1 + p; // 把 sell1 超过 buy1 加 节点 ? sell1 : buy1 加 节点 存入 sell1
    buy2 = buy2 > sell1 - p
        ? buy2
        : sell1 - p; // 把 buy2 超过 sell1 减 节点 ? buy2 : sell1 减 节点 存入 buy2
    sell2 = sell2 > buy2 + p
        ? sell2
        : buy2 + p; // 把 sell2 超过 buy2 加 节点 ? sell2 : buy2 加 节点 存入 sell2
  }
  return sell2; // 返回 sell2
}

void main() {
  // 程序入口：跑内嵌自测用例
  if (maxProfitIII([1, 2, 3]) != 2)
    throw StateError(
      'c1',
    ); // 若 maxProfitIII([1,2,3]) 不等于 2) throw StateError('c1');
  if (maxProfitIII([1, 2, 3, 4, 5]) != 4)
    throw StateError(
      'c2',
    ); // 若 maxProfitIII([1,2,3,4,5]) 不等于 4) throw StateError('c2');
  if (maxProfitIII([7, 6, 4, 3, 1]) != 0)
    throw StateError(
      'c3',
    ); // 若 maxProfitIII([7,6,4,3,1]) 不等于 0) throw StateError('c3');
  if (maxProfitIII([3, 3, 5, 0, 0, 3, 1, 4]) != 6) throw StateError('c4');
  if (maxProfitIII([1]) != 0)
    throw StateError(
      'c5',
    ); // 若 maxProfitIII([1]) 不等于 0) throw StateError('c5');
  if (maxProfitIII([1, 2]) != 1)
    throw StateError(
      'c6',
    ); // 若 maxProfitIII([1,2]) 不等于 1) throw StateError('c6');
  print('PASS');
} // 全部用例通过，输出 PASS
