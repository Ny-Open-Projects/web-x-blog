/**
 ** LeetCode 682. 棒球比赛
 ** 来源：https://blog.csdn.net/tyro_java/article/details/130734875
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function calPoints(operations: string[]): number {
    // 定义函数/方法 calPoints
    const history: number[] = []; // 把 []; 写入 const history: number[]
    for (const op of operations) {
      // for (const op of operations) {
      if (op === 'C') {
        // 若 op 全等于 「C」
        history.pop(); // 弹出栈顶元素
      } else if (op === 'D') {
        // 否则，若 op 全等于 「D」
        history.push(history[history.length - 1] * 2); // 把 history[history.长度 减 1] 乘 2 压入栈/数组尾部
      } else if (op === '+') {
        // 否则，若 op 全等于 「 加 」
        history.push(history[history.length - 1] + history[history.length - 2]); // 把 history[history.长度 减 1] 加 history[history.长度 减 2] 压入栈/数组尾部
      } else {
        // 否则
        history.push(parseInt(op, 10)); // 把 转整数(op, 10 压入栈/数组尾部
      }
    }
    return history.reduce((a, b) => a + b, 0);
  }

  const cases: { in: string[]; want: number }[] = [
    { in: ['5', '2', 'C', 'D', '+'], want: 30 },
    { in: ['1', 'C'], want: 0 },
    { in: ['5', '-2', '4', 'C', 'D', '9', '+', '+'], want: 27 },
    { in: ['-3', '-4', '+'], want: -14 },
    { in: ['10'], want: 10 },
  ];

  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = calPoints(c.in); // 把 calPoints(字符.in) 存入 got
    if (got !== c.want) {
      // 若 got 不等于 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL calPoints(' +
          JSON.stringify(c.in) +
          ')=' +
          got +
          ' want ' +
          c.want,
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
