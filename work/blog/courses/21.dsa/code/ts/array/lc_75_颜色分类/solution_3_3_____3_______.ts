/**
 ** LeetCode 75. 颜色分类
 ** 方案：1 ) 方案1：单指针
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145370043
 */

function sortColors(nums: number[]): void {
  // 定义函数/方法 sortColors
  const n = nums.length; // 把 数组.长度 存入 元素个数
  let p0 = 0,
    p2 = n - 1; // 把 0, p2 赋值为 元素个数 减 1 存入 p0
  let i = 0; // 把 0 存入 下标 i
  while (i <= p2) {
    // 循环，直到不满足「下标 i 不超过 p2」
    while (i <= p2 && nums[i] === 2) {
      // 循环，直到不满足「下标 i 不超过 p2 且 数组[下标 i] 全等于 2」
      const tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
      nums[i] = nums[p2]; // 把 数组[p2]; 写入 nums[i]
      nums[p2] = tmp; // 把 临时变量; 写入 nums[p2]
      p2--; // p2 减一
    }
    if (nums[i] === 0) {
      // 若 数组[下标 i] 全等于 0
      const tmp = nums[i]; // 把 数组[下标 i] 存入 临时变量
      nums[i] = nums[p0]; // 把 数组[p0]; 写入 nums[i]
      nums[p0] = tmp; // 把 临时变量; 写入 nums[p0]
      p0++; // p0 加一
    }
    i++; // 下标 i 加一
  }
}

function eqArr(a: number[], b: number[]): boolean {
  // 定义函数/方法 eqArr
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] !== b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number[]][] = [
    [
      [2, 0, 2, 1, 1, 0],
      [0, 0, 1, 1, 2, 2],
    ],
    [[0], [0]],
    [
      [2, 0, 1],
      [0, 1, 2],
    ],
  ];
  for (const [input, expected] of cases) {
    // for (const [input, expected] of cases) {
    sortColors(input); // sortColors(input);
    if (!eqArr(input, expected)) {
      // 若 取反 eqArr(input, expected
      throw new Error('FAIL: got ' + input + ' expected ' + expected);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
