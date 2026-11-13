// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145084192

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
function buildTree(vals: (number | null)[]): TreeNode | null {
  // 定义函数/方法 buildTree
  if (vals.length === 0 || vals[0] === null) return null; // 若 vals.长度 全等于 0 或 vals[0] 全等于 null，直接返回 null
  const root = new TreeNode(vals[0] as number); // 把 new TreeNode(vals[0] as number) 存入 根节点
  const q: (TreeNode | null)[] = [root];
  let i = 1; // 把 [根节点]; let 下标 i 赋值为 1; 写入 const q: (TreeNode | null)[]
  while (i < vals.length) {
    // 循环，直到不满足「下标 i 小于 vals.长度」
    const node = q.shift() as TreeNode; // 把 节点.shift() as TreeNode 存入 节点
    if (i < vals.length && vals[i] !== null) {
      node.left = new TreeNode(vals[i] as number);
      q.push(node.left);
    }
    i++; // 下标 i 加一
    if (i < vals.length && vals[i] !== null) {
      node.right = new TreeNode(vals[i] as number);
      q.push(node.right);
    }
    i++; // 下标 i 加一
  }
  return root; // 返回 根节点
}

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function sumOfLeftLeaves(root: TreeNode | null): number {
  // 定义函数/方法 sumOfLeftLeaves
  let leftSum = 0; // 把 0 存入 leftSum
  function travese(node: TreeNode | null): void {
    // 定义函数/方法 travese
    if (!node) return; // 若 取反 节点) return;
    const left = node.left; // 把 节点.左边界 存入 左边界
    if (left && !left.left && !left.right) leftSum += left.val; // 若 左边界 且 取反 左边界.左边界 且 取反 左边界.右边界) leftSum 累加 左边界.值;
    travese(node.left); // travese(节点.左边界);
    travese(node.right); // travese(节点.右边界);
  }
  travese(root); // travese(根节点);
  return leftSum; // 返回 leftSum
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    sumOfLeftLeaves(buildTree([3, 9, 20, null, null, 15, 7])),
    24,
    'sumLeftLeaves',
  ); // 断言校验
  assertEq(sumOfLeftLeaves(null), 0, 'null'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
