// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091772

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

function insertIntoBST(root: TreeNode | null, val: number): TreeNode {
  // 定义函数/方法 insertIntoBST
  if (root === null) return new TreeNode(val); // 若 根节点 全等于 null，直接返回 new TreeNode(值)
  let pos = root; // 把 根节点 存入 pos
  while (pos !== null) {
    // 循环，直到不满足「pos 不等于 null」
    if (val < pos.val) {
      // 若 值 小于 pos.值
      if (pos.left === null) {
        pos.left = new TreeNode(val);
        break;
      } // 若 pos.左边界 全等于 null) { pos.左边界 赋值为 new TreeNode(值); break; }
      else pos = pos.left; // 否则
    } else {
      // 否则
      if (pos.right === null) {
        pos.right = new TreeNode(val);
        break;
      } // 若 pos.右边界 全等于 null) { pos.右边界 赋值为 new TreeNode(值); break; }
      else pos = pos.right; // 否则
    }
  }
  return root; // 返回 根节点
}
function toList(root: TreeNode | null): number[] {
  // 定义函数/方法 toList
  const res: number[] = []; // 把 []; 写入 const res: number[]
  const stack: (TreeNode | null)[] = [root]; // 把 [根节点]; 写入 const stack: (TreeNode | null)[]
  while (stack.length) {
    // 循环，直到不满足「栈.长度」
    const node = stack.pop()!; // 把 栈 弹出 )取反 存入 节点
    if (node) {
      // 若 节点
      res.push(node.val); // 把 节点.值 压入栈/数组尾部
      if (node.right) stack.push(node.right); // 若 节点.右边界) 栈 追加 节点.右边界);
      if (node.left) stack.push(node.left); // 若 节点.左边界) 栈 追加 节点.左边界);
    }
  }
  return res; // 返回 结果
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const root = new TreeNode(
    4,
    new TreeNode(2, new TreeNode(1), new TreeNode(3)),
    new TreeNode(7),
  );
  assertEq(toList(insertIntoBST(root, 5)), [4, 2, 1, 3, 7, 5], 'insert'); // 断言校验
  const r2 = new TreeNode(
    4,
    new TreeNode(2, new TreeNode(1), new TreeNode(3)),
    new TreeNode(7),
  );
  assertEq(toList(insertIntoBST(r2, 5)), [4, 2, 1, 3, 7, 5], 'insert2'); // 断言校验
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
