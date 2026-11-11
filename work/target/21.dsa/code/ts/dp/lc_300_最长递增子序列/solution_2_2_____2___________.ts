// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144823912
/**
 ** LeetCode 300. 最长递增子序列
 ** 方案：方案2（动态规划 + 二分查找 O(n log n)）
 ** 来源：python 参考忠实移植
 */

function lengthOfLIS(nums: number[]): number {
  // 定义函数/方法 lengthOfLIS
  const n = nums.length; // 把 数组.长度 存入 元素个数
  if (n === 0) return 0; // 若 元素个数 全等于 0，直接返回 0
  const dp: number[] = []; // 把 []; 写入 const dp: number[]
  for (const num of nums) {
    // for (const num of 数组) {
    let lo = 0,
      hi = dp.length; // 把 0, 右边界 赋值为 DP 表.长度 存入 左边界
    while (lo < hi) {
      // 循环，直到不满足「左边界 小于 右边界」
      const mid = (lo + hi) >> 1; // 把 (左边界 加 右边界) 超过 超过 1 存入 中点
      if (dp[mid] < num)
        lo = mid + 1; // 若 DP 表[中点] 小于 num) 左边界 赋值为 中点 加 1;
      else hi = mid; // 否则
    }
    if (lo === dp.length)
      dp.push(num); // 若 左边界 全等于 DP 表.长度) DP 表 追加 num);
    else dp[lo] = num; // 否则
  }
  return dp.length; // 返回 DP 表.长度
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: { in: number[]; want: number }[] = [
    { in: [10, 9, 2, 5, 3, 7, 101, 18], want: 4 },
    { in: [0, 1, 0, 3, 2, 3], want: 4 },
    { in: [7, 7, 7, 7], want: 1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = lengthOfLIS(c.in); // 把 lengthOfLIS(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log('FAIL', JSON.stringify(c.in), 'want', c.want, 'got', got); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
