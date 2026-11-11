/**
 ** LeetCode 746. 使用最小花费爬楼梯
 ** 方案：1 ) 方案1: 动态规划
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144853675
 */

function minCostClimbingStairs(cost: number[]): number {
  // 定义函数/方法 minCostClimbingStairs
  const n = cost.length; // 把 cost.长度 存入 元素个数
  let prev2 = cost[0]; // 把 cost[0] 存入 prev2
  let prev1 = cost[1]; // 把 cost[1] 存入 prev1
  for (let i = 2; i < n; i++) {
    // 让 下标 i 从 2 开始计数，下标 i 小于 元素个数 就继续
    const cur = cost[i] + Math.min(prev1, prev2); // 把 cost[下标 i] 加 Math.取较小值 prev1, prev2) 存入 当前值
    prev2 = prev1; // 把 prev1 存入 prev2
    prev1 = cur; // 把 当前值 存入 prev1
  }
  return Math.min(prev1, prev2); // 返回 Math.取较小值 prev1, prev2)
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number][] = [
    [[10, 15, 20], 15],
    [[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6],
  ];
  for (const [cost, want] of cases) {
    // for (const [cost, want] of cases) {
    const got = minCostClimbingStairs(cost); // 把 minCostClimbingStairs(cost) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error('FAIL: got ' + got + ' expected ' + want); // throw new Error(「FAIL: got 」 加 got 加 「FAIL: got 」 加 want);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
