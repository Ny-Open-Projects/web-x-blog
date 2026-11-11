/**
 ** LeetCode 136. 只出现一次的数字
 ** 方案：1 ) 方案1: 位运算
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145029963
 */

// 位运算：所有元素异或，成对数字抵消，剩下只出现一次的数字。
// 忠实翻译自 Python 参考实现（方案1: 位运算）。
function singleNumber(nums: number[]): number {
  // 定义函数/方法 singleNumber
  let ret = 0; // 把 0 存入 ret
  for (const item of nums) {
    // for (const item of 数组) {
    ret ^= item; // 相同的数字，异或完成后都会变成 0
  }
  return ret; // 返回 ret
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
