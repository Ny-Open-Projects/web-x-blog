// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function radixSort(nums: number[]): number[] {
    // 定义函数/方法 radixSort
    if (nums.length === 0) return nums; // 若 数组.长度 全等于 0，直接返回 数组
    let min_val = nums[0],
      max_val = nums[0]; // 把 数组[0], max_val 赋值为 数组[0] 存入 min_val
    for (const x of nums) {
      if (x < min_val) min_val = x;
      if (x > max_val) max_val = x;
    }
    const offset = min_val < 0 ? -min_val : 0; // 把 min_val 小于 0 ? 减 min_val : 0 存入 offset
    let adjusted = nums.map((x) => x + offset);
    let max_adjusted = adjusted[0]; // 把 adjusted[0] 存入 max_adjusted
    for (const x of adjusted) if (x > max_adjusted) max_adjusted = x;
    let radix = 1; // 把 1 存入 radix
    const tmp = new Array(adjusted.length).fill(0); // 把 new Array(adjusted.长度).fill(0) 存入 临时变量
    while (max_adjusted >= radix) {
      // 循环，直到不满足「max_adjusted 不低于 radix」
      const bucket = new Array(10).fill(0); // 把 new Array(10).fill(0) 存入 bucket
      for (const num of adjusted) {
        // for (const num of adjusted) {
        const d = Math.floor(num / radix) % 10; // 把 向下取整(num 除以 radix) 对…取模 10 存入 d
        bucket[d] += 1; // bucket[d]累加 1
      }
      for (let i = 1; i < 10; i++) bucket[i] += bucket[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 10 就继续
      for (let i = adjusted.length - 1; i >= 0; i--) {
        // 让 下标 i 从 adjusted.长度 减 1 开始计数，下标 i 不低于 0 就继续
        const d = Math.floor(adjusted[i] / radix) % 10; // 把 向下取整(adjusted[下标 i] 除以 radix) 对…取模 10 存入 d
        tmp[bucket[d] - 1] = adjusted[i]; // 把 adjusted[下标 i]; 写入 tmp[bucket[d] - 1]
        bucket[d] -= 1; // bucket[d]累减 1
      }
      for (let i = 0; i < adjusted.length; i++) adjusted[i] = tmp[i]; // 让 下标 i 从 0 开始计数，下标 i 小于 adjusted.长度 就继续
      radix *= 10; // 把 10; 写入 radix *
    }
    return adjusted.map((x) => x - offset);
  }
  const cases: number[][] = [
    [1, 2, 3],
    [5, 4, 3, 2, 1],
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], // [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
  ];
  const wants: number[][] = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], // [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
  ];
  let fail = false; // 把 false 存入 fail
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = radixSort(cases[i]); // 把 radixSort(cases[下标 i]) 存入 got
    if (got.length !== wants[i].length) {
      fail = true;
      console.log('FAIL len ' + i);
      continue;
    }
    for (let j = 0; j < got.length; j++)
      if (got[j] !== wants[i][j]) {
        fail = true;
        console.log(
          'FAIL case ' +
            i +
            ' idx ' +
            j +
            ' got ' +
            got[j] +
            ' want ' +
            wants[i][j],
        );
      } // 让 下标 j 从 0 开始计数，下标 j 小于 got.长度 就继续
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
