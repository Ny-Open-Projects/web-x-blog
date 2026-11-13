// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
/**
 ** LeetCode 112. 路径总和
 ** 忠实翻译自 python/tree/lc_112_路径总和/solution_11_1_____1________DFS_.py
 ** 运行即自检：失败抛错（非 0 退出），通过打印 PASS
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

// 递归：叶子节点判定 val == targetSum，否则向左右子树传递剩余目标值
function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  // 定义函数/方法 hasPathSum
  if (root === null) return false; // 若 根节点 全等于 null，直接返回 false
  if (root.left === null && root.right === null) return root.val === targetSum;
  return (
    hasPathSum(root.left, targetSum - root.val) ||
    hasPathSum(root.right, targetSum - root.val)
  );
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
    { arr: DEMO, target: 22, want: true }, // normal: 5+4+11+2
    { arr: DEMO, target: 20, want: false }, // normal: 20 非完整根到叶路径
    { arr: DEMO, target: 26, want: true }, // normal: 5+8+13
    { arr: [1], target: 1, want: true }, // boundary: 单节点命中
    { arr: [1], target: 2, want: false }, // boundary: 单节点不命中
    { arr: [], target: 0, want: false }, // boundary: 空树
    { arr: [1, 2], target: 3, want: true }, // boundary: 单层两节点 1+2
    { arr: [1, 2], target: 1, want: false }, // boundary: 根非叶，1 不是完整路径和
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
