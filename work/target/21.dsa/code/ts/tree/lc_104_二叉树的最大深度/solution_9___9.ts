// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631

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

function maxDepth(root: TreeNode | null): number {
  // 定义函数/方法 maxDepth
  if (!root) return 0; // 若 取反 根节点，直接返回 0
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right)); // 返回 1 加 Math.取较大值 maxDepth(根节点.左边界), maxDepth(根节点.右边界))
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(maxDepth(null), 0, 'null'); // 断言校验
  assertEq(maxDepth(buildTree([3, 9, 20, null, null, 15, 7])), 3, 'depth3'); // 断言校验
  assertEq(maxDepth(buildTree([1, 2, 3, 4, 5])), 3, 'depth35'); // 断言校验
  assertEq(maxDepth(buildTree([1, null, 2, null, 3])), 3, 'depthChain3'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
