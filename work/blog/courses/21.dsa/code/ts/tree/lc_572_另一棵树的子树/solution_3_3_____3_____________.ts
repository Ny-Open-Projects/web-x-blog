// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089820
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
  function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    // 定义判定函数 isSubtree
    if (!root) return false; // 若 取反 根节点，直接返回 false
    if (root.val === subRoot!.val && isSameTree(root, subRoot)) return true;
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot); // 返回 isSubtree(根节点.左边界, subRoot) 或 isSubtree(根节点.右边界, subRoot)
  }
  function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    // 定义判定函数 isSameTree
    if (!p && !q) return true; // 若 取反 节点 且 取反 节点，直接返回 true
    if (!p || !q) return false; // 若 取反 节点 或 取反 节点，直接返回 false
    if (p.val !== q.val) return false; // 若 节点.值 不等于 节点.值，直接返回 false
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right); // 返回 isSameTree(节点.左边界, 节点.左边界) 且 isSameTree(节点.右边界, 节点.右边界)
  }
  const cases = [
    { a: [3, 4, 5, 1, 2], b: [4, 1, 2], want: true },
    {
      a: [3, 4, 5, 1, 2, null, null, null, null, 0],
      b: [4, 1, 2],
      want: false,
    },
    { a: [], b: [], want: false },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = isSubtree(buildTree(c.a), buildTree(c.b)); // 把 isSubtree(buildTree(字符.数组), buildTree(字符.b)) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
