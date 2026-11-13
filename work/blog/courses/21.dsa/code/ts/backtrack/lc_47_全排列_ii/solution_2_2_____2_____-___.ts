/**
 ** LeetCode 47. 全排列 II
 ** 方案2: 搜索回溯-优化版（忠实翻译 python 参考实现）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145233874
 */

function permuteUnique(nums: number[]): number[][] {
  // 定义函数/方法 permuteUnique
  const sorted = nums.slice().sort((a, b) => a - b);
  const res: number[][] = []; // 把 []; 写入 const res: number[][]
  const used: boolean[] = new Array(sorted.length).fill(false); // 把 new Array(sorted.长度).fill(false); 写入 const used: boolean[]
  function backtrack(path: number[]): void {
    // 定义函数/方法 backtrack
    if (path.length === sorted.length) {
      // 若 当前路径.长度 全等于 sorted.长度
      res.push(path.slice()); // 把 当前路径 截取 压入栈/数组尾部
      return; // return;
    }
    for (let i = 0; i < sorted.length; i++) {
      // 让 下标 i 从 0 开始计数，下标 i 小于 sorted.长度 就继续
      if (used[i]) continue; // 若 已用标记[下标 i]) continue;
      if (i > 0 && sorted[i] === sorted[i - 1] && !used[i - 1]) continue;
      used[i] = true; // 把 true; 写入 used[i]
      path.push(sorted[i]); // 把 sorted[下标 i] 压入栈/数组尾部
      backtrack(path); // backtrack(当前路径);
      path.pop(); // 弹出栈顶元素
      used[i] = false; // 把 false; 写入 used[i]
    }
  }
  backtrack([]); // backtrack([]);
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function norm(x: number[][]): string {
    // 定义函数/方法 norm
    return x
      .map((r) => r.join(','))
      .sort()
      .join('|');
  }
  function eqArr2(a: number[][], b: number[][]): boolean {
    // 定义函数/方法 eqArr2
    return a.length === b.length && norm(a) === norm(b); // 返回 数组.长度 全等于 b.长度 且 norm(数组) 全等于 norm(b)
  }
  const cases: { in: number[]; want: number[][] }[] = [
    {
      in: [1, 1, 2],
      want: [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1],
      ],
    },
    {
      in: [1, 2, 3],
      want: [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
      ],
    },
    { in: [1], want: [[1]] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = permuteUnique(c.in); // 把 permuteUnique(字符.in) 存入 got
    if (!eqArr2(got, c.want)) {
      // 若 取反 eqArr2(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL permuteUnique(' +
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
