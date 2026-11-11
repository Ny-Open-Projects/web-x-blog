// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
/**
 ** LeetCode 1356. 根据数字二进制下 1 的数目排序
 ** 方案：方案2（递推预处理 bit 计数）
 */

function sortByBits(arr: number[]): number[] {
  // 定义函数/方法 sortByBits
  const bit = new Array<number>(10001).fill(0); // 把 new Array 小于 number 超过 (10001).fill(0) 存入 bit
  for (let i = 1; i < 10001; i++) bit[i] = bit[i >> 1] + (i & 1); // 让 下标 i 从 1 开始计数，下标 i 小于 10001 就继续
  const sorted = arr.slice(); // 把 数组 截取 ) 存入 sorted
  sorted.sort((a, b) => bit[a] - bit[b] || a - b);
  return sorted; // 返回 sorted
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const got = sortByBits([1, 2, 3]); // 把 sortByBits([1, 2, 3]) 存入 got
  const expected = [1, 2, 3]; // 把 [1, 2, 3] 存入 expected
  if (got.length !== expected.length || got.some((v, i) => v !== expected[i]))
    throw new Error('sortByBits([1,2,3]) mismatch'); // throw new Error(「sortByBits([1,2,3]) mismatch」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
