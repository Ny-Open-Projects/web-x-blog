// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function bfs(graph: number[][], start: number): [number[], number[]] {
  // 定义函数/方法 bfs
  const n = graph.length; // 把 graph.长度 存入 元素个数
  const status: string[] = new Array(n).fill('UNDISCOVERED');
  const parent: number[] = new Array(n).fill(-1); // 把 new Array(元素个数).fill( 减 1); 写入 const parent: number[]
  const order: number[] = []; // 把 []; 写入 const order: number[]
  const q: number[] = [start]; // 把 [起点]; 写入 const q: number[]
  status[start] = 'DISCOVERED'; // 把 'DISCOVERED'; 写入 status[start]
  while (q.length) {
    // 循环，直到不满足「节点.长度」
    const v = q.shift()!; // 把 节点.shift()取反 存入 值
    order.push(v); // 把 值 压入栈/数组尾部
    for (const u of graph[v]) {
      // for (const 节点 u of graph[值]) {
      if (status[u] === 'UNDISCOVERED') {
        status[u] = 'DISCOVERED';
        parent[u] = v;
        q.push(u);
      }
    }
    status[v] = 'VISITED'; // 把 'VISITED'; 写入 status[v]
  }
  return [order, parent]; // 返回 [order, parent]
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const graph = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]; // 把 [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]] 存入 graph
  const [order, parent] = bfs(graph, 0); // 把 bfs(graph, 0); 写入 const [order, parent]
  assertEq(order, [0, 1, 2, 3, 4, 5], 'order'); // 断言校验
  assertEq(parent, [-1, 0, 0, 1, 1, 2], 'parent'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
