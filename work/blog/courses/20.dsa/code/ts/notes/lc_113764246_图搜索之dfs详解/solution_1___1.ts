// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
/**
 ** 笔记：图搜索之 DFS 详解
 ** 方案：方案1（递归 DFS，记录发现/结束时间与边分类）
 ** 来源：python 参考忠实移植
 */

function dfs(
  graph: number[][],
  start: number,
): [number[], number[], Record<string, string>, number[]] {
  // 定义函数/方法 dfs
  const n = graph.length; // 把 graph.长度 存入 元素个数
  const status: string[] = new Array(n).fill('UNDISCOVERED');
  const dTime: number[] = new Array(n).fill(0); // 把 new Array(元素个数).fill(0); 写入 const dTime: number[]
  const fTime: number[] = new Array(n).fill(0); // 把 new Array(元素个数).fill(0); 写入 const fTime: number[]
  const parent: number[] = new Array(n).fill(-1); // 把 new Array(元素个数).fill( 减 1); 写入 const parent: number[]
  const edges: Record<string, string> = {}; // 把 {}; 写入 const edges: Record<string, string>
  let clock = 0; // 把 0 存入 clock
  const visit = (v: number): void => {
    clock++; // clock 加一
    dTime[v] = clock; // 把 clock; 写入 dTime[v]
    status[v] = 'DISCOVERED'; // 把 「DISCOVERED」; 写入 status[v]
    for (const u of graph[v]) {
      // for (const 节点 u of graph[值]) {
      if (status[u] === 'UNDISCOVERED') {
        // 若 status[节点 u] 全等于 「UNDISCOVERED」
        edges[`${v}, ${u}`] = 'TREE';
        parent[u] = v; // 把 值; 写入 parent[u]
        visit(u); // visit(节点 u);
      } else if (status[u] === 'DISCOVERED') {
        // 否则，若 status[节点 u] 全等于 「DISCOVERED」
        edges[`${v}, ${u}`] = 'BACKWARD';
      } else {
        // 否则
        edges[`${v}, ${u}`] = dTime[v] < dTime[u] ? 'FORWARD' : 'CROSS';
      }
    }
    clock++; // clock 加一
    fTime[v] = clock; // 把 clock; 写入 fTime[v]
    status[v] = 'VISITED'; // 把 「VISITED」; 写入 status[v]
  };
  visit(start); // visit(起点);
  return [dTime, fTime, edges, parent]; // 返回 [dTime, fTime, 边集, parent]
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const graph: number[][] = [[1, 5], [2], [], [4], [5, 6], [1, 6], []];
  const cases: { start: number; wantD: number[]; wantP: number[] }[] = [
    { start: 0, wantD: [1, 2, 3, 0, 0, 6, 7], wantP: [-1, 0, 1, -1, -1, 0, 5] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const [gotD, , , gotP] = dfs(graph, c.start); // 把 dfs(graph, 字符.起点); 写入 const [gotD, , , gotP]
    if (!eqArr(gotD, c.wantD) || !eqArr(gotP, c.wantP)) {
      // 若 取反 eqArr(gotD, 字符.wantD) 或 取反 eqArr(gotP, 字符.wantP
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL start',
        c.start,
        'want',
        JSON.stringify(c.wantD),
        JSON.stringify(c.wantP),
        'got',
        JSON.stringify(gotD),
        JSON.stringify(gotP),
      ); // 「got」, JSON.stringify(gotD), JSON.stringify(gotP));
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
