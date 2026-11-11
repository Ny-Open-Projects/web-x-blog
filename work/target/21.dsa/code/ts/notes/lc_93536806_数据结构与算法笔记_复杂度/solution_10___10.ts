// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 暴力解法：时间复杂度 O(n^2)
  function twoSumBrute(nums: number[], target: number): number[] {
    // 定义函数/方法 twoSumBrute
    for (let i = 0; i < nums.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      for (let j = i + 1; j < nums.length; j++) {
        // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 数组.长度 就继续
        if (nums[i] + nums[j] === target) return [i, j]; // 若 数组[下标 i] 加 数组[下标 j] 全等于 目标值，直接返回 [下标 i, 下标 j]
      }
    }
    return []; // 返回 []
  }

  // 哈希表解法：时间复杂度 O(n)
  function twoSumHash(nums: number[], target: number): number[] {
    // 定义函数/方法 twoSumHash
    const seen = new Map<number, number>(); // 把 new Map 小于 number, number 超过 () 存入 已见集合
    for (let i = 0; i < nums.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      const num = nums[i]; // 把 数组[下标 i] 存入 num
      if (seen.has(target - num)) {
        // 若 已见集合.has(目标值 减 num
        return [seen.get(target - num) as number, i]; // 返回 [已见集合 查找 目标值 减 num) as number, 下标 i]
      }
      seen.set(num, i); // 已见集合.set(num, 下标 i);
    }
    return []; // 返回 []
  }

  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }

  const cases: { nums: number[]; target: number; want: number[] }[] = [
    { nums: [2, 7, 11, 15], target: 9, want: [0, 1] },
    { nums: [3, 2, 4], target: 6, want: [1, 2] },
    { nums: [3, 3], target: 6, want: [0, 1] },
    { nums: [1, 2, 3], target: 7, want: [] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const g1 = twoSumBrute(c.nums, c.target); // 把 twoSumBrute(字符.数组, 字符.目标值) 存入 g1
    const g2 = twoSumHash(c.nums, c.target); // 把 twoSumHash(字符.数组, 字符.目标值) 存入 g2
    if (!eqArr(g1, c.want) || !eqArr(g2, c.want)) {
      // 若 取反 eqArr(g1, 字符.want) 或 取反 eqArr(g2, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL twoSum(%o,%d): brute=%o hash=%o want %o',
        c.nums,
        c.target,
        g1,
        g2,
        c.want,
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
