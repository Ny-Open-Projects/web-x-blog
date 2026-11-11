// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134623793
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class TreeNode {
    // 定义类型
    val: number; // 值: number;
    left: TreeNode | null; // 左边界: TreeNode 按位或 null;
    right: TreeNode | null; // 右边界: TreeNode 按位或 null;
    constructor(
      v: number,
      left: TreeNode | null = null,
      right: TreeNode | null = null,
    ) {
      this.val = v;
      this.left = left;
      this.right = right; // 把 值; this.左边界 赋值为 左边界; this.右边界 赋值为 右边界; 写入 值
    }
  }
  function buildTree(a: (number | null)[]): TreeNode | null {
    // 定义函数/方法 buildTree
    if (a.length === 0 || a[0] === null) return null; // 若 数组.长度 全等于 0 或 数组[0] 全等于 null，直接返回 null
    const root = new TreeNode(a[0] as number); // 把 new TreeNode(数组[0] as number) 存入 根节点
    const q: (TreeNode | null)[] = [root]; // 把 [根节点]; 写入 const q: (TreeNode | null)[]
    let i = 1; // 把 1 存入 下标 i
    while (q.length && i < a.length) {
      // 循环，直到不满足「节点.长度 且 下标 i 小于 数组.长度」
      const n = q.shift() as TreeNode; // 把 节点.shift() as TreeNode 存入 元素个数
      if (a[i] !== null) {
        n.left = new TreeNode(a[i] as number);
        q.push(n.left);
      }
      i++; // 下标 i 加一
      if (i < a.length && a[i] !== null) {
        n.right = new TreeNode(a[i] as number);
        q.push(n.right);
      }
      i++; // 下标 i 加一
    }
    return root; // 返回 根节点
  }
  function isSymmetric(root: TreeNode | null): boolean {
    // 定义判定函数 isSymmetric
    if (!root) return true; // 若 取反 根节点，直接返回 true
    function isMirror(l: TreeNode | null, r: TreeNode | null): boolean {
      // 定义判定函数 isMirror
      if (!l && !r) return true; // 若 取反 左指针 且 取反 右指针，直接返回 true
      if (!l || !r) return false; // 若 取反 左指针 或 取反 右指针，直接返回 false
      return (
        l.val === r.val &&
        isMirror(l.left, r.right) &&
        isMirror(r.left, l.right)
      );
    }
    return isMirror(root.left, root.right); // 返回 isMirror(根节点.左边界, 根节点.右边界)
  }
  const cases: [any, boolean][] = [
    [null, true],
    [[1, 2, 2, 3, 4, 4, 3], true],
    [[1, 2, 2, null, 3, null, 3], false],
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const inp = c[0]; // 把 字符[0] 存入 inp
    const want = c[1]; // 把 字符[1] 存入 want
    const root = inp === null ? null : buildTree(inp as (number | null)[]);
    const got = isSymmetric(root); // 把 isSymmetric(根节点) 存入 got
    if (got !== want) {
      fail = true;
      console.log(
        'FAIL isSymmetric(' +
          JSON.stringify(inp) +
          ')=' +
          got +
          ' want ' +
          want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
