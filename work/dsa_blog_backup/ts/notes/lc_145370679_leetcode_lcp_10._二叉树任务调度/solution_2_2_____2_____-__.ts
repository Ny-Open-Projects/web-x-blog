// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — TS 版（方案2：深度优先-优化）

class TreeNode {
  // 二叉树节点：val 为自身执行时间
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val: number) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function buildTree(vals: (number | null)[]): TreeNode | null {
  // 层序数组建树，null 表示空节点
  if (vals.length === 0) return null;
  const root = new TreeNode(vals[0] as number);
  const queue: TreeNode[] = [root]; // 队列里只放非空节点
  let i = 1;
  while (queue.length > 0 && i < vals.length) {
    const node = queue.shift() as TreeNode; // 出队一个父节点
    if (i < vals.length && vals[i] !== null) {
      // 左孩子
      node.left = new TreeNode(vals[i] as number);
      queue.push(node.left);
    }
    i++;
    if (i < vals.length && vals[i] !== null) {
      // 右孩子
      node.right = new TreeNode(vals[i] as number);
      queue.push(node.right);
    }
    i++;
  }
  return root;
}

// dfs 返回 [子树总耗时, 子树最小完成时间 maxExec]
function dfs(root: TreeNode | null): number[] {
  if (root === null) return [0.0, 0.0]; // 空子树
  const [leftSum, leftExec] = dfs(root.left); // 左子树的总耗时与最小完成时间
  const [rightSum, rightExec] = dfs(root.right);
  // 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
  // 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
  const parallel = (leftSum + rightSum) / 2.0; // 两台机器均摊左右子树总工作量（浮点）
  const maxExec = root.val + Math.max(Math.max(leftExec, rightExec), parallel);
  return [leftSum + rightSum + root.val, maxExec];
}

function minimalExecutionTime(root: TreeNode | null): number {
  // 答案 = 整棵树的最小完成时间
  return dfs(root)[1];
}

// 三个官方用例
const cases: { vals: (number | null)[]; want: number }[] = [
  { vals: [47, 74, 31], want: 121.0 },
  { vals: [15, 21, null, 24, null, 27, 26], want: 87.0 },
  { vals: [1, 3, 2, null, null, 4, 4], want: 7.5 },
];
let fail = false;
for (const tc of cases) {
  const got = minimalExecutionTime(buildTree(tc.vals));
  if (Math.abs(got - tc.want) >= 1e-6) {
    // 浮点比较用 1e-6 容差
    console.log('FAIL', tc.vals, 'got', got, 'want', tc.want); // 失败打印 FAIL
    fail = true;
  }
}
if (fail) process.exit(1); // 非零退出
console.log('PASS'); // 全部用例通过，输出 PASS
