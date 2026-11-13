// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091535
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  class TreeNode {
    // 定义类型
    val: number; // 值: number;
    left: TreeNode | null; // 左边界: TreeNode 按位或 null;
    right: TreeNode | null; // 右边界: TreeNode 按位或 null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
      this.val = val === undefined ? 0 : val; // 把 (值 全等于 undefined ? 0 : 值); 写入 值
      this.left = left === undefined ? null : left; // 把 (左边界 全等于 undefined ? null : 左边界); 写入 左边界
      this.right = right === undefined ? null : right; // 把 (右边界 全等于 undefined ? null : 右边界); 写入 右边界
    }
  }
  function constructMaximumBinaryTree(nums: number[]): TreeNode | null {
    // 定义函数/方法 constructMaximumBinaryTree
    if (!nums || nums.length === 0) return null; // 若 取反 数组 或 数组.长度 全等于 0，直接返回 null
    let idx = 0; // 把 0 存入 idx
    for (let i = 0; i < nums.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (nums[i] > nums[idx]) idx = i; // 若 数组[下标 i] 超过 数组[idx]) idx 赋值为 下标 i;
    }
    const root = new TreeNode(nums[idx]); // 把 new TreeNode(数组[idx]) 存入 根节点
    root.left = constructMaximumBinaryTree(nums.slice(0, idx)); // 把 constructMaximumBinaryTree(数组 截取 0, idx)); 写入 左边界
    root.right = constructMaximumBinaryTree(nums.slice(idx + 1)); // 把 constructMaximumBinaryTree(数组 截取 idx 加 1)); 写入 右边界
    return root; // 返回 根节点
  }
  const cases = [
    { t: [3, 2, 1, 6, 0, 5], want: 6 },
    { t: [1], want: 1 },
    { t: [3, 2, 1], want: 3 },
    { t: [], want: null },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = constructMaximumBinaryTree(c.t); // 把 constructMaximumBinaryTree(字符.另一字符串) 存入 got
    const gotv = got ? got.val : null; // 把 got ? got.值 : null 存入 gotv
    if (gotv !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', gotv);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
