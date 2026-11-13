/**
 ** LeetCode 637. 二叉树的层平均值
 ** 方案：方案2（广度优先搜索）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145091296
 */

class TreeNode {
  // 定义类型
  val: number; // 值: number;
  left: TreeNode | null; // 左边界: TreeNode 按位或 null;
  right: TreeNode | null; // 右边界: TreeNode 按位或 null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val; // 把 (值 全等于 undefined ? 0 : 值); 写入 值
    this.left = left === undefined ? null : left; // 把 (左边界 全等于 undefined ? null : 左边界); 写入 左边界
    this.right = right === undefined ? null : right; // 把 (右边界 全等于 undefined ? null : 右边界); 写入 右边界
  }
}

function buildTree(vals: (number | null)[]): TreeNode | null {
  // 定义函数/方法 buildTree
  if (!vals.length || vals[0] === null) return null; // 若 取反 vals.长度 或 vals[0] 全等于 null，直接返回 null
  const root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]) 存入 根节点
  const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
  let i = 1; // 把 1 存入 下标 i
  while (i < vals.length) {
    // 循环，直到不满足「下标 i 小于 vals.长度」
    const node = q.shift()!; // 把 节点.shift()取反 存入 节点
    if (vals[i] !== null && vals[i] !== undefined) {
      node.left = new TreeNode(vals[i] as number);
      q.push(node.left);
    }
    i++; // 下标 i 加一
    if (i < vals.length) {
      // 若 下标 i 小于 vals.长度
      if (vals[i] !== null && vals[i] !== undefined) {
        node.right = new TreeNode(vals[i] as number);
        q.push(node.right);
      }
      i++; // 下标 i 加一
    }
  }
  return root; // 返回 根节点
}

function averageOfLevels(root: TreeNode | null): number[] {
  // 定义函数/方法 averageOfLevels
  const averages: number[] = []; // 把 []; 写入 const averages: number[]
  const queue: TreeNode[] = [root]; // 把 [根节点]; 写入 const queue: TreeNode[]
  while (queue.length > 0) {
    // 循环，直到不满足「队列.长度 超过 0」
    let total = 0; // 把 0 存入 总和
    const size = queue.length; // 把 队列.长度 存入 大小
    for (let i = 0; i < size; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
      const node = queue.shift()!; // 把 队列.shift()取反 存入 节点
      total += node.val; // 总和累加 节点.值
      if (node.left) queue.push(node.left); // 若 节点.左边界) 队列 追加 节点.左边界);
      if (node.right) queue.push(node.right); // 若 节点.右边界) 队列 追加 节点.右边界);
    }
    averages.push(total / size); // 把 总和 除以 大小 压入栈/数组尾部
  }
  return averages; // 返回 averages
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { vals: (number | null)[]; want: number[] }[] = [
    { vals: [3, 9, 20, 15, 7], want: [3, 14.5, 11] },
    { vals: [3, 9, 20, null, null, 15, 7], want: [3, 14.5, 11] },
    { vals: [1], want: [1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = averageOfLevels(buildTree(c.vals)); // 把 averageOfLevels(buildTree(字符.vals)) 存入 got
    let ok = got.length === c.want.length; // 把 got.长度 全等于 字符.want.长度 存入 ok
    for (let i = 0; i < got.length && ok; i++)
      if (Math.abs(got[i] - c.want[i]) > 1e-9) ok = false; // 让 下标 i 从 0 开始计数，下标 i 小于 got.长度 且 ok 就继续
    if (!ok) {
      // 若 取反 ok
      fail = true; // 把 true 存入 fail
      console.log(
        `FAIL averageOfLevels(${JSON.stringify(c.vals)})=${JSON.stringify(got)} want ${JSON.stringify(c.want)}`,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
