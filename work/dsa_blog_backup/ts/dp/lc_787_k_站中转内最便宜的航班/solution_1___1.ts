// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130717572
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function findCheapestPrice(
    n: number,
    flights: number[][],
    src: number,
    dst: number,
    k: number,
  ): number {
    // 定义函数/方法 findCheapestPrice
    const INF = Infinity; // 把 Infinity 存入 INF
    const dp: number[][] = []; // 把 []; 写入 const dp: number[][]
    for (let i = 0; i < k + 2; i++) dp.push(new Array(n).fill(INF)); // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 加 2 就继续
    for (let i = 0; i < k + 2; i++) dp[i][src] = 0; // 让 下标 i 从 0 开始计数，下标 i 小于 下标 k 加 2 就继续
    for (let i = 1; i <= k + 1; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 不超过 下标 k 加 1 就继续
      for (const f of flights) {
        // for (const f of flights) {
        const frm = f[0],
          to = f[1],
          price = f[2]; // 把 f[0], to 赋值为 f[1], price 赋值为 f[2] 存入 frm
        if (dp[i - 1][frm] !== INF)
          dp[i][to] = Math.min(dp[i][to], dp[i - 1][frm] + price);
      }
    }
    let ans = INF; // 把 INF 存入 答案
    for (let i = 1; i <= k + 1; i++) ans = Math.min(ans, dp[i][dst]); // 让 下标 i 从 1 开始计数，下标 i 不超过 下标 k 加 1 就继续
    return ans === INF ? -1 : ans; // 返回 答案 全等于 INF ? 减 1 : 答案
  }
  const cases = [
    {
      n: 4,
      flights: [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200],
      ],
      src: 0,
      dst: 3,
      k: 1,
      want: 700,
    },
    {
      n: 4,
      flights: [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200],
      ],
      src: 0,
      dst: 0,
      k: 1,
      want: 0,
    },
    {
      n: 3,
      flights: [
        [0, 1, 1],
        [1, 2, 1],
      ],
      src: 0,
      dst: 2,
      k: 1,
      want: 2,
    },
    { n: 3, flights: [[0, 1, 1]], src: 0, dst: 2, k: 1, want: -1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = findCheapestPrice(c.n, c.flights, c.src, c.dst, c.k);
    if (got !== c.want) {
      fail = true;
      console.log(
        'FAIL findCheapestPrice n=' + c.n + ' want ' + c.want + ' got ' + got,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
