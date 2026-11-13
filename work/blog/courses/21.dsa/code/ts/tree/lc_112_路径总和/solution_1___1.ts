// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
/**
 ** LeetCode 112. 路径总和
 ** 方案1：DFS 累加根到当前节点的和，到达叶子时与 targetSum 比较（对齐博客算法）。
 */

class TreeNode {
  // 定义类型
  val: number; // 值: number;
  left: TreeNode | null; // 左边界: TreeNode 按位或 null;
  right: TreeNode | null; // 右边界: TreeNode 按位或 null;
  constructor(
    val: number,
    left: TreeNode | null = null,
    right: TreeNode | null = null,
  ) {
    this.val = val; // 把 值; 写入 值
    this.left = left; // 把 左边界; 写入 左边界
    this.right = right; // 把 右边界; 写入 右边界
  }
}

// 按层序数组构建二叉树（null 表示空节点），如 [5,4,8,11,null,13,4,7,2,null,null,null,1]
function buildTree(arr: (number | null)[]): TreeNode | null {
  // 定义函数/方法 buildTree
  if (arr.length === 0 || arr[0] === null) return null; // 若 数组.长度 全等于 0 或 数组[0] 全等于 null，直接返回 null
  const root = new TreeNode(arr[0]); // 把 new TreeNode(数组[0]) 存入 根节点
  const queue: TreeNode[] = [root]; // 把 [根节点]; 写入 const queue: TreeNode[]
  let i = 1; // 把 1 存入 下标 i
  while (i < arr.length) {
    // 循环，直到不满足「下标 i 小于 数组.长度」
    const node = queue.shift()!; // 把 队列.shift()取反 存入 节点
    if (i < arr.length) {
      // 若 下标 i 小于 数组.长度
      const v = arr[i++]; // 把 数组[下标 i 加一 ] 存入 值
      if (v !== null) {
        // 若 值 不等于 null
        node.left = new TreeNode(v); // 把 new TreeNode(值); 写入 左边界
        queue.push(node.left); // 把 节点.左边界 压入栈/数组尾部
      }
    }
    if (i < arr.length) {
      // 若 下标 i 小于 数组.长度
      const v = arr[i++]; // 把 数组[下标 i 加一 ] 存入 值
      if (v !== null) {
        // 若 值 不等于 null
        node.right = new TreeNode(v); // 把 new TreeNode(值); 写入 右边界
        queue.push(node.right); // 把 节点.右边界 压入栈/数组尾部
      }
    }
  }
  return root; // 返回 根节点
}

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  // 定义函数/方法 hasPathSum
  if (root === null) return false; // 若 根节点 全等于 null，直接返回 false
  let res = false; // 把 false 存入 结果
  const dfs = (n: TreeNode, v: number): void => {
    if (n.left === null && n.right === null) {
      // 若 元素个数.左边界 全等于 null 且 元素个数.右边界 全等于 null
      if (v === targetSum) res = true; // 若 值 全等于 targetSum) 结果 赋值为 true;
      return; // return;
    }
    if (n.left !== null) dfs(n.left, v + n.left.val); // 若 元素个数.左边界 不等于 null) dfs(元素个数.左边界, 值 加 元素个数.左边界.值);
    if (n.right !== null) dfs(n.right, v + n.right.val); // 若 元素个数.右边界 不等于 null) dfs(元素个数.右边界, 值 加 元素个数.右边界.值);
  };
  dfs(root, root.val); // dfs(根节点, 根节点.值);
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const DEMO: (number | null)[] = [
    5,
    4,
    8,
    11,
    null,
    13,
    4,
    7,
    2,
    null,
    null,
    null,
    1,
  ];
  const cases: { arr: (number | null)[]; target: number; want: boolean }[] = [
    { arr: DEMO, target: 22, want: true }, // 5+4+11+2
    { arr: DEMO, target: 27, want: true }, // 5+4+11+7
    { arr: DEMO, target: 18, want: true }, // 5+8+4+1
    { arr: DEMO, target: 26, want: true }, // 5+8+13
    { arr: DEMO, target: 20, want: false }, // 20 非完整根到叶路径
    { arr: DEMO, target: 1, want: false },
    { arr: [1], target: 1, want: true }, // 单节点即叶子，命中
    { arr: [1], target: 2, want: false },
    { arr: [], target: 0, want: false }, // 空树
    { arr: [1, 2], target: 3, want: true }, // 1+2（2 是叶子）
    { arr: [1, 2], target: 1, want: false }, // 根非叶，1 不是完整路径和
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const root = buildTree(c.arr); // 把 buildTree(字符.数组) 存入 根节点
    const got = hasPathSum(root, c.target); // 把 hasPathSum(根节点, 字符.目标值) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        `FAIL hasPathSum(${JSON.stringify(c.arr)}, ${c.target})=${got} want ${c.want}`,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
