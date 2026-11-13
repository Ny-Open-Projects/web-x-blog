/**
 ** LeetCode 136. 只出现一次的数字
 ** 方案：2 ) 方案2: 基于Set (不推荐)
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145029963
 */

// 基于集合：出现则删除，未出现则加入，最后集合里剩下的即为答案。
// 忠实翻译自 Python 参考实现（方案2: 基于 Set）。
function singleNumber(nums: number[]): number {
  // 定义函数/方法 singleNumber
  const set = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 set
  for (const num of nums) {
    // for (const num of 数组) {
    if (set.has(num)) {
      // 若 set.has(num
      set.delete(num); // set.delete(num);
    } else {
      // 否则
      set.add(num); // set 追加 num);
    }
  }
  // 题目保证恰好有一个只出现一次的数字
  return Array.from(set)[0]; // 返回 Array.from(set)[0]
}

// 自检入口：遍历 cases 逐一比对，任一不符则 throw（非 0 退出）。
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // (args, expected) 取自 _tools/correctness_check.py 的 lc_136_只出现一次的数字 cases
  const cases: Array<{ name: string; in: number[]; want: number }> = [
    { name: 'case1', in: [2, 2, 1], want: 1 },
    { name: 'case2', in: [4, 1, 2, 1, 2], want: 4 },
    { name: 'case3', in: [1], want: 1 },
  ];
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = singleNumber(c.in); // 把 singleNumber(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      throw new Error(`FAIL ${c.name}: got ${got} want ${c.want}`);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
