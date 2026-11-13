// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631

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
    this.val = val; // 把 值; 写入 值
    this.left = left; // 把 左边界; 写入 左边界
    this.right = right; // 把 右边界; 写入 右边界
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

function assertEq(actual: any, expected: any, msg: string = ''): void {
  // 定义函数/方法 assertEq
  const a = JSON.stringify(actual); // 把 JSON.stringify(actual) 存入 数组
  const e = JSON.stringify(expected); // 把 JSON.stringify(expected) 存入 e
  if (a !== e) {
    // 若 数组 不等于 e
    throw new Error(
      'ASSERT FAILED ' + msg + ' :: actual=' + a + ' expected=' + e,
    );
  }
}

function maxDepth(root: TreeNode | null): number {
  // 定义函数/方法 maxDepth
  let dep = 0; // 把 0 存入 dep
  function dfs(n: TreeNode | null, l: number): void {
    // 定义函数/方法 dfs
    if (!n) return; // 若 取反 元素个数) return;
    if (!n.left && !n.right) dep = Math.max(dep, l); // 若 取反 元素个数.左边界 且 取反 元素个数.右边界) dep 赋值为 Math.取较大值 dep, 左指针);
    dfs(n.left, l + 1); // dfs(元素个数.左边界, 左指针 加 1);
    dfs(n.right, l + 1); // dfs(元素个数.右边界, 左指针 加 1);
  }
  dfs(root, 1); // dfs(根节点, 1);
  return dep; // 返回 dep
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  assertEq(maxDepth(null), 0, 'maxDepth null'); // 断言校验
  assertEq(maxDepth(buildTree([1])), 1, 'maxDepth [1]'); // 断言校验
  assertEq(maxDepth(buildTree([3, 9, 20, null, null, 15, 7])), 3, 'maxDepth 3'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
