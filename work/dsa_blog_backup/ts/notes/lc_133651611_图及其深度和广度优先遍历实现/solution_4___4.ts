/**
 ** LeetCode 133651611. 图及其深度和广度优先遍历实现
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133651611
 */

class Graph {
  // 定义类型
  private adjList: Map<number, number[]>; // private adjList: Map 小于 number, number[] 超过 ;

  constructor() {
    // constructor() {
    this.adjList = new Map(); // 把 new Map(); 写入 this.adjList
  }

  addEdge(from: number, to: number): void {
    // addEdge(from: number, to: number): void {
    if (!this.adjList.has(from)) this.adjList.set(from, []); // 若 取反 this.adjList.has(from)) this.adjList.set(from, []);
    if (!this.adjList.has(to)) this.adjList.set(to, []); // 若 取反 this.adjList.has(to)) this.adjList.set(to, []);
    this.adjList.get(from)!.push(to); // 把 to 压入栈/数组尾部
    this.adjList.get(to)!.push(from); // 把 from 压入栈/数组尾部
  }

  dfs(start: number): number[] {
    // dfs(起点: number): number[] {
    const visited = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 已访问集合
    const result: number[] = []; // 把 []; 写入 const result: number[]
    this.dfsHelper(start, visited, result); // this.dfsHelper(起点, 已访问集合, 结果);
    return result; // 返回 结果
  }

  private dfsHelper(
    node: number,
    visited: Set<number>,
    result: number[],
  ): void {
    if (visited.has(node)) return; // 若 已访问集合.has(节点)) return;
    visited.add(node); // 已访问集合 追加 节点);
    result.push(node); // 把 节点 压入栈/数组尾部
    for (const neighbor of this.adjList.get(node) || []) {
      // for (const neighbor of this.adjList 查找 节点) 或 []) {
      this.dfsHelper(neighbor, visited, result); // this.dfsHelper(neighbor, 已访问集合, 结果);
    }
  }

  bfs(start: number): number[] {
    // bfs(起点: number): number[] {
    const visited = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 已访问集合
    const result: number[] = []; // 把 []; 写入 const result: number[]
    const queue: number[] = [start]; // 把 [起点]; 写入 const queue: number[]
    visited.add(start); // 已访问集合 追加 起点);

    while (queue.length > 0) {
      // 循环，直到不满足「队列.长度 超过 0」
      const node = queue.shift()!; // 把 队列.shift()取反 存入 节点
      result.push(node); // 把 节点 压入栈/数组尾部
      for (const neighbor of this.adjList.get(node) || []) {
        // for (const neighbor of this.adjList 查找 节点) 或 []) {
        if (!visited.has(neighbor)) {
          // 若 取反 已访问集合.has(neighbor
          visited.add(neighbor); // 已访问集合 追加 neighbor);
          queue.push(neighbor); // 把 neighbor 压入栈/数组尾部
        }
      }
    }
    return result; // 返回 结果
  }
}

function eq(a: number[], b: number[]): boolean {
  // 定义函数/方法 eq
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] !== b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // case 1: square graph 0-1-3-2-0
  const g1 = new Graph(); // 把 new Graph() 存入 g1
  g1.addEdge(0, 1); // g1.addEdge(0, 1);
  g1.addEdge(0, 2); // g1.addEdge(0, 2);
  g1.addEdge(1, 3); // g1.addEdge(1, 3);
  g1.addEdge(2, 3); // g1.addEdge(2, 3);
  if (!eq(g1.dfs(0), [0, 1, 3, 2])) throw new Error('FAILED case1 dfs(0)');
  if (!eq(g1.bfs(0), [0, 1, 2, 3])) throw new Error('FAILED case1 bfs(0)');

  // case 2: traversal from another start node
  if (!eq(g1.dfs(2), [2, 0, 1, 3])) throw new Error('FAILED case2 dfs(2)');
  if (!eq(g1.bfs(2), [2, 0, 3, 1])) throw new Error('FAILED case2 bfs(2)');

  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
