// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145053587

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

function kthSmallest(root: TreeNode | null, k: number): number {
  // 定义函数/方法 kthSmallest
  const stack: TreeNode[] = []; // 把 []; 写入 const stack: TreeNode[]
  let cur: TreeNode | null = root; // 把 根节点; 写入 let cur: TreeNode | null
  while (cur !== null || stack.length) {
    // 循环，直到不满足「当前值 不等于 null 或 栈.长度」
    while (cur !== null) {
      stack.push(cur);
      cur = cur.left;
    } // 循环，直到不满足「当前值 不等于 null) { 栈 追加 当前值); 当前值 赋值为 当前值.左边界; }」
    cur = stack.pop()!; // 把 栈 弹出 )取反 存入 当前值
    k -= 1; // 下标 k累减 1
    if (k === 0) break; // 若 下标 k 全等于 0) break;
    cur = cur.right; // 把 当前值.右边界 存入 当前值
  }
  return cur!.val; // 返回 当前值取反 .值
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const root = buildTree([3, 1, 4, null, 2]); // 把 buildTree([3, 1, 4, null, 2]) 存入 根节点
  assertEq(kthSmallest(root, 1), 1, 'kth 1'); // 断言校验
  assertEq(kthSmallest(root, 2), 2, 'kth 2'); // 断言校验
  assertEq(kthSmallest(root, 3), 3, 'kth 3'); // 断言校验
  assertEq(kthSmallest(root, 4), 4, 'kth 4'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
