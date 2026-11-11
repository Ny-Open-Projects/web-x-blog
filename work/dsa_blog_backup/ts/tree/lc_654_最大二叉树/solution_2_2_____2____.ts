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
    const n = nums.length; // 把 数组.长度 存入 元素个数
    if (n === 0) return null; // 若 元素个数 全等于 0，直接返回 null
    const stack: number[] = []; // 把 []; 写入 const stack: number[]
    const tree: TreeNode[] = []; // 把 []; 写入 const tree: TreeNode[]
    for (let i = 0; i < n; i++) tree.push(new TreeNode(nums[i])); // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    for (let i = 0; i < n; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      while (stack.length > 0 && nums[i] > nums[stack[stack.length - 1]]) {
        // 循环，直到不满足「栈.长度 超过 0 且 数组[下标 i] 超过 数组[栈[栈.长度 减 1]]」
        tree[i].left = tree[stack[stack.length - 1]]; // 把 tree[栈[栈.长度 减 1]]; 写入 左边界
        stack.pop(); // 弹出栈顶元素
      }
      if (stack.length > 0) {
        // 若 栈.长度 超过 0
        tree[stack[stack.length - 1]].right = tree[i]; // 把 tree[下标 i]; 写入 右边界
      }
      stack.push(i); // 把 下标 i 压入栈/数组尾部
    }
    return tree[stack[0]]; // 返回 tree[栈[0]]
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
