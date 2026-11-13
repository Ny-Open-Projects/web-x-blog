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
    const graph: { [k: number]: number[][] } = {}; // 把 {}; 写入 const graph: { [k: number]: number[][] }
    for (const f of flights) {
      // for (const f of flights) {
      const frm = f[0],
        to = f[1],
        price = f[2]; // 把 f[0], to 赋值为 f[1], price 赋值为 f[2] 存入 frm
      if (!graph[frm]) graph[frm] = []; // 若 取反 graph[frm]) graph[frm] 赋值为 [];
      graph[frm].push([to, price]); // 把 [to, price] 压入栈/数组尾部
    }
    const memo: { [k: string]: number } = {}; // 把 {}; 写入 const memo: { [k: string]: number }
    function dfs(city: number, rem: number): number {
      // 定义函数/方法 dfs
      if (city === dst) return 0; // 若 city 全等于 dst，直接返回 0
      if (rem === 0) return INF; // 若 rem 全等于 0，直接返回 INF
      const key = city + ',' + rem; // 把 city 加 「,」 加 rem 存入 key
      if (memo[key] !== undefined) return memo[key]; // 若 记忆化表[key] 不等于 undefined，直接返回 记忆化表[key]
      let best = INF; // 把 INF 存入 当前最优
      const edges = graph[city] || []; // 把 graph[city] 或 [] 存入 边集
      for (const e of edges) {
        // for (const e of 边集) {
        const to = e[0],
          price = e[1]; // 把 e[0], price 赋值为 e[1] 存入 to
        const nxt = dfs(to, rem - 1); // 把 dfs(to, rem 减 1) 存入 nxt
        if (nxt !== INF) best = Math.min(best, price + nxt); // 若 nxt 不等于 INF) 当前最优 赋值为 Math.取较小值 当前最优, price 加 nxt);
      }
      memo[key] = best; // 把 当前最优; 写入 memo[key]
      return best; // 返回 当前最优
    }
    const res = dfs(src, k + 1); // 把 dfs(src, 下标 k 加 1) 存入 结果
    return res === INF ? -1 : res; // 返回 结果 全等于 INF ? 减 1 : 结果
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
