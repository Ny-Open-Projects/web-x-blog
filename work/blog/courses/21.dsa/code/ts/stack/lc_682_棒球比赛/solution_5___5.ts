/**
 ** LeetCode 682. 棒球比赛
 ** 方案：方案5
 ** 来源：https://blog.csdn.net/tyro_java/article/details/130734875
 */

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function calPoints(operations: string[]): number {
    // 定义函数/方法 calPoints
    // 初始化容器
    const numStack: number[] = []; // 把 []; 写入 const numStack: number[]
    // 累加器
    const sum = (nums: number[]) => {
      return nums.reduce((i, j) => i + j, 0);
    };
    // 操作对应数组
    const operationMap: { [key: string]: () => void } = {
      C: () => {
        numStack.pop();
      },
      D: () => numStack.push(numStack[numStack.length - 1] * 2),
      '+': () => numStack.push(sum(numStack.slice(-2))),
    };
    // 判断是否为整数（含负号），与 python 参考的 isdigit 检查一致
    const isInt = (s: string) => /^-?\d+$/.test(s);
    // 遍历操作数进行匹配操作
    operations.forEach((o) => {
      if (isInt(o)) {
        // 若 isInt(o
        numStack.push(parseInt(o, 10)); // 把 转整数(o, 10 压入栈/数组尾部
      } else {
        // 否则
        operationMap[o](); // operationMap[o]();
      }
    }); // });
    return sum(numStack); // 返回 累计和(numStack)
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
