// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function rob(nums: number[]): number {
    // 定义函数/方法 rob
    const n = nums.length; // 把 数组.长度 存入 元素个数
    if (n === 0) return 0; // 若 元素个数 全等于 0，直接返回 0
    if (n === 1) return nums[0]; // 若 元素个数 全等于 1，直接返回 数组[0]
    function helper(arr: number[]): number {
      // 定义函数/方法 helper
      let f0 = 0,
        f1 = 0; // 把 0, f1 赋值为 0 存入 f0
      for (const x of arr) {
        const nf = Math.max(f1, f0 + x);
        f0 = f1;
        f1 = nf;
      }
      return f1; // 返回 f1
    }
    return Math.max(
      nums[0] + helper(nums.slice(2, n - 1)),
      helper(nums.slice(1, n)),
    );
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
