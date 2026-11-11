// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function countBinarySubstrings(s: string): number {
    // 定义函数/方法 countBinarySubstrings
    const groups: number[] = []; // 把 []; 写入 const groups: number[]
    let i = 0; // 把 0 存入 下标 i
    const n = s.length; // 把 字符串.长度 存入 元素个数
    while (i < n) {
      // 循环，直到不满足「下标 i 小于 元素个数」
      const ch = s[i]; // 把 字符串[下标 i] 存入 字符
      let cnt = 0; // 把 0 存入 计数
      while (i < n && s[i] === ch) {
        // 循环，直到不满足「下标 i 小于 元素个数 且 字符串[下标 i] 全等于 字符」
        cnt += 1; // 计数累加 1
        i += 1; // 下标 i累加 1
      }
      groups.push(cnt); // 把 计数 压入栈/数组尾部
    }
    let ans = 0; // 把 0 存入 答案
    for (let j = 1; j < groups.length; j++) {
      // 让 下标 j 从 1 开始计数，下标 j 小于 groups.长度 就继续
      ans += Math.min(groups[j - 1], groups[j]); // 答案累加 Math.取较小值 groups[下标 j 减 1], groups[下标 j])
    }
    return ans; // 返回 答案
  }
  const cases: { in: string; want: number }[] = [
    { in: '00110011', want: 6 },
    { in: '10101', want: 4 },
    { in: '0', want: 0 },
    { in: '111000', want: 3 },
    { in: 'abc', want: 2 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = countBinarySubstrings(c.in); // 把 countBinarySubstrings(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL countBinarySubstrings(' + c.in + ')=' + got + ' want ' + c.want,
      ); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
