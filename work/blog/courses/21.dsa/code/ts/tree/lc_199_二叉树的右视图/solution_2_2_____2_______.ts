// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145030731
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class TreeNode {
    // 定义类型
    val: number; // 值: number;
    left: TreeNode | null; // 左边界: TreeNode 按位或 null;
    right: TreeNode | null; // 右边界: TreeNode 按位或 null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
      this.val = val === undefined ? 0 : val; // 把 值 全等于 undefined ? 0 : 值; 写入 值
      this.left = left === undefined ? null : left; // 把 左边界 全等于 undefined ? null : 左边界; 写入 左边界
      this.right = right === undefined ? null : right; // 把 右边界 全等于 undefined ? null : 右边界; 写入 右边界
    }
  }

  function buildTree(vals: (number | null)[]): TreeNode | null {
    // 定义函数/方法 buildTree
    if (vals.length === 0 || vals[0] === null) return null; // 若 vals.长度 全等于 0 或 vals[0] 全等于 null，直接返回 null
    const root = new TreeNode(vals[0]!); // 把 new TreeNode(vals[0]取反 ) 存入 根节点
    const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
    let i = 1; // 把 1 存入 下标 i
    while (i < vals.length) {
      // 循环，直到不满足「下标 i 小于 vals.长度」
      const node = q.shift()!; // 把 节点.shift()取反 存入 节点
      if (vals[i] !== null) {
        // 若 vals[下标 i] 不等于 null
        node.left = new TreeNode(vals[i]!); // 把 new TreeNode(vals[下标 i]取反 ); 写入 左边界
        q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
      }
      i++; // 下标 i 加一
      if (i < vals.length) {
        // 若 下标 i 小于 vals.长度
        if (vals[i] !== null) {
          // 若 vals[下标 i] 不等于 null
          node.right = new TreeNode(vals[i]!); // 把 new TreeNode(vals[下标 i]取反 ); 写入 右边界
          q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
        }
        i++; // 下标 i 加一
      }
    }
    return root; // 返回 根节点
  }

  function rightSideView(root: TreeNode | null): number[] {
    // 定义函数/方法 rightSideView
    if (root === null) return []; // 若 根节点 全等于 null，直接返回 []
    const result: number[] = []; // 把 []; 写入 const result: number[]
    const queue: TreeNode[] = [root]; // 把 [根节点]; 写入 const queue: TreeNode[]
    while (queue.length > 0) {
      // 循环，直到不满足「队列.长度 超过 0」
      const levelSize = queue.length; // 把 队列.长度 存入 levelSize
      for (let i = 0; i < levelSize; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 levelSize 就继续
        const node = queue.shift()!; // 把 队列.shift()取反 存入 节点
        if (i === levelSize - 1) result.push(node.val); // 若 下标 i 全等于 levelSize 减 1) 结果 追加 节点.值);
        if (node.left !== null) queue.push(node.left); // 若 节点.左边界 不等于 null) 队列 追加 节点.左边界);
        if (node.right !== null) queue.push(node.right); // 若 节点.右边界 不等于 null) 队列 追加 节点.右边界);
      }
    }
    return result; // 返回 结果
  }

  function eq(a: number[], b: number[]): boolean {
    // 定义函数/方法 eq
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { in: (number | null)[]; want: number[] }[] = [
    { in: [1, 2, 3, null, 5, null, 4], want: [1, 3, 4] },
    { in: [], want: [] },
    { in: [1], want: [1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = rightSideView(buildTree(c.in)); // 把 rightSideView(buildTree(字符.in)) 存入 got
    if (!eq(got, c.want)) {
      // 若 取反 eq(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL in=' +
          JSON.stringify(c.in) +
          ' got=' +
          JSON.stringify(got) +
          ' want=' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
