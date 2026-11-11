// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134625776
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
  function toList(root: TreeNode | null): (number | null)[] {
    // 定义函数/方法 toList
    if (!root) return []; // 若 取反 根节点，直接返回 []
    const res: (number | null)[] = []; // 把 []; 写入 const res: (number | null)[]
    const q: (TreeNode | null)[] = [root]; // 把 [根节点]; 写入 const q: (TreeNode | null)[]
    while (q.length) {
      // 循环，直到不满足「节点.长度」
      const node = q.shift() as TreeNode | null; // 把 节点.shift() as TreeNode 按位或 null 存入 节点
      if (node) {
        res.push(node.val);
        q.push(node.left);
        q.push(node.right);
      } // 若 节点) { 结果 追加 节点.值); 节点 追加 节点.左边界); 节点 追加 节点.右边界); }
      else res.push(null); // 否则
    }
    while (res.length && res[res.length - 1] === null) res.pop(); // 循环，直到不满足「结果.长度 且 结果[结果.长度 减 1] 全等于 null) 结果 弹出 );」
    return res; // 返回 结果
  }
  function invertTree(root: TreeNode | null): any {
    if (!root) return {}; // 定义函数/方法 invertTree

    const stack: (TreeNode | null)[] = [root]; // 把 [根节点]; 写入 const stack: (TreeNode | null)[]
    while (stack.length) {
      // 循环，直到不满足「栈.长度」
      const node = stack.pop() as TreeNode; // 把 栈 弹出 ) as TreeNode 存入 节点
      const tmp = node.left;
      node.left = node.right;
      node.right = tmp; // 把 节点.左边界; 节点.左边界 赋值为 节点.右边界; 节点.右边界 赋值为 临时变量 存入 临时变量
      if (node.left) stack.push(node.left); // 若 节点.左边界) 栈 追加 节点.左边界);
      if (node.right) stack.push(node.right); // 若 节点.右边界) 栈 追加 节点.右边界);
    }
    return root; // 返回 根节点
  }
  let fail = false; // 把 false 存入 fail
  const gotNull = invertTree(null); // 把 invertTree(null) 存入 gotNull
  if (JSON.stringify(gotNull) !== '{}') {
    fail = true;
    console.log(
      'FAIL invertTree(null)=' + JSON.stringify(gotNull) + ' want {}',
    );
  }
  const real = buildTree([4, 2, 7, 1, 3, 6, 9]); // 把 buildTree([4,2,7,1,3,6,9]) 存入 real
  const got = toList(invertTree(real)); // 把 toList(invertTree(real)) 存入 got
  if (JSON.stringify(got) !== JSON.stringify([4, 7, 2, 9, 6, 3, 1])) {
    fail = true;
    console.log(
      'FAIL invertTree([4,2,7,1,3,6,9])=' +
        JSON.stringify(got) +
        ' want [4,7,2,9,6,3,1]',
    );
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
