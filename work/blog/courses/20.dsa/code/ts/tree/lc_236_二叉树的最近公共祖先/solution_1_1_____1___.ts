// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083302
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class TreeNode {
    // 定义类型
    val: number;
    left: TreeNode | null;
    right: TreeNode | null; // 值: number; 左边界: TreeNode 按位或 null; 右边界: TreeNode 按位或 null;
    constructor(
      val: number,
      left: TreeNode | null = null,
      right: TreeNode | null = null,
    ) {
      this.val = val;
      this.left = left;
      this.right = right; // 把 值; this.左边界 赋值为 左边界; this.右边界 赋值为 右边界; 写入 值
    }
  }
  function lowestCommonAncestor(
    root: TreeNode | null,
    p: TreeNode,
    q: TreeNode,
  ): TreeNode | null {
    // 定义函数/方法 lowestCommonAncestor
    if (root === null || root === p || root === q) return root; // 若 根节点 全等于 null 或 根节点 全等于 节点 或 根节点 全等于 节点，直接返回 根节点
    const left = lowestCommonAncestor(root.left, p, q); // 把 lowestCommonAncestor(根节点.左边界, 节点, 节点) 存入 左边界
    const right = lowestCommonAncestor(root.right, p, q); // 把 lowestCommonAncestor(根节点.右边界, 节点, 节点) 存入 右边界
    if (left && right) return root; // 若 左边界 且 右边界，直接返回 根节点
    return left ? left : right; // 返回 左边界 ? 左边界 : 右边界
  }
  function find(root: TreeNode | null, val: number): TreeNode | null {
    // 定义函数/方法 find
    if (root === null) return null; // 若 根节点 全等于 null，直接返回 null
    if (root.val === val) return root; // 若 根节点.值 全等于 值，直接返回 根节点
    return find(root.left, val) || find(root.right, val); // 返回 find(根节点.左边界, 值) 或 find(根节点.右边界, 值)
  }
  function build(): TreeNode {
    // 定义函数/方法 build
    const root = new TreeNode(3); // 把 new TreeNode(3) 存入 根节点
    root.left = new TreeNode(5); // 把 new TreeNode(5); 写入 左边界
    root.right = new TreeNode(1); // 把 new TreeNode(1); 写入 右边界
    root.left.left = new TreeNode(6); // 把 new TreeNode(6); 写入 左边界
    root.left.right = new TreeNode(2); // 把 new TreeNode(2); 写入 右边界
    root.right.left = new TreeNode(0); // 把 new TreeNode(0); 写入 左边界
    root.right.right = new TreeNode(8); // 把 new TreeNode(8); 写入 右边界
    root.left.right.left = new TreeNode(7); // 把 new TreeNode(7); 写入 左边界
    root.left.right.right = new TreeNode(4); // 把 new TreeNode(4); 写入 右边界
    return root; // 返回 根节点
  }
  const cases: [number, number, number][] = [
    [5, 1, 3],
    [5, 4, 5],
    [6, 4, 5],
  ];
  let fail = false; // 把 false 存入 fail
  for (const [pv, qv, want] of cases) {
    // for (const [pv, qv, want] of cases) {
    const root = build(); // 把 build() 存入 根节点
    const p = find(root, pv)!; // 把 find(根节点, pv)取反 存入 节点
    const q = find(root, qv)!; // 把 find(根节点, qv)取反 存入 节点
    const lca = lowestCommonAncestor(root, p, q); // 把 lowestCommonAncestor(根节点, 节点, 节点) 存入 lca
    const got = lca ? lca.val : -1; // 把 lca ? lca.值 : 减 1 存入 got
    if (got !== want) {
      fail = true;
      console.log('FAIL (' + pv + ',' + qv + ') got ' + got + ' want ' + want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
