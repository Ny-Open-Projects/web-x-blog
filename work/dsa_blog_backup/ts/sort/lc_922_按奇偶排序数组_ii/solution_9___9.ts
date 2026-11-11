/**
 ** LeetCode 922. 按奇偶排序数组 II
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134394571
 ** 方案：方案9（按奇偶下标归位，不排序）
 */

function sortArrayByParityII(nums: number[]): number[] {
  // 定义函数/方法 sortArrayByParityII
  const res = new Array<number>(nums.length).fill(0); // 把 new Array 小于 number 超过 (数组.长度).fill(0) 存入 结果
  let e = 0; // 把 0 存入 e
  let o = 1; // 把 1 存入 o
  for (const x of nums) {
    // for (const x of 数组) {
    if (x % 2 === 0) {
      // 若 x 对…取模 2 全等于 0
      res[e] = x; // 把 x; 写入 res[e]
      e += 2; // e累加 2
    } else {
      // 否则
      res[o] = x; // 把 x; 写入 res[o]
      o += 2; // o累加 2
    }
  }
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const a = sortArrayByParityII([4, 2, 5, 7]); // 把 sortArrayByParityII([4, 2, 5, 7]) 存入 数组
  if (a.join(',') !== '4,5,2,7') throw new Error('case1 mismatch: ' + a); // 若 数组.join(「,」) 不等于 「,」) throw new Error(「,」 加 数组);
  const b = sortArrayByParityII([2, 3]); // 把 sortArrayByParityII([2, 3]) 存入 b
  if (b.join(',') !== '2,3') throw new Error('case2 mismatch: ' + b); // 若 b.join(「,」) 不等于 「,」) throw new Error(「,」 加 b);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
