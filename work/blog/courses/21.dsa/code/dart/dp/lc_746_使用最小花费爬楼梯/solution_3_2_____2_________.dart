// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130521152
// LeetCode 746. 使用最小花费爬楼梯 — Dart 版（方案3）
int minCostClimbingStairs(List<int> cost) {
  // 定义函数/方法 minCostClimbingStairs
  var a = 0, b = 0; // 把 0, b 赋值为 0 存入 数组
  for (var i = 2; i <= cost.length; i++) {
    // 让 下标 i 从 2 开始计数，下标 i 不超过 cost.长度 就继续
    final t = (a + cost[i - 2]) < (b + cost[i - 1])
        ? (a + cost[i - 2])
        : (b + cost[i - 1]);
    a = b;
    b = t; // 把 b; b 赋值为 另一字符串 存入 数组
  }
  return b; // 返回 b
}

void main() {
  if (minCostClimbingStairs([10, 15, 20]) != 15) throw StateError('c1');
  if (minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) != 6)
    throw StateError('c2');
  print('PASS');
} // 全部用例通过，输出 PASS
