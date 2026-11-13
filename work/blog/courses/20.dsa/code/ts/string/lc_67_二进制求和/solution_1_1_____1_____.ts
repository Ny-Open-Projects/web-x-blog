// 二进制求和：使用 BigInt 按二进制相加（忠实于 Python bin(int(a,2)+int(b,2))）

function addBinary(a: string, b: string): string {
  // 定义函数/方法 addBinary
  const x = BigInt('0b' + a); // 把 BigInt(「0b」 加 数组) 存入 x
  const y = BigInt('0b' + b); // 把 BigInt(「0b」 加 b) 存入 y
  return (x + y).toString(2); // 返回 (x 加 y).toString(2)
}

// 自检用例：(a, b, 期望)
const cases: [string, string, string][] = [
  ['11', '1', '100'],
  ['1010', '1011', '10101'],
  ['0', '0', '0'],
];

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  for (const [a, b, want] of cases) {
    // for (const [数组, b, want] of cases) {
    const got = addBinary(a, b); // 把 addBinary(数组, b) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(`FAIL: addBinary(${a},${b})=${got} want ${want}`);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
