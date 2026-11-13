// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130836270
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class TreeNode {
    // 定义类型
    val: number; // 值: number;
    left: TreeNode | null; // 左边界: TreeNode 按位或 null;
    right: TreeNode | null; // 右边界: TreeNode 按位或 null;
    constructor(v: number) {
      this.val = v;
      this.left = null;
      this.right = null;
    } // 把 值; this.左边界 赋值为 null; this.右边界 赋值为 null; } 写入 值
  }

  function buildTree(vals: (number | null)[]): TreeNode | null {
    // 定义函数/方法 buildTree
    if (vals.length === 0 || vals[0] === null) return null; // 若 vals.长度 全等于 0 或 vals[0] 全等于 null，直接返回 null
    const root = new TreeNode(vals[0]); // 把 new TreeNode(vals[0]) 存入 根节点
    const q: TreeNode[] = [root]; // 把 [根节点]; 写入 const q: TreeNode[]
    let i = 1; // 把 1 存入 下标 i
    while (q.length > 0 && i < vals.length) {
      // 循环，直到不满足「节点.长度 超过 0 且 下标 i 小于 vals.长度」
      const node = q.shift() as TreeNode; // 把 节点.shift() as TreeNode 存入 节点
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

  function minDepth(root: TreeNode | null): number {
    // 定义函数/方法 minDepth
    if (!root) return 0; // 若 取反 根节点，直接返回 0
    const q: [TreeNode, number][] = [[root, 1]]; // 队列传递根节点和层级
    while (q.length) {
      // 循环，直到不满足「节点.长度」
      const [n, l] = q.shift() as [TreeNode, number]; // 取出队首元素和层级
      if (!n.left && !n.right) return l; // 遇到叶子节点直接返回层级
      if (n.left) q.push([n.left, l + 1]); // 若 元素个数.左边界) 节点 追加 [元素个数.左边界, 左指针 加 1]);
      if (n.right) q.push([n.right, l + 1]); // 若 元素个数.右边界) 节点 追加 [元素个数.右边界, 左指针 加 1]);
    }
    return 0; // 返回 0
  }

  const cases: { in: (number | null)[]; want: number }[] = [
    { in: [3, 9, 20, null, null, 15, 7], want: 2 },
    { in: [2, null, 3, null, 4, null, 5, null, 6], want: 5 },
    { in: [], want: 0 },
    { in: [1], want: 1 },
    { in: [1, 2], want: 2 },
    { in: [1, 2, 3, 4, 5], want: 2 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = minDepth(buildTree(c.in)); // 把 minDepth(buildTree(字符.in)) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL minDepth(%o)=%d want %d', c.in, got, c.want); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
