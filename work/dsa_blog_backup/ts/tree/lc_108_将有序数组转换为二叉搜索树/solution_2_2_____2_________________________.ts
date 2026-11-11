/**
 ** LeetCode 108. 将有序数组转换为二叉搜索树
 ** 方案：2 ) 方案2: 中序遍历，总是选择中间位置右边的数字作为根节点
 ** 来源：https://blog.csdn.net/tyro_java/article/details/144993168
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class TreeNode {
    // 定义类型
    val: number; // 值: number;
    left: TreeNode | null; // 左边界: TreeNode 按位或 null;
    right: TreeNode | null; // 右边界: TreeNode 按位或 null;
    constructor(v: number) {
      this.val = v;
      this.left = null;
      this.right = null;
    } // 把 值; this.左边界 赋值为 null; this.右边界 赋值为 null; } 写入 值
  }

  function sortedArrayToBST(nums: number[]): TreeNode | null {
    // 定义函数/方法 sortedArrayToBST
    return helper(nums, 0, nums.length - 1); // 返回 helper(数组, 0, 数组.长度 减 1)
  }

  function helper(
    nums: number[],
    left: number,
    right: number,
  ): TreeNode | null {
    // 定义函数/方法 helper
    if (left > right) return null; // 若 左边界 超过 右边界，直接返回 null

    // 总是选择中间位置右边的数字作为根节点
    const mid = Math.floor((left + right + 1) / 2); // 加1保证了当长度为偶数时取右中位数
    const root = new TreeNode(nums[mid]); // 把 new TreeNode(数组[中点]) 存入 根节点

    root.left = helper(nums, left, mid - 1); // 把 helper(数组, 左边界, 中点 减 1); 写入 左边界
    root.right = helper(nums, mid + 1, right); // 把 helper(数组, 中点 加 1, 右边界); 写入 右边界

    return root; // 返回 根节点
  }

  function inorder(root: TreeNode | null, out: number[]): number[] {
    // 定义函数/方法 inorder
    if (root === null) return out; // 若 根节点 全等于 null，直接返回 out
    inorder(root.left, out); // inorder(根节点.左边界, out);
    out.push(root.val); // 把 根节点.值 压入栈/数组尾部
    inorder(root.right, out); // inorder(根节点.右边界, out);
    return out; // 返回 out
  }

  // 层序序列化（尾部 null 裁剪），与 LeetCode 表示一致
  function serialize(root: TreeNode | null): (number | null)[] {
    // 定义函数/方法 serialize
    if (root === null) return []; // 若 根节点 全等于 null，直接返回 []
    const out: (number | null)[] = []; // 把 []; 写入 const out: (number | null)[]
    const q: (TreeNode | null)[] = [root]; // 把 [根节点]; 写入 const q: (TreeNode | null)[]
    let head = 0; // 把 0 存入 头节点
    while (head < q.length) {
      // 循环，直到不满足「头节点 小于 节点.长度」
      const node = q[head++]; // 把 节点[头节点 加一 ] 存入 节点
      if (node === null) {
        out.push(null);
        continue;
      } // 若 节点 全等于 null) { out 追加 null); continue; }
      out.push(node.val); // 把 节点.值 压入栈/数组尾部
      q.push(node.left); // 把 节点.左边界 压入栈/数组尾部
      q.push(node.right); // 把 节点.右边界 压入栈/数组尾部
    }
    while (out.length > 0 && out[out.length - 1] === null) out.pop(); // 循环，直到不满足「out.长度 超过 0 且 out[out.长度 减 1] 全等于 null) out 弹出 );」
    return out; // 返回 out
  }

  function eqArr(a: (number | null)[], b: (number | null)[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { in: number[]; want: (number | null)[] }[] = [
    { in: [-10, -3, 0, 5, 9], want: [0, -3, 9, -10, null, 5] },
    { in: [1], want: [1] },
    { in: [], want: [] },
    { in: [1, 2, 3, 4, 5, 6, 7], want: [4, 2, 6, 1, 3, 5, 7] },
  ];

  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = serialize(sortedArrayToBST(c.in)); // 把 serialize(sortedArrayToBST(字符.in)) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL sortedArrayToBST(' +
          JSON.stringify(c.in) +
          ')=' +
          JSON.stringify(got) +
          ' want ' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
    // 附加性质：中序序列必须等于排序后的输入（BST 不变量）
    const io = inorder(sortedArrayToBST(c.in), []); // 把 inorder(sortedArrayToBST(字符.in), []) 存入 io
    const sorted = c.in.slice().sort((a, b) => a - b);
    if (!eqArr(io, sorted)) {
      // 若 取反 eqArr(io, sorted
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL inorder(' +
          JSON.stringify(c.in) +
          ')=' +
          JSON.stringify(io) +
          ' want sorted ' +
          JSON.stringify(sorted),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
