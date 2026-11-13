// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145084192

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
    this.val = val;
    this.left = left;
    this.right = right; // 把 值; this.左边界 赋值为 左边界; this.右边界 赋值为 右边界; 写入 值
  }
}
function buildTree(vals: (number | null)[]): TreeNode | null {
  // 定义函数/方法 buildTree
  if (vals.length === 0 || vals[0] === null) return null; // 若 vals.长度 全等于 0 或 vals[0] 全等于 null，直接返回 null
  const root = new TreeNode(vals[0] as number); // 把 new TreeNode(vals[0] as number) 存入 根节点
  const q: (TreeNode | null)[] = [root]; // 把 [根节点]; 写入 const q: (TreeNode | null)[]
  let i = 1; // 把 1 存入 下标 i
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
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e)
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
}

function isLeafNode(node: TreeNode | null): boolean {
  // 定义判定函数 isLeafNode
  return node !== null && node.left === null && node.right === null; // 返回 节点 不等于 null 且 节点.左边界 全等于 null 且 节点.右边界 全等于 null
}
function sumOfLeftLeaves(root: TreeNode | null): number {
  // 定义函数/方法 sumOfLeftLeaves
  if (!root) return 0; // 若 取反 根节点，直接返回 0
  let total = 0; // 把 0 存入 总和
  const stack: TreeNode[] = [root]; // 把 [根节点]; 写入 const stack: TreeNode[]
  while (stack.length) {
    // 循环，直到不满足「栈.长度」
    const node = stack.pop()!; // 把 栈 弹出 )取反 存入 节点
    if (node.left) {
      // 若 节点.左边界
      if (isLeafNode(node.left))
        total += node.left.val; // 若 isLeafNode(节点.左边界)) 总和 累加 节点.左边界.值;
      else stack.push(node.left); // 否则
    }
    if (node.right) stack.push(node.right); // 若 节点.右边界) 栈 追加 节点.右边界);
  }
  return total; // 返回 总和
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(
    sumOfLeftLeaves(buildTree([3, 9, 20, null, null, 15, 7])),
    24,
    'sumOfLeftLeaves',
  ); // 断言校验
  assertEq(sumOfLeftLeaves(null), 0, 'sumOfLeftLeaves null'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
