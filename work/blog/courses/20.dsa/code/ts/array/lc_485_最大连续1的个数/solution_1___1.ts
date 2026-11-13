/**
 ** LeetCode 485. 最大连续1的个数
 ** 忠实化打样：算法对标 python 参考实现 ref_findMaxConsecutiveOnes
 */

function findMaxConsecutiveOnes(nums: number[]): number {
  // 定义函数/方法 findMaxConsecutiveOnes
  let best = 0,
    cur = 0; // 把 0, 当前值 赋值为 0 存入 当前最优
  for (const x of nums) {
    // for (const x of 数组) {
    if (x === 1) {
      // 若 x 全等于 1
      cur++; // 当前值 加一
      if (cur > best) best = cur; // 若 当前值 超过 当前最优) 当前最优 赋值为 当前值;
    } else {
      // 否则
      cur = 0; // 把 0 存入 当前值
    }
  }
  return best; // 返回 当前最优
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number][] = [
    [[1, 1, 0, 1, 1, 1], 3],
    [[1, 0, 1, 1, 0, 1], 2],
    [[0], 0],
  ];
  for (const [nums, want] of cases) {
    // for (const [数组, want] of cases) {
    const got = findMaxConsecutiveOnes(nums); // 把 findMaxConsecutiveOnes(数组) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error('FAIL: got ' + got + ' expected ' + want); // throw new Error(「FAIL: got 」 加 got 加 「FAIL: got 」 加 want);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
