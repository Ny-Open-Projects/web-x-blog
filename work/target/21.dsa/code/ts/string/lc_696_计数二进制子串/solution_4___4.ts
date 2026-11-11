// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
// 忠实翻译 python solution_4（countBinarySubstrings2）：双游标，无需额外数组
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function countBinarySubstrings2(s: string): number {
    // 定义函数/方法 countBinarySubstrings2
    let prev = 0; // 把 0 存入 前一个
    let curr = 1; // 把 1 存入 当前值
    let res = 0; // 把 0 存入 结果
    for (let i = 1; i < s.length; i++) {
      // 让 下标 i 从 1 开始计数，下标 i 小于 字符串.长度 就继续
      if (s[i] !== s[i - 1]) {
        // 若 字符串[下标 i] 不等于 字符串[下标 i 减 1]
        res += Math.min(prev, curr); // 结果累加 Math.取较小值 前一个, 当前值)
        prev = curr; // 把 当前值 存入 前一个
        curr = 1; // 把 1 存入 当前值
      } else {
        // 否则
        curr += 1; // 当前值累加 1
      }
    }
    return res + Math.min(prev, curr); // 返回 结果 加 Math.取较小值 前一个, 当前值)
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
    const got = countBinarySubstrings2(c.in); // 把 countBinarySubstrings2(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL countBinarySubstrings2(' + c.in + ')=' + got + ' want ' + c.want,
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
