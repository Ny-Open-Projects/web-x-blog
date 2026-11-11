/**
 ** LeetCode 131. 分割回文串
 ** 方案1: 回溯（忠实翻译 python 参考实现）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145240399
 */

function partition(s: string): string[][] {
  // 定义函数/方法 partition
  const result: string[][] = []; // 把 []; 写入 const result: string[][]
  function backtrack(start: number, path: string[]): void {
    // 定义函数/方法 backtrack
    if (start === s.length) {
      // 若 起点 全等于 字符串.长度
      result.push([...path]); // 把 复制的 当前路径 压入栈/数组尾部
      return; // return;
    }
    for (let end = start + 1; end <= s.length; end++) {
      // 让 终点 从 起点 加 1 开始计数，终点 不超过 字符串.长度 就继续
      const sub = s.slice(start, end); // 把 字符串 截取 起点, 终点) 存入 sub
      if (sub === sub.split('').reverse().join('')) {
        // 若 sub 全等于 sub.split('').reverse().join(''
        path.push(sub); // 把 sub 压入栈/数组尾部
        backtrack(end, path); // backtrack(终点, 当前路径);
        path.pop(); // 弹出栈顶元素
      }
    }
  }
  backtrack(0, []); // backtrack(0, []);
  return result; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr2(a: string[][], b: string[][]): boolean {
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
  const cases: { in: string; want: string[][] }[] = [
    {
      in: 'aab',
      want: [
        ['a', 'a', 'b'],
        ['aa', 'b'],
      ],
    },
    { in: 'abc', want: [['a', 'b', 'c']] },
    { in: 'a', want: [['a']] },
    {
      in: 'racecar',
      want: [
        ['r', 'a', 'c', 'e', 'c', 'a', 'r'],
        ['r', 'a', 'cec', 'a', 'r'],
        ['r', 'aceca', 'r'],
        ['racecar'],
      ],
    },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = partition(c.in); // 把 partition(字符.in) 存入 got
    if (!eqArr2(got, c.want)) {
      // 若 取反 eqArr2(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL partition(' +
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
