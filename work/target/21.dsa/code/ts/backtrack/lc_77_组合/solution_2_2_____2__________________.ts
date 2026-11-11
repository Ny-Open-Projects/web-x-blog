/**
 ** LeetCode 77. 组合
 ** 方案2: 非递归（字典序法）实现组合型枚举（忠实翻译 python 参考实现）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145240015
 */

function combine(n: number, k: number): number[][] {
  // 定义函数/方法 combine
  const result: number[][] = []; // 把 []; 写入 const result: number[][]
  function backtrack(start: number, path: number[]): void {
    // 定义函数/方法 backtrack
    if (path.length === k) {
      // 若 当前路径.长度 全等于 下标 k
      result.push(path.slice()); // 把 当前路径 截取 压入栈/数组尾部
      return; // return;
    }
    for (let i = start; i <= n; i++) {
      // 让 下标 i 从 起点 开始计数，下标 i 不超过 元素个数 就继续
      path.push(i); // 把 下标 i 压入栈/数组尾部
      backtrack(i + 1, path); // backtrack(下标 i 加 1, 当前路径);
      path.pop(); // 弹出栈顶元素
    }
  }
  backtrack(1, []); // backtrack(1, []);
  return result; // 返回 结果
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
  function eq(a: number[][], b: number[][]): boolean {
    // 定义函数/方法 eq
    return a.length === b.length && norm(a) === norm(b); // 返回 数组.长度 全等于 b.长度 且 norm(数组) 全等于 norm(b)
  }
  const cases: { in: [number, number]; want: number[][] }[] = [
    {
      in: [4, 2],
      want: [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
      ],
    },
    {
      in: [5, 3],
      want: [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 5],
        [3, 4, 5],
      ],
    },
    { in: [1, 1], want: [[1]] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = combine(c.in[0], c.in[1]); // 把 combine(字符.in[0], 字符.in[1]) 存入 got
    if (!eq(got, c.want)) {
      // 若 取反 eq(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL combine(' +
          c.in +
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
