// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113233
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function evalRPN(tokens: string[]): number {
    // 定义函数/方法 evalRPN
    const stack: number[] = []; // 把 []; 写入 const stack: number[]
    for (const token of tokens) {
      // for (const token of tokens) {
      if (token !== '+' && token !== '-' && token !== '*' && token !== '/') {
        stack.push(parseInt(token, 10)); // 把 转整数(token, 10 压入栈/数组尾部
      } else {
        // 否则
        const num2 = stack.pop() as number; // 把 栈 弹出 ) as number 存入 num2
        const num1 = stack.pop() as number; // 把 栈 弹出 ) as number 存入 num1
        if (token === '+')
          stack.push(num1 + num2); // 若 token 全等于 「 加 」) 栈 追加 num1 加 num2);
        else if (token === '-')
          stack.push(num1 - num2); // 否则，若 token 全等于 「 减 」) 栈 追加 num1 减 num2);
        else if (token === '*')
          stack.push(num1 * num2); // 否则，若 token 全等于 「 乘 」) 栈 追加 num1 乘 num2);
        else stack.push(Math.trunc(num1 / num2)); // 否则
      }
    }
    return stack.pop() as number; // 返回 栈 弹出 ) as number
  }
  const cases = [
    { t: ['2', '1', '+', '3', '*'], want: 9 },
    { t: ['4', '13', '5', '/', '+'], want: 6 },
    {
      t: ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'],
      want: 22,
    },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = evalRPN(c.t); // 把 evalRPN(字符.另一字符串) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
