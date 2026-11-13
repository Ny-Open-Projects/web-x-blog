// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
/**
 ** LeetCode 922. 按奇偶排序数组 II
 ** 方案：方案1（先排序再按奇偶下标归位）
 */

function sortArrayByParityII(nums: number[]): number[] {
  // 定义函数/方法 sortArrayByParityII
  const sorted = nums.slice().sort((a, b) => a - b);
  const res = new Array<number>(nums.length).fill(0); // 把 new Array 小于 number 超过 (数组.长度).fill(0) 存入 结果
  let odd = 1; // 把 1 存入 odd
  let even = 0; // 把 0 存入 even
  for (const item of sorted) {
    // for (const item of sorted) {
    if (item % 2 === 1) {
      // 若 item 对…取模 2 全等于 1
      res[odd] = item; // 把 item; 写入 res[odd]
      odd += 2; // odd累加 2
    } else {
      // 否则
      res[even] = item; // 把 item; 写入 res[even]
      even += 2; // even累加 2
    }
  }
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const got = sortArrayByParityII([4, 2, 5, 7]); // 把 sortArrayByParityII([4, 2, 5, 7]) 存入 got
  const expected = [2, 5, 4, 7]; // 把 [2, 5, 4, 7] 存入 expected
  if (got.length !== expected.length || got.some((v, i) => v !== expected[i]))
    throw new Error('sortArrayByParityII([4,2,5,7]) mismatch'); // throw new Error(「sortArrayByParityII([4,2,5,7]) mismatch」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
