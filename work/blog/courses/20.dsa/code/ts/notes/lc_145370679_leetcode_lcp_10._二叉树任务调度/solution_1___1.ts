// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — TS 版（方案1：深度优先-贪心）

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

// dfs 返回 [子树总耗时, 两台机器并行可节省的耗时]
function dfs(root: TreeNode | null): number[] {
  if (root === null) return [0.0, 0.0]; // 空子树：总耗时 0，节省 0
  const [a, b] = dfs(root.left); // a: 左子树总耗时, b: 左子树已节省
  const [c, d] = dfs(root.right); // c: 右子树总耗时, d: 右子树已节省
  let saved: number;
  if ((c - 2 * d <= a && a <= c) || (a - 2 * b <= c && c <= a)) {
    // 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
    saved = (a + c) / 2.0; // 浮点除法：总和为奇数时会出现 0.5
  } else if (a - 2 * b > c) {
    // 左子树串行段太长：右子树整体塞进左边空闲的那台机器
    saved = b + c;
  } else {
    // 右子树占主导：左子树整体塞进右边空闲的那台机器
    saved = a + d;
  }
  return [a + c + root.val, saved]; // 加上当前节点自身的执行时间
}

function minimalExecutionTime(root: TreeNode | null): number {
  // 答案 = 子树总和 - 并行节省
  const [total, saved] = dfs(root);
  return total - saved;
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
