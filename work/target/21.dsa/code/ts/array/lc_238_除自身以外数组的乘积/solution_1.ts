/** 来源: LeetCode 238 除自身以外数组的乘积 */
export function productExceptSelf(nums: number[]): number[] {
  // 定义函数/方法 productExceptSelf
  const n = nums.length; // 把 数组.长度 存入 元素个数
  const out = new Array(n).fill(1); // 把 new Array(元素个数).fill(1) 存入 out
  let p = 1; // 把 1 存入 节点
  for (let i = 0; i < n; i++) {
    out[i] = p;
    p *= nums[i];
  } // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
  p = 1; // 把 1 存入 节点
  for (let i = n - 1; i >= 0; i--) {
    out[i] *= p;
    p *= nums[i];
  } // 让 下标 i 从 元素个数 减 1 开始计数，下标 i 不低于 0 就继续
  return out; // 返回 out
}

function eqList(a: number[], b: number[]): boolean {
  // 定义函数/方法 eqList
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number[]][] = [
    [
      [1, 2, 3, 4],
      [24, 12, 8, 6],
    ],
    [
      [0, 0],
      [0, 0],
    ],
    [
      [-1, 1, 0, -3, 3],
      [0, 0, 9, 0, 0],
    ],
  ];
  for (const [inp, want] of cases) {
    // for (const [inp, want] of cases) {
    const got = productExceptSelf(inp); // 把 productExceptSelf(inp) 存入 got
    if (!eqList(got, want))
      throw new Error(
        `FAIL in=${JSON.stringify(inp)} want=${JSON.stringify(want)} got=${JSON.stringify(got)}`,
      );
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
