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
    const w: number[][] = []; // 把 []; 写入 const w: number[][]
    for (let i = 0; i < n; i++) {
      w.push(new Array(n).fill(INF));
      w[i][i] = 0;
    } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (const f of flights) {
      w[f[0]][f[1]] = f[2];
    } // 把 f[2]; } 写入 for (const f of flights) { w[f[0]][f[1]]
    const dist: number[] = new Array(n).fill(INF); // 把 new Array(元素个数).fill(INF); 写入 const dist: number[]
    dist[src] = 0; // 把 0; 写入 dist[src]
    for (let pass = 0; pass < k + 1; pass++) {
      // 让 pass 从 0 开始计数，pass 小于 下标 k 加 1 就继续
      const prev = dist.slice(); // 把 dist 截取 ) 存入 前一个
      for (let i = 0; i < n; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
        if (prev[i] === INF) continue; // 若 前一个[下标 i] 全等于 INF) continue;
        for (let j = 0; j < n; j++) {
          // 让 下标 j 从 0 开始计数，下标 j 小于 元素个数 就继续
          if (prev[i] + w[i][j] < dist[j]) dist[j] = prev[i] + w[i][j];
        }
      }
    }
    return dist[dst] === INF ? -1 : dist[dst]; // 返回 dist[dst] 全等于 INF ? 减 1 : dist[dst]
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
