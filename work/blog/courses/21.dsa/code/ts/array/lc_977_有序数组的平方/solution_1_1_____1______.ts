// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
/**
 ** LeetCode 977. 有序数组的平方
 ** 方案1: 直接排序
 */

function sortedSquares(nums: number[]): number[] {
  // 定义函数/方法 sortedSquares
  const ans: number[] = nums.map((x) => x * x);
  ans.sort((a, b) => a - b);
  return ans; // 返回 答案
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases: { in: number[]; want: number[] }[] = [
    { in: [1, 2, 3], want: [1, 4, 9] },
    { in: [-4, -1, 0, 3, 10], want: [0, 1, 9, 16, 100] },
    { in: [-7, -3, 2, 3, 11], want: [4, 9, 9, 49, 121] },
    { in: [], want: [] },
    { in: [0], want: [0] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = sortedSquares([...c.in]); // 把 sortedSquares([...字符.in]) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL sortedSquares(' +
          JSON.stringify(c.in) +
          ')=' +
          JSON.stringify(got) +
          ' want ' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
