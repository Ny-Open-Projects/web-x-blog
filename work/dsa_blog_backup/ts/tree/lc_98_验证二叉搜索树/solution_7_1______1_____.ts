// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class TreeNode {
    // 定义类型
    val: number; // 值: number;
    left: TreeNode | null; // 左边界: TreeNode 按位或 null;
    right: TreeNode | null; // 右边界: TreeNode 按位或 null;
    constructor(
      val?: number,
      left: TreeNode | null = null,
      right: TreeNode | null = null,
    ) {
      this.val = val === undefined ? 0 : val; // 把 (值 全等于 undefined ? 0 : 值); 写入 值
      this.left = left; // 把 左边界; 写入 左边界
      this.right = right; // 把 右边界; 写入 右边界
    }
  }
  function buildTree(vals: (number | null)[]): TreeNode | null {
    // 定义函数/方法 buildTree
    if (vals.length === 0) return null; // 若 vals.长度 全等于 0，直接返回 null
    const root = new TreeNode(vals[0] as number); // 把 new TreeNode(vals[0] as number) 存入 根节点
    const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
    let i = 1; // 把 1 存入 下标 i
    while (i < vals.length) {
      // 循环，直到不满足「下标 i 小于 vals.长度」
      const node = q.shift() as TreeNode; // 把 节点.shift() as TreeNode 存入 节点
      if (i < vals.length && vals[i] !== null && vals[i] !== undefined) {
        node.left = new TreeNode(vals[i] as number); // 把 new TreeNode(vals[下标 i] as number); 写入 左边界
        q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
      }
      i++; // 下标 i 加一
      if (i < vals.length && vals[i] !== null && vals[i] !== undefined) {
        node.right = new TreeNode(vals[i] as number); // 把 new TreeNode(vals[下标 i] as number); 写入 右边界
        q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }
  function isValidBST(root: TreeNode | null): boolean {
    // 定义判定函数 isValidBST
    function dfs(
      node: TreeNode | null,
      low: number | null,
      high: number | null,
    ): boolean {
      // 定义函数/方法 dfs
      if (!node) return true; // 若 取反 节点，直接返回 true
      if (
        (low !== null && node.val <= low) ||
        (high !== null && node.val >= high)
      )
        return false;
      return dfs(node.left, low, node.val) && dfs(node.right, node.val, high); // 返回 dfs(节点.左边界, low, 节点.值) 且 dfs(节点.右边界, 节点.值, high)
    }
    return dfs(root, null, null); // 返回 dfs(根节点, null, null)
  }
  const cases: { in: (number | null)[]; want: boolean }[] = [
    { in: [2, 1, 3], want: true },
    { in: [5, 1, 4, null, null, 3, 6], want: false },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = isValidBST(buildTree(c.in)); // 把 isValidBST(buildTree(字符.in)) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c.in, 'got', got, 'want', c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
