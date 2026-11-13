// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130877211
export function demo(): void {
  // 程序入口：跑内嵌自测用例
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
  function buildTree(nums: (number | null)[]): TreeNode | null {
    // 定义函数/方法 buildTree
    if (!nums || nums.length === 0 || nums[0] === null || nums[0] === undefined)
      return null;
    const root = new TreeNode(nums[0] as number); // 把 new TreeNode(数组[0] as number) 存入 根节点
    const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
    let i = 1; // 把 1 存入 下标 i
    while (q.length > 0 && i < nums.length) {
      // 循环，直到不满足「节点.长度 超过 0 且 下标 i 小于 数组.长度」
      const node = q.shift() as TreeNode; // 把 节点.shift() as TreeNode 存入 节点
      if (i < nums.length && nums[i] !== null && nums[i] !== undefined) {
        // 若 下标 i 小于 数组.长度 且 数组[下标 i] 不等于 null 且 数组[下标 i] 不等于 undefined
        node.left = new TreeNode(nums[i] as number); // 把 new TreeNode(数组[下标 i] as number); 写入 左边界
        q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
      }
      i++; // 下标 i 加一
      if (i < nums.length && nums[i] !== null && nums[i] !== undefined) {
        // 若 下标 i 小于 数组.长度 且 数组[下标 i] 不等于 null 且 数组[下标 i] 不等于 undefined
        node.right = new TreeNode(nums[i] as number); // 把 new TreeNode(数组[下标 i] as number); 写入 右边界
        q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }
  function levelOrder(root: TreeNode | null): number[][] {
    // 定义函数/方法 levelOrder
    if (!root) return []; // 若 取反 根节点，直接返回 []
    const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
    const res: number[][] = []; // 把 []; 写入 const res: number[][]
    while (q.length > 0) {
      // 循环，直到不满足「节点.长度 超过 0」
      const size = q.length; // 把 节点.长度 存入 大小
      const level: number[] = []; // 把 []; 写入 const level: number[]
      for (let i = 0; i < size; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 大小 就继续
        const node = q.shift() as TreeNode; // 把 节点.shift() as TreeNode 存入 节点
        level.push(node.val); // 把 节点.值 压入栈/数组尾部
        if (node.left) q.push(node.left); // 若 节点.左边界) 节点 追加 节点.左边界);
        if (node.right) q.push(node.right); // 若 节点.右边界) 节点 追加 节点.右边界);
      }
      res.push(level); // 把 level 压入栈/数组尾部
    }
    return res; // 返回 结果
  }
  function eq2d(a: number[][], b: number[][]): boolean {
    // 定义函数/方法 eq2d
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i].length !== b[i].length) return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
      for (let j = 0; j < a[i].length; j++)
        if (a[i][j] !== b[i][j]) return false; // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
    }
    return true; // 返回 true
  }
  const cases = [
    { t: [], want: [] },
    { t: [3, 9, 20, null, null, 15, 7], want: [[3], [9, 20], [15, 7]] },
    { t: [1], want: [[1]] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = levelOrder(buildTree(c.t)); // 把 levelOrder(buildTree(字符.另一字符串)) 存入 got
    if (!eq2d(got, c.want)) {
      fail = true;
      console.log('FAIL', c, 'got', JSON.stringify(got));
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
