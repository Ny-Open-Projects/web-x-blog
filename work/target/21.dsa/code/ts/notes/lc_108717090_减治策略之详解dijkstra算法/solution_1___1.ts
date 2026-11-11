// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
/**
 ** 笔记：减治策略之详解 Dijkstra 算法
 ** 方案：方案1（优先队列实现单源最短路）
 ** 来源：python 参考忠实移植
 */

class MinHeap {
  // 定义类型
  private a: [number, number][] = []; // 把 []; 写入 private a: [number, number][]
  size(): number {
    return this.a.length;
  } // 大小(): number { return this.数组.长度; }
  push(x: [number, number]): void {
    // push(x: [number, number]): void {
    this.a.push(x); // 把 x 压入栈/数组尾部
    let i = this.a.length - 1; // 把 this.数组.长度 减 1 存入 下标 i
    while (i > 0) {
      // 循环，直到不满足「下标 i 超过 0」
      const p = (i - 1) >> 1; // 把 (下标 i 减 1) 超过 超过 1 存入 节点
      if (this.a[p][0] <= this.a[i][0]) break; // 若 this.数组[节点][0] 不超过 this.数组[下标 i][0]) break;
      [this.a[p], this.a[i]] = [this.a[i], this.a[p]]; // 把 [this.数组[下标 i], this.数组[节点]]; 写入 [this.a[p], this.a[i]]
      i = p; // 把 节点 存入 下标 i
    }
  }
  pop(): [number, number] | undefined {
    // pop(): [number, number] 按位或 undefined {
    if (!this.a.length) return undefined; // 若 取反 this.数组.长度，直接返回 undefined
    const top = this.a[0]; // 把 this.数组[0] 存入 top
    const last = this.a.pop()!; // 把 this.数组 弹出 )取反 存入 last
    if (this.a.length) {
      // 若 this.数组.长度
      this.a[0] = last; // 把 last; 写入 this.a[0]
      let i = 0; // 把 0 存入 下标 i
      const n = this.a.length; // 把 this.数组.长度 存入 元素个数
      while (true) {
        // 循环，直到不满足「true」
        let l = 2 * i + 1,
          r = 2 * i + 2,
          s = i; // 把 2 乘 下标 i 加 1, 右指针 赋值为 2 乘 下标 i 加 2, 字符串 赋值为 下标 i 存入 左指针
        if (l < n && this.a[l][0] < this.a[s][0]) s = l;
        if (r < n && this.a[r][0] < this.a[s][0]) s = r;
        if (s === i) break; // 若 字符串 全等于 下标 i) break;
        [this.a[s], this.a[i]] = [this.a[i], this.a[s]]; // 把 [this.数组[下标 i], this.数组[字符串]]; 写入 [this.a[s], this.a[i]]
        i = s; // 把 字符串 存入 下标 i
      }
    }
    return top; // 返回 top
  }
}

function dijkstra(
  graph: [number, number][][],
  src: number,
): [number[], number[]] {
  // 定义函数/方法 dijkstra
  const n = graph.length; // 把 graph.长度 存入 元素个数
  const dist: number[] = new Array(n).fill(Infinity); // 把 new Array(元素个数).fill(Infinity); 写入 const dist: number[]
  dist[src] = 0; // 把 0; 写入 dist[src]
  const parent: number[] = new Array(n).fill(-1); // 把 new Array(元素个数).fill( 减 1); 写入 const parent: number[]
  const pq = new MinHeap(); // 把 new MinHeap() 存入 优先队列
  pq.push([0, src]); // 把 [0, src] 压入栈/数组尾部
  while (pq.size()) {
    // 循环，直到不满足「优先队列.大小(」
    const [d, u] = pq.pop()!; // 弹出栈顶元素
    if (d > dist[u]) continue; // 若 d 超过 dist[节点 u]) continue;
    for (const [v, w] of graph[u]) {
      // for (const [值, 权重] of graph[节点 u]) {
      if (dist[u] + w < dist[v]) {
        // 若 dist[节点 u] 加 权重 小于 dist[值]
        dist[v] = dist[u] + w; // 把 dist[节点 u] 加 权重; 写入 dist[v]
        parent[v] = u; // 把 节点 u; 写入 parent[v]
        pq.push([dist[v], v]); // 把 [dist[值], 值] 压入栈/数组尾部
      }
    }
  }
  return [dist, parent]; // 返回 [dist, parent]
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const graph: [number, number][][] = [
    [
      [1, 4],
      [2, 1],
    ],
    [[3, 1]],
    [
      [1, 2],
      [3, 5],
    ],
    [[4, 3]],
    [],
  ];
  const cases: { src: number; wantDist: number[]; wantParent: number[] }[] = [
    { src: 0, wantDist: [0, 3, 1, 4, 7], wantParent: [-1, 2, 0, 1, 3] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const [gotDist, gotParent] = dijkstra(graph, c.src); // 把 dijkstra(graph, 字符.src); 写入 const [gotDist, gotParent]
    if (!eqArr(gotDist, c.wantDist) || !eqArr(gotParent, c.wantParent)) {
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL src',
        c.src,
        'want',
        JSON.stringify(c.wantDist),
        JSON.stringify(c.wantParent),
        'got',
        JSON.stringify(gotDist),
        JSON.stringify(gotParent),
      ); // 「got」, JSON.stringify(gotDist), JSON.stringify(gotParent));
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
