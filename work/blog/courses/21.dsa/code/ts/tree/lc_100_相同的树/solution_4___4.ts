// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134622591

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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  // 定义判定函数 isSameTree
  if (!p && !q) return true; // 若 取反 节点 且 取反 节点，直接返回 true
  if (p!.val !== q!.val) return false; // 若 节点取反 .值 不等于 节点取反 .值，直接返回 false
  const q1: (TreeNode | null)[] = [p]; // 把 [节点]; 写入 const q1: (TreeNode | null)[]
  const q2: (TreeNode | null)[] = [q]; // 把 [节点]; 写入 const q2: (TreeNode | null)[]
  while (q1.length && q2.length) {
    // 循环，直到不满足「q1.长度 且 q2.长度」
    const pTop = q1.shift()!; // 把 q1.shift()取反 存入 pTop
    const qTop = q2.shift()!; // 把 q2.shift()取反 存入 qTop
    if (pTop.val !== qTop.val) return false; // 若 pTop.值 不等于 qTop.值，直接返回 false
    const pL = pTop.left,
      pR = pTop.right,
      qL = qTop.left,
      qR = qTop.right;
    if ((pL && !qL) || (!pL && qL)) return false; // 若 (pL 且 取反 qL) 或 (取反 pL 且 qL)，直接返回 false
    if ((pR && !qR) || (!pR && qR)) return false; // 若 (pR 且 取反 qR) 或 (取反 pR 且 qR)，直接返回 false
    if (pL) q1.push(pL); // 若 pL) q1 追加 pL);
    if (pR) q1.push(pR); // 若 pR) q1 追加 pR);
    if (qL) q2.push(qL); // 若 qL) q2 追加 qL);
    if (qR) q2.push(qR); // 若 qR) q2 追加 qR);
  }
  return !q1.length && !q2.length; // 返回 取反 q1.长度 且 取反 q2.长度
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(isSameTree(null, null), true, 'isSameTree null'); // 断言校验
  assertEq(
    isSameTree(buildTree([1, 2, 3]), buildTree([1, 2, 3])),
    true,
    'isSameTree same',
  ); // 断言校验
  assertEq(
    isSameTree(buildTree([1, 2]), buildTree([1, null, 2])),
    false,
    'isSameTree diff',
  ); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
