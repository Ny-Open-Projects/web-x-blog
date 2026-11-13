// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function rob(nums: number[]): number {
    // 定义函数/方法 rob
    const n = nums.length; // 把 数组.长度 存入 元素个数
    if (n === 0) return 0; // 若 元素个数 全等于 0，直接返回 0
    if (n === 1) return nums[0]; // 若 元素个数 全等于 1，直接返回 数组[0]
    const dp1 = new Array(n).fill(0); // 把 new Array(元素个数).fill(0) 存入 dp1
    const dp2 = new Array(n).fill(0); // 把 new Array(元素个数).fill(0) 存入 dp2
    dp1[0] = nums[0]; // 把 数组[0]; 写入 dp1[0]
    dp1[1] = Math.max(nums[0], nums[1]); // 把 Math.取较大值 数组[0], 数组[1]); 写入 dp1[1]
    dp2[1] = nums[1]; // 把 数组[1]; 写入 dp2[1]
    for (let i = 2; i < n; i++)
      dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i]); // 让 下标 i 从 2 开始计数，下标 i 小于 元素个数 就继续
    for (let i = 2; i < n; i++)
      dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + nums[i]); // 让 下标 i 从 2 开始计数，下标 i 小于 元素个数 减 1 就继续
    return Math.max(dp1[n - 2], dp2[n - 1]); // 返回 Math.取较大值 dp1[元素个数 减 2], dp2[元素个数 减 1])
  }
  const cases = [
    { in: [2, 3, 2], want: 3 },
    { in: [1, 2, 3, 1], want: 4 },
    { in: [5], want: 5 },
    { in: [], want: 0 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = rob(c.in); // 把 rob(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log(
        'FAIL rob(' + JSON.stringify(c.in) + ')=' + got + ' want ' + c.want,
      );
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
