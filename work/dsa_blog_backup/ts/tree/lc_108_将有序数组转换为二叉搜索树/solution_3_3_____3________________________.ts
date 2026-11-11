/**
 ** LeetCode 108. 将有序数组转换为二叉搜索树
 ** 方案：3 ) 方案3: 中序遍历，选择任意一个中间位置数字作为根节点
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

    // 随机选取一个合法根，得到不同但同样合法的 BST（保留原"变体"意图）
    const mid = left + Math.floor(Math.random() * (right - left + 1)); // 把 左边界 加 向下取整(Math.random() 乘 (右边界 减 左边界 加 1)) 存入 中点
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

  // 校验 BST 不变量：左子树全部小于 root，右子树全部大于 root
  function isValidBST(
    root: TreeNode | null,
    lo: number | null,
    hi: number | null,
  ): boolean {
    // 定义判定函数 isValidBST
    if (root === null) return true; // 若 根节点 全等于 null，直接返回 true
    if (lo !== null && root.val <= lo) return false; // 若 左边界 不等于 null 且 根节点.值 不超过 左边界，直接返回 false
    if (hi !== null && root.val >= hi) return false; // 若 右边界 不等于 null 且 根节点.值 不低于 右边界，直接返回 false
    return (
      isValidBST(root.left, lo, root.val) &&
      isValidBST(root.right, root.val, hi)
    );
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: number[][] = [
    [-10, -3, 0, 5, 9],
    [1],
    [],
    [1, 2, 3, 4, 5, 6, 7],
  ];

  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const root = sortedArrayToBST(c); // 把 sortedArrayToBST(字符) 存入 根节点
    // 随机中点使树形不确定，但中序遍历必须恒等于排序后的输入
    const io = inorder(root, []); // 把 inorder(根节点, []) 存入 io
    const sorted = c.slice().sort((a, b) => a - b);
    if (!eqArr(io, sorted)) {
      // 若 取反 eqArr(io, sorted
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL inorder(' +
          JSON.stringify(c) +
          ')=' +
          JSON.stringify(io) +
          ' want sorted ' +
          JSON.stringify(sorted),
      ); // 打印输出
    }
    if (!isValidBST(root, null, null)) {
      // 若 取反 isValidBST(根节点, null, null
      fail = true; // 把 true 存入 fail
      console.log('FAIL isValidBST(' + JSON.stringify(c) + ')=false'); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
