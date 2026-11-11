// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145380834
// Faithful translation of python reference. Self-check via demo().
function minimumTime(n: number, relations: number[][], time: number[]): number {
  // 定义函数/方法 minimumTime
  const graph: number[][] = Array.from({ length: n + 1 }, () => []);
  const indeg: number[] = new Array(n + 1).fill(0); // 把 new Array(元素个数 加 1).fill(0); 写入 const indeg: number[]
  for (const [u, v] of relations) {
    graph[u].push(v);
    indeg[v]++;
  } // 把 值 压入栈/数组尾部
  const dp: number[] = new Array(n + 1).fill(0); // 把 new Array(元素个数 加 1).fill(0); 写入 const dp: number[]
  for (let i = 1; i <= n; i++) dp[i] = time[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
  const q: number[] = []; // 把 []; 写入 const q: number[]
  for (let i = 1; i <= n; i++) if (indeg[i] === 0) q.push(i); // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
  while (q.length) {
    // 循环，直到不满足「节点.长度」
    const u = q.shift()!; // 把 节点.shift()取反 存入 节点 u
    for (const v of graph[u]) {
      // for (const 值 of graph[节点 u]) {
      dp[v] = Math.max(dp[v], dp[u] + time[v - 1]); // 把 Math.取较大值 DP 表[值], DP 表[节点 u] 加 time[值 减 1]); 写入 dp[v]
      indeg[v]--; // indeg[值] 减一 ;
      if (indeg[v] === 0) q.push(v); // 若 indeg[值] 全等于 0) 节点 追加 值);
    }
  }
  let ans = 0; // 把 0 存入 答案
  for (let i = 1; i <= n; i++) if (dp[i] > ans) ans = dp[i]; // 让 下标 i 从 1 开始计数，下标 i 不超过 元素个数 就继续
  return ans; // 返回 答案
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    [
      3,
      [
        [1, 3],
        [2, 3],
      ],
      [3, 2, 5],
    ],
    [
      5,
      [
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
      ],
      [1, 2, 3, 4, 5],
    ],
    [1, [], [5]],
  ];
  const want = [8, 15, 5]; // 把 [8, 15, 5] 存入 want
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = minimumTime(cases[i][0], cases[i][1], cases[i][2]);
    if (got !== want[i])
      throw new Error('FAIL case ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
