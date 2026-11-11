/**
 ** LeetCode 133. 克隆图
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133986698
 ** 方案：方案6（BFS，visited 以节点对象为键）
 */

class Node {
  // 定义类型
  val: number; // 值: number;
  neighbors: Node[]; // neighbors: Node[];
  constructor(val: number = 0, neighbors?: Node[]) {
    // 把 0, neighbors?: Node[]) { 写入 constructor(val: number
    this.val = val; // 把 值; 写入 值
    this.neighbors = neighbors !== undefined ? neighbors : [];
  }
}

function cloneGraph(node: Node | null): Node | null {
  // 定义函数/方法 cloneGraph
  if (!node) return null; // 若 取反 节点，直接返回 null
  const visited = new Map<Node, Node>(); // 把 new Map 小于 Node, Node 超过 () 存入 已访问集合
  visited.set(node, new Node(node.val)); // 已访问集合.set(节点, new Node(节点.值));
  const q: Node[] = [node]; // 把 [节点]; 写入 const q: Node[]
  while (q.length) {
    // 循环，直到不满足「节点.长度」
    const n = q.shift()!; // 把 节点.shift()取反 存入 元素个数
    for (const ne of n.neighbors) {
      // for (const ne of 元素个数.neighbors) {
      if (!visited.has(ne)) {
        // 若 取反 已访问集合.has(ne
        q.push(ne); // 把 ne 压入栈/数组尾部
        visited.set(ne, new Node(ne.val)); // 已访问集合.set(ne, new Node(ne.值));
      }
      visited.get(n)!.neighbors.push(visited.get(ne)!); // 把 已访问集合 查找 ne 压入栈/数组尾部
    }
  }
  return visited.get(node)!; // 返回 已访问集合 查找 节点)取反
}

function buildGraph(adj: number[][]): Node {
  // 定义函数/方法 buildGraph
  const nodes = new Map<number, Node>(); // 把 new Map 小于 number, Node 超过 () 存入 nodes
  for (let i = 1; i <= adj.length; i++) nodes.set(i, new Node(i)); // 让 下标 i 从 1 开始计数，下标 i 不超过 邻接表.长度 就继续
  let idx = 1; // 把 1 存入 idx
  for (const nbrs of adj) {
    // for (const nbrs of 邻接表) {
    for (const nb of nbrs) nodes.get(idx)!.neighbors.push(nodes.get(nb)!); // 把 nodes 查找 nb 压入栈/数组尾部
    idx++; // idx 加一
  }
  return nodes.get(1)!; // 返回 nodes 查找 1)取反
}

function signature(node: Node): Record<number, number[]> {
  // 定义函数/方法 signature
  const vis: Record<number, number[]> = {}; // 把 {}; 写入 const vis: Record<number, number[]>
  function dfs(n: Node) {
    // 定义函数/方法 dfs
    if (n.val in vis) return; // 若 元素个数.值 in vis) return;
    vis[n.val] = n.neighbors.map((x) => x.val).sort((a, b) => a - b);
    for (const x of n.neighbors) dfs(x); // for (const x of 元素个数.neighbors) dfs(x);
  }
  dfs(node); // dfs(节点);
  return vis; // 返回 vis
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const root = buildGraph([
    [2, 4],
    [1, 3],
    [2, 4],
    [1, 3],
  ]); // ]);
  const cloned = cloneGraph(root); // 把 cloneGraph(根节点) 存入 cloned
  if (!cloned) throw new Error('cloneGraph returned null'); // 若 取反 cloned) throw new Error(「cloneGraph returned null」);
  if (cloned === root) throw new Error('not a deep copy (same object)');
  const sig = signature(cloned); // 把 signature(cloned) 存入 sig
  const expected: Record<number, number[]> = {
    // 把 { 写入 const expected: Record<number, number[]>
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3],
  };
  for (const k of [1, 2, 3, 4]) {
    // for (const 下标 k of [1, 2, 3, 4]) {
    const a = sig[k]; // 把 sig[下标 k] 存入 数组
    const b = expected[k]; // 把 expected[下标 k] 存入 b
    if (!a || a.length !== b.length || a.some((v, i) => v !== b[i]))
      throw new Error('signature mismatch at ' + k); // throw new Error(「signature mismatch at 」 加 下标 k);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
