// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130742026
/**
 ** LeetCode 144. 二叉树的前序遍历
 ** 方案：方案6（迭代，显式栈）
 ** 来源：python 参考忠实移植
 */

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
  if (!vals.length) return null; // 若 取反 vals.长度，直接返回 null
  const root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]) 存入 根节点
  const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
  let i = 1; // 把 1 存入 下标 i
  while (i < vals.length && q.length) {
    // 循环，直到不满足「下标 i 小于 vals.长度 且 节点.长度」
    const node = q.shift()!; // 把 节点.shift()取反 存入 节点
    if (i < vals.length && vals[i] !== null) {
      // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
      node.left = new TreeNode(vals[i] as number); // 把 new TreeNode(vals[下标 i] as number); 写入 左边界
      q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
    }
    i++; // 下标 i 加一
    if (i < vals.length && vals[i] !== null) {
      // 若 下标 i 小于 vals.长度 且 vals[下标 i] 不等于 null
      node.right = new TreeNode(vals[i] as number); // 把 new TreeNode(vals[下标 i] as number); 写入 右边界
      q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
    }
    i++; // 下标 i 加一
  }
  return root; // 返回 根节点
}

function preorderTraversal(root: TreeNode | null): number[] {
  // 定义函数/方法 preorderTraversal
  const res: number[] = []; // 把 []; 写入 const res: number[]
  const stack: TreeNode[] = []; // 把 []; 写入 const stack: TreeNode[]
  if (root) stack.push(root); // 若 根节点) 栈 追加 根节点);
  while (stack.length) {
    // 循环，直到不满足「栈.长度」
    const node = stack.pop()!; // 把 栈 弹出 )取反 存入 节点
    res.push(node.val); // 把 节点.值 压入栈/数组尾部
    if (node.right) stack.push(node.right); // 若 节点.右边界) 栈 追加 节点.右边界);
    if (node.left) stack.push(node.left); // 若 节点.左边界) 栈 追加 节点.左边界);
  }
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { in: (number | null)[]; want: number[] }[] = [
    { in: [1, null, 2, null, 3], want: [1, 2, 3] },
    { in: [1, 2, 3, null, null, 4, 5], want: [1, 2, 3, 4, 5] },
    { in: [], want: [] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = preorderTraversal(buildTree(c.in)); // 把 preorderTraversal(buildTree(字符.in)) 存入 got
    if (JSON.stringify(got) !== JSON.stringify(c.want)) {
      // 若 JSON.stringify(got) 不等于 JSON.stringify(字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL',
        JSON.stringify(c.in),
        'want',
        JSON.stringify(c.want),
        'got',
        JSON.stringify(got),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
