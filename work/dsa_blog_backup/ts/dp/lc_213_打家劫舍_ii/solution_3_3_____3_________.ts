// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function helper(nums: number[], l: number, r: number): number {
    // 定义函数/方法 helper
    let prev = 0,
      cur = 0; // 把 0, 当前值 赋值为 0 存入 前一个
    for (let i = l; i <= r; i++) {
      const t = cur;
      cur = Math.max(cur, prev + nums[i]);
      prev = t;
    } // 让 下标 i 从 左指针 开始计数，下标 i 不超过 右指针 就继续
    return cur; // 返回 当前值
  }
  function rob(nums: number[]): number {
    // 定义函数/方法 rob
    const n = nums.length; // 把 数组.长度 存入 元素个数
    if (n === 0) return 0; // 若 元素个数 全等于 0，直接返回 0
    if (n === 1) return nums[0]; // 若 元素个数 全等于 1，直接返回 数组[0]
    return Math.max(helper(nums, 0, n - 2), helper(nums, 1, n - 1)); // 返回 Math.取较大值 helper(数组,0,元素个数 减 2), helper(数组,1,元素个数 减 1))
  }
  const cases = [
    { in: [2, 3, 2], want: 3 },
    { in: [1, 2, 3, 1], want: 4 },
    { in: [1, 2, 1, 1], want: 3 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = rob(c.in); // 把 rob(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
