/**
 ** LeetCode 39. 组合总和
 ** 方案1: 搜索回溯（忠实翻译 python 参考实现）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145239508
 */

function combinationSum(candidates: number[], target: number): number[][] {
  // 定义函数/方法 combinationSum
  const sorted = candidates.slice().sort((a, b) => a - b);
  const result: number[][] = []; // 把 []; 写入 const result: number[][]
  function backtrack(start: number, path: number[], remaining: number): void {
    // 定义函数/方法 backtrack
    if (remaining === 0) {
      // 若 remaining 全等于 0
      result.push([...path]); // 把 复制的 当前路径 压入栈/数组尾部
      return; // return;
    }
    for (let i = start; i < sorted.length; i++) {
      // 让 下标 i 从 起点 开始计数，下标 i 小于 sorted.长度 就继续
      if (sorted[i] > remaining) break; // 若 sorted[下标 i] 超过 remaining) break;
      path.push(sorted[i]); // 把 sorted[下标 i] 压入栈/数组尾部
      backtrack(i, path, remaining - sorted[i]); // backtrack(下标 i, 当前路径, remaining 减 sorted[下标 i]);
      path.pop(); // 弹出栈顶元素
    }
  }
  backtrack(0, [], target); // backtrack(0, [], 目标值);
  return result; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr2(a: number[][], b: number[][]): boolean {
    // 定义函数/方法 eqArr2
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
      if (a[i].length !== b[i].length) return false; // 若 数组[下标 i].长度 不等于 b[下标 i].长度，直接返回 false
      for (let j = 0; j < a[i].length; j++) {
        // 让 下标 j 从 0 开始计数，下标 j 小于 数组[下标 i].长度 就继续
        if (a[i][j] !== b[i][j]) return false; // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]，直接返回 false
      }
    }
    return true; // 返回 true
  }
  const cases: { in: [number[], number]; want: number[][] }[] = [
    { in: [[2, 3, 6, 7], 7], want: [[2, 2, 3], [7]] },
    {
      in: [[2, 3, 5], 8],
      want: [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5],
      ],
    },
    { in: [[2], 1], want: [] },
    { in: [[2, 3, 6, 7], 1], want: [] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = combinationSum(c.in[0], c.in[1]); // 把 combinationSum(字符.in[0], 字符.in[1]) 存入 got
    if (!eqArr2(got, c.want)) {
      // 若 取反 eqArr2(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL combinationSum(' +
          JSON.stringify(c.in) +
          ') got=' +
          JSON.stringify(got) +
          ' want=' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
